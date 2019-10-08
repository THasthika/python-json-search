import json

# from .models import ORGANIZATION_FIELDS

USERS_JSON_FILE = './data/users.json'
ORGANIZATIONS_JSON_FILE = './data/organizations.json'
TICKETS_JSON_FILE = './data/tickets.json'


def _load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


def _list_to_id_dict(data):
    ret = {}
    for d in data:
        ret[d['_id']] = d
    return ret


def load_organizations():
    data = _load_json(ORGANIZATIONS_JSON_FILE)
    return _list_to_id_dict(data)


def load_users():
    data = _load_json(USERS_JSON_FILE)
    return _list_to_id_dict(data)


def load_tickets():
    data = _load_json(TICKETS_JSON_FILE)
    return _list_to_id_dict(data)
