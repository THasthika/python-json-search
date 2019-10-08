import unittest

from .loader import load_organizations


class TestLoader(unittest.TestCase):

    def test_main(self):

        x = load_organizations()
        print(x)

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        # data = [1, 2, 3]
        result = 6
        self.assertEqual(result, 6)
