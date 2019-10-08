import json

USERS_JSON_FILE = '../data/users.json'
ORGANIZATIONS_JSON_FILE = '../data/organizations.json'
TICKETS_JSON_FILE = '../data/tickets.json'


def _load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except IOError:
        return None


def load_organizations():
    return _load_json(ORGANIZATIONS_JSON_FILE)


def load_users():
    return _load_json(USERS_JSON_FILE)


def load_tickets():
    return _load_json(TICKETS_JSON_FILE)
