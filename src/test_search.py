import unittest

import search


class TestSearch(unittest.TestCase):

    def test_init(self):
        s = search.SearchManager.getInstance()
        self.assertIsNotNone(s)

    def test_search_empty(self):
        res = search.SearchManager.getInstance().search(
            search.SEARCH_TYPE_USER, '_id', 0)
        self.assertIsNone(res)

    def test_search_not_empty(self):
        res = search.SearchManager.getInstance().search(
            search.SEARCH_TYPE_USER, '_id', 1
        )
        self.assertIsNotNone(res)

    def test_search_tickets_pending(self):
        res = search.SearchManager.getInstance().search(
            search.SEARCH_TYPE_TICKET, 'status', 'pending'
        )
        self.assertIsNotNone(res)

    def test_search_user_active(self):
        res = search.SearchManager.getInstance().search(
            search.SEARCH_TYPE_USER, 'active', True
        )
        self.assertIsNotNone(res)
