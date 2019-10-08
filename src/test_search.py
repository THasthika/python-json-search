import unittest

from .search import Search


class TestSearch(unittest.TestCase):

    def test_init(self):

        s = Search.getInstance()

        print(s)
