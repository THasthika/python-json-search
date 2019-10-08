from .loader import load_organizations, load_users, load_tickets


class Search(object):

    __instance = None

    organizations = {}
    tickets = {}
    users = {}

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Search.__instance is None:
            Search()
        return Search.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Search.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Search.__instance = self

        self.organizations = load_organizations()
        self.users = load_users()
        self.tickets = load_tickets()
