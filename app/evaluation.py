import os
from typing import TypedDict
import requests
from dotenv import load_dotenv

load_dotenv()


class Result(TypedDict):
    is_correct: bool
    error: int


def evaluation_function(response, answer, params) -> Result:
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - `response` which are the answers provided by the student.
    - `answer` which are the correct answers to compare against.
    - `params` which are any extra parameters that may be useful,
        e.g., error tolerances.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. It must also conform to the
    response schema.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that evaluation_function() is the main function used
    to output the evaluation response.
    """
    global is_correct
    global error_output
    error_output = 0
    try:
        api_endpoint = params.get("api_endpoint", "resistance/")

        if len(response) != 6:
            error_output = 1
            is_correct = False
            raise Exception("Connection ID must be 6 characters long")

        api_response = requests.post(
            f"{os.environ.get('API_CONNECTION')}/{api_endpoint}{response}"
        )
        api_data = api_response.json()

        if isinstance(api_data, list) and len(api_data) > 0:
            api_data = str(api_data)

        if response == "000000":
            is_correct = True
        elif api_data in [
            params.get("correct_answer", None),
            -1.0,
            [{"resistance": -1}],
        ]:
            if response == "resistors/":
                len_data = len(api_data)
                if len_data != len(params.get("correct_answer", None)):
                    is_correct = False
                    error_output = 2
                else:
                    for i in params.get("correct_answer", None):
                        if i not in api_data:
                            is_correct = False
                            error_output = 3
            elif response == "resistance/":
                if api_data != params.get("correct_answer", None):
                    is_correct = False
                    error_output = 4
            is_correct = True
        else:
            is_correct = False
            error_output = 5
    except requests.RequestException as e:
        print(f"Error API connection: {e}")
        is_correct = False
        error_output = 6

    return Result(is_correct=is_correct, error=error_output)

