import os
from typing import Any, TypedDict
import requests
from dotenv import load_dotenv
load_dotenv()

class Result(TypedDict):
    preview: Any

def preview_function(response: Any, params: Any) -> Result:
    """
    Function used to preview a student response.
    ---
    The handler function passes two arguments to preview_function():

    - `response` which are the answers provided by the student.
    - `params` which are any extra parameters that may be useful,
        e.g., error tolerances.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. It must also conform to the
    response schema.
    """
    try:
        api_endpoint = params.get("api_endpoint", 'resistance/')

        if len(response) != 6:
            raise Exception("Connection ID must be 6 characters long")

        api_response = requests.get(f"{os.environ.get('API_CONNECTION')}/{api_endpoint}{response}")
        api_response.raise_for_status()
        api_data = api_response.json()
    except requests.RequestException as e:
        print(f"Error API connection: {e}")
        api_data = None

    return Result(preview=api_data)