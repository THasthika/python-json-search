import search
import models

_STATE_START = 0
_STATE_ENTER_TYPE = 1
_STATE_ENTER_FIELD = 2
_STATE_ENTER_VALUE = 3
_STATE_SHOWING_RESULT = 4


def sanitize_input(type, field, value):
    if value == "NULL":
        return None
    if type == search.SEARCH_TYPE_USER and field == models.USER_FIELD_ID:
        return int(value)
    if type == search.SEARCH_TYPE_ORGANIZATION \
            and field == models.ORGANIZATION_FIELD_ID:
        return int(value)
    if field in [
        models.USER_FIELD_ORGANIZATION_ID,
        models.TICKET_FIELD_ORGANIZATION_ID,
        models.TICKET_FIELD_SUBMITTER_ID,
        models.TICKET_FIELD_ASSIGNEE_ID
    ]:
        return int(value)
    return value


class SearchAppPrompt(object):

    state = _STATE_START
    stype = None
    sfield = None
    svalue = None
    result = None
    should_exit = False

    def loop(self):
        self.handle_state()
        self.update_state()
        if not self.should_exit:
            self.loop()

    # Handle and print state related stuff
    def handle_state(self):
        if self.state == _STATE_START:
            print("Welcome!")
            print("Type 'quit' to exit at any time, Press 'Enter' to Continue")

        elif self.state == _STATE_ENTER_TYPE:
            print("Choose Search Type:")
            print("1) Users | 2) Tickets | 3) Organizations")

        elif self.state == _STATE_ENTER_FIELD:
            print("Enter Field [type '?' to see fields]:")

        elif self.state == _STATE_ENTER_VALUE:
            print("Enter Value [type 'NULL' for null value]:")

        elif self.state == _STATE_SHOWING_RESULT:
            print("Press 'Enter' to Continue")

    # update state according to the current state and new input
    def update_state(self):
        inp = input("> ")

        if self.state == _STATE_START:
            if inp == '':
                self.state = _STATE_ENTER_TYPE

        elif self.state == _STATE_ENTER_TYPE:
            valid = True
            if inp == '1':
                self.stype = search.SEARCH_TYPE_USER
            elif inp == '2':
                self.stype = search.SEARCH_TYPE_TICKET
            elif inp == '3':
                self.stype = search.SEARCH_TYPE_ORGANIZATION
            else:
                print("please select a valid search type!")
                valid = False
            if valid:
                self.state = _STATE_ENTER_FIELD

        elif self.state == _STATE_ENTER_FIELD:

            fields = None
            if self.stype == search.SEARCH_TYPE_USER:
                fields = models.USER_FIELDS
            elif self.stype == search.SEARCH_TYPE_TICKET:
                fields = models.TICKET_FIELDS
            elif self.stype == search.SEARCH_TYPE_ORGANIZATION:
                fields = models.ORGANIZATION_FIELDS

            if fields is None:
                print("please select search type!")
                self.state = _STATE_ENTER_TYPE
                return

            if inp == '?':
                print("")
                if self.stype == search.SEARCH_TYPE_USER:
                    print("User Fields:")
                elif self.stype == search.SEARCH_TYPE_TICKET:
                    print("Ticket Fields:")
                elif self.stype == search.SEARCH_TYPE_ORGANIZATION:
                    print("Organization Fields:")
                print("\n".join(fields))
                print("")

            if inp not in fields:
                print("incorrect search field!")
            else:
                self.sfield = inp
                self.state = _STATE_ENTER_VALUE

        elif self.state == _STATE_ENTER_VALUE:
            self.svalue = sanitize_input(self.stype, self.sfield, inp)
            self.state = _STATE_SHOWING_RESULT
            result = search.SearchManager.getInstance().search(
                self.stype,
                self.sfield,
                self.svalue
            )
            if result is None:
                print("No results found!")
            else:
                print(result)
            return

        elif self.state == _STATE_SHOWING_RESULT:
            self.state = _STATE_ENTER_TYPE

        else:
            self.state = _STATE_START

        if inp == 'quit':
            self.should_exit = True
