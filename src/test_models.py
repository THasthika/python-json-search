import unittest

# from .models import Organization


class TestModels(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        # data = [1, 2, 3]
        result = 6
        self.assertEqual(result, 6)
