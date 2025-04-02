import os
import unittest
from app.utility import initialize_test_connection

try:
    from .evaluation import Params, evaluation_function
except ImportError:
    from evaluation import Params, evaluation_function



class TestEvaluationFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practise to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use evaluation_function() to check your algorithm works
    as it should.
    """

    def test_connection(self):
        id_connection = initialize_test_connection()

        response, answer, params = id_connection, 0.0, {"api_endpoint": "resistance/"}
        result = evaluation_function(response, answer, params)

        self.assertEqual(result.get("is_correct"), True)

if __name__ == "__main__":
    unittest.main()
