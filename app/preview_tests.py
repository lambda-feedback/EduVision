import unittest
from app.utility import initialize_test_connection
from dotenv import load_dotenv
load_dotenv()

try:
    from .preview import preview_function
except ImportError:
    from preview import preview_function


class TestPreviewFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practice to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use preview_function() to check your algorithm works
    as it should.
    """

    def test_api_endpoint_resistance(self):
        id_connection = initialize_test_connection()
        response, params = id_connection, {"api_endpoint": "resistance/", "correct_answer": 0.0}
        result = preview_function(response, params)

        self.assertIn("preview", result)
        self.assertIsNotNone(result["preview"])

    def test_api_endpoint_resistors(self):
        id_connection = initialize_test_connection()
        response, params = id_connection, {"api_endpoint": "resistors/", "correct_answer": 0.0}
        result = preview_function(response, params)

        self.assertIn("preview", result)
        self.assertIsNotNone(result["preview"])


if __name__ == "__main__":
    unittest.main()
