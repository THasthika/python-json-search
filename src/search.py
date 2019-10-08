import loader
import models

SEARCH_TYPE_ORGANIZATION = 'organization'
SEARCH_TYPE_USER = 'user'
SEARCH_TYPE_TICKET = 'ticket'


class SearchManager(object):

    __instance = None

    organizations = {}
    tickets = {}
    users = {}

    # organization mappings
    organization_mappings = {
        models.ORGANIZATION_FIELD_URL: {},
        models.ORGANIZATION_FIELD_EXTERNAL_ID: {},
        models.ORGANIZATION_FIELD_NAME: {},
        models.ORGANIZATION_FIELD_DOMAIN_NAMES: {},
        models.ORGANIZATION_FIELD_CREATED_AT: {},
        models.ORGANIZATION_FIELD_DETAILS: {},
        models.ORGANIZATION_FIELD_SHARED_TICKETS: {},
        models.ORGANIZATION_FIELD_TAGS: {}
    }

    # user mappings
    user_mappings = {
        models.USER_FIELD_URL: {},
        models.USER_FIELD_EXTERNAL_ID: {},
        models.USER_FIELD_NAME: {},
        models.USER_FIELD_ALIAS: {},
        models.USER_FIELD_CREATED_AT: {},
        models.USER_FIELD_ACTIVE: {},
        models.USER_FIELD_VERIFIED: {},
        models.USER_FIELD_SHARED: {},
        models.USER_FIELD_LOCALE: {},
        models.USER_FIELD_TIMEZONE: {},
        models.USER_FIELD_LAST_LOGIN_AT: {},
        models.USER_FIELD_EMAIL: {},
        models.USER_FIELD_PHONE: {},
        models.USER_FIELD_SIGNATURE: {},
        models.USER_FIELD_ORGANIZATION_ID: {},
        models.USER_FIELD_TAGS: {},
        models.USER_FIELD_SUSPENDED: {},
        models.USER_FIELD_ROLE: {}
    }

    # ticket mappings
    ticket_mappings = {
        models.TICKET_FIELD_URL: {},
        models.TICKET_FIELD_EXTERNAL_ID: {},
        models.TICKET_FIELD_CREATED_AT: {},
        models.TICKET_FIELD_TYPE: {},
        models.TICKET_FIELD_SUBJECT: {},
        models.TICKET_FIELD_DESCRIPTION: {},
        models.TICKET_FIELD_PRIORITY: {},
        models.TICKET_FIELD_STATUS: {},
        models.TICKET_FIELD_SUBMITTER_ID: {},
        models.TICKET_FIELD_ASSIGNEE_ID: {},
        models.TICKET_FIELD_ORGANIZATION_ID: {},
        models.TICKET_FIELD_TAGS: {},
        models.TICKET_FIELD_HAS_INCIDENTS: {},
        models.TICKET_FIELD_DUE_AT: {},
        models.TICKET_FIELD_VIA: {}
    }

    @staticmethod
    def getInstance():
        """
        Returns the instance.

        Parameters:

        Returns:
            SearchManager: Search Manager Class.
        """
        if SearchManager.__instance is None:
            SearchManager()
        return SearchManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SearchManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SearchManager.__instance = self

        self._init_organizations()
        self._init_users()
        self._init_tickets()

    def _init_organizations(self):
        data = loader.load_organizations()
        if data is None:
            raise Exception("Could not read organizations data store.")
        for d in data:
            _id = d[models.ORGANIZATION_FIELD_ID]
            self.organizations[_id] = d

            # set mappings
            for f in models.ORGANIZATION_FIELDS:
                if f == models.ORGANIZATION_FIELD_ID:
                    continue
                if f in d:
                    fval = d[f]
                else:
                    fval = None

                # array of items
                if f in [models.ORGANIZATION_FIELD_DOMAIN_NAMES,
                         models.ORGANIZATION_FIELD_TAGS]:
                    for v in fval:
                        if v not in self.organization_mappings[f]:
                            self.organization_mappings[f][v] = set()
                        self.organization_mappings[f][v].add(_id)
                    continue

                # normal mappings
                if fval not in self.organization_mappings[f]:
                    self.organization_mappings[f][fval] = set()
                self.organization_mappings[f][fval].add(_id)

    def _init_users(self):
        data = loader.load_users()
        if data is None:
            raise Exception("Could not read users data store.")
        for d in data:
            _id = d[models.USER_FIELD_ID]
            self.users[_id] = d

            # set mappings
            for f in models.USER_FIELDS:
                if f == models.USER_FIELD_ID:
                    continue
                if f in d:
                    fval = d[f]
                else:
                    fval = None

                # array of items
                if f == models.USER_FIELD_TAGS:
                    for v in fval:
                        if v not in self.user_mappings[f]:
                            self.user_mappings[f][v] = set()
                        self.user_mappings[f][v].add(_id)
                    continue

                # normal mappings
                if fval not in self.user_mappings[f]:
                    self.user_mappings[f][fval] = set()
                self.user_mappings[f][fval].add(_id)

    def _init_tickets(self):
        data = loader.load_tickets()
        if data is None:
            raise Exception("Could not read tickets data store.")
        for d in data:
            _id = d[models.TICKET_FIELD_ID]
            self.tickets[_id] = d

            # set mappings
            for f in models.TICKET_FIELDS:
                if f == models.TICKET_FIELD_ID:
                    continue
                if f in d:
                    fval = d[f]
                else:
                    fval = None

                # array of items
                if f == models.TICKET_FIELD_TAGS:
                    for v in fval:
                        if v not in self.ticket_mappings[f]:
                            self.ticket_mappings[f][v] = set()
                        self.ticket_mappings[f][v].add(_id)
                    continue

                # normal mappings
                if fval not in self.ticket_mappings[f]:
                    self.ticket_mappings[f][fval] = set()
                self.ticket_mappings[f][fval].add(_id)

    # given type returns the data structures that hold that type
    def _get_storage(self, type):
        if type == SEARCH_TYPE_USER:
            return (self.users, self.user_mappings)
        elif type == SEARCH_TYPE_TICKET:
            return (self.tickets, self.ticket_mappings)
        elif type == SEARCH_TYPE_ORGANIZATION:
            return (self.organizations, self.organization_mappings)
        return (None, None)

    # return ids of matching data fields
    def _get_ids(self, type, field, value):
        (coll, coll_mapping) = self._get_storage(type)
        if coll is None or coll_mapping is None:
            return []
        if field in [models.USER_FIELD_ID,
                     models.TICKET_FIELD_ID,
                     models.ORGANIZATION_FIELD_ID]:
            if value not in coll:
                return []
            return [value]
        if field not in coll_mapping:
            return []
        if value not in coll_mapping[field]:
            return []
        return coll_mapping[field][value]

    def _get_user_string(self, id):

        user = self.users[id]

        # get organization name
        if models.USER_FIELD_ORGANIZATION_ID in user:
            org_id = user[models.USER_FIELD_ORGANIZATION_ID]
            org = self.organizations[org_id]
            org_name = org[models.ORGANIZATION_FIELD_NAME]
        else:
            org_name = "NULL"

        # get tickets
        submitted_ticket_ids = self._get_ids(
            SEARCH_TYPE_TICKET, models.TICKET_FIELD_SUBMITTER_ID, id
        )
        assigned_ticket_ids = self._get_ids(
            SEARCH_TYPE_TICKET, models.TICKET_FIELD_ASSIGNEE_ID, id
        )
        ticket_ids = set(list(submitted_ticket_ids) +
                         list(assigned_ticket_ids))
        tickets = []
        for tid in ticket_ids:
            ticket = self.tickets[tid]
            tickets.append(ticket[models.TICKET_FIELD_SUBJECT])

        # construct the user string
        ret = ""
        for f in models.USER_FIELDS:
            if f in user:
                ret += "{:20}: {}".format(f, user[f])
            else:
                ret += "{:20}: null".format(f)
            ret += "\n"
        ret += "{:20}: {}\n".format("Organization", org_name)
        for (i, v) in enumerate(tickets):
            ret += "{:20}: {}\n".format("Ticket{}".format(i), v)
        ret += "-"*80
        return ret

    def _get_ticket_string(self, id):

        ticket = self.tickets[id]

        # get organization name
        if models.TICKET_FIELD_ORGANIZATION_ID in ticket:
            org_id = ticket[models.TICKET_FIELD_ORGANIZATION_ID]
            org = self.organizations[org_id]
            org_name = org[models.ORGANIZATION_FIELD_NAME]
        else:
            org_name = "NULL"

        # get submitter name
        if models.TICKET_FIELD_SUBMITTER_ID in ticket:
            submitter_id = ticket[models.TICKET_FIELD_SUBMITTER_ID]
            submitter = self.users[submitter_id]
            submitter_name = submitter[models.USER_FIELD_NAME]
        else:
            submitter_name = "NULL"

        # get assignee name
        if models.TICKET_FIELD_ASSIGNEE_ID in ticket:
            assignee_id = ticket[models.TICKET_FIELD_ASSIGNEE_ID]
            assignee = self.users[assignee_id]
            assignee_name = assignee[models.USER_FIELD_NAME]
        else:
            assignee_name = "NULL"

        # construct the ticket string
        ret = ""
        for f in models.TICKET_FIELDS:
            if f in ticket:
                ret += "{:20}: {}".format(f, ticket[f])
            else:
                ret += "{:20}: null".format(f)
            ret += "\n"
        ret += "{:20}: {}\n".format("Organization", org_name)
        ret += "{:20}: {}\n".format("Submitter", submitter_name)
        ret += "{:20}: {}\n".format("Assignee", assignee_name)
        ret += "-"*80
        return ret

    def _get_organization_string(self, id):

        organization = self.organizations[id]

        # get users
        user_ids = self._get_ids(
            SEARCH_TYPE_USER, models.USER_FIELD_ORGANIZATION_ID, id
        )
        users = []
        for uid in user_ids:
            user = self.users[uid]
            users.append(user[models.USER_FIELD_NAME])

        # get tickets
        ticket_ids = self._get_ids(
            SEARCH_TYPE_TICKET, models.TICKET_FIELD_ORGANIZATION_ID, id
        )
        tickets = []
        for tid in ticket_ids:
            ticket = self.tickets[tid]
            tickets.append(ticket[models.TICKET_FIELD_SUBJECT])

        # construct the user string
        ret = ""
        for f in models.ORGANIZATION_FIELDS:
            if f in organization:
                ret += "{:20}: {}".format(f, organization[f])
            else:
                ret += "{:20}: null".format(f)
            ret += "\n"
        for (i, v) in enumerate(users):
            ret += "{:20}: {}\n".format("User{}".format(i), v)
        for (i, v) in enumerate(tickets):
            ret += "{:20}: {}\n".format("Ticket{}".format(i), v)
        ret += "-"*80
        return ret

    def _get_string(self, type, id):
        if type == SEARCH_TYPE_USER:
            return self._get_user_string(id)
        elif type == SEARCH_TYPE_TICKET:
            return self._get_ticket_string(id)
        elif type == SEARCH_TYPE_ORGANIZATION:
            return self._get_organization_string(id)
        return ""

    def search(self, type, field, value):
        ids = self._get_ids(type, field, value)
        ret = ""
        for id in ids:
            s = self._get_string(type, id)
            if s == "":
                continue
            ret += s
            ret += "\n"
        if ret == "":
            return None
        return ret
