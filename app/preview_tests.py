import unittest
from app.utility import initialize_test_connection

try:
    from .preview import Params, preview_function
except ImportError:
    from preview import Params, preview_function


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
        response, params = id_connection, {"server": "http://20.117.225.136:8000", "api_endpoint": "resistance/"}
        result = preview_function(response, params)

        self.assertIn("preview", result)
        self.assertIsNotNone(result["preview"])

    def test_api_endpoint_resistors(self):
        id_connection = initialize_test_connection()
        response, params = id_connection, {"server": "http://20.117.225.136:8000", "api_endpoint": "resistors/"}
        result = preview_function(response, params)

        self.assertIn("preview", result)
        self.assertIsNotNone(result["preview"])


if __name__ == "__main__":
    unittest.main()
