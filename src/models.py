# Organization
'''
_id = attr.ib(default=None)
url = attr.ib(default=None)
external_id = attr.ib(default=None)
name = attr.ib(default=None)
domain_names = attr.ib(default=None)
created_at = attr.ib(default=None)
details = attr.ib(default=None)
shared_tickets = attr.ib(default=None)
tags = attr.ib(default=None)
}
'''

ORGANIZATION_FIELD_ID = '_id'
ORGANIZATION_FIELD_URL = 'url'
ORGANIZATION_FIELD_EXTERNAL_ID = 'external_id'
ORGANIZATION_FIELD_NAME = 'name'
ORGANIZATION_FIELD_DOMAIN_NAMES = 'domain_names'
ORGANIZATION_FIELD_CREATED_AT = 'created_at'
ORGANIZATION_FIELD_DETAILS = 'details'
ORGANIZATION_FIELD_SHARED_TICKETS = 'shared_tickets'
ORGANIZATION_FIELD_TAGS = 'tags'

ORGANIZATION_FIELDS = [
    ORGANIZATION_FIELD_ID,
    ORGANIZATION_FIELD_URL,
    ORGANIZATION_FIELD_EXTERNAL_ID,
    ORGANIZATION_FIELD_NAME,
    ORGANIZATION_FIELD_DOMAIN_NAMES,
    ORGANIZATION_FIELD_CREATED_AT,
    ORGANIZATION_FIELD_DETAILS,
    ORGANIZATION_FIELD_SHARED_TICKETS,
    ORGANIZATION_FIELD_TAGS
]

# User
'''
User
  _id = attr.ib(default=None)
  url = attr.ib(default=None)
  external_id = attr.ib(default=None)
  name:
  alias:
  created_at = attr.ib(default=None)
  active = attr.ib(default=None)
  verified = attr.ib(default=None)
  shared = attr.ib(default=None)
  locale = attr.ib(default=None)
  timezone = attr.ib(default=None)
  last_login_at = attr.ib(default=None)
  email = attr.ib(default=None)
  phone = attr.ib(default=None)
  signature = attr.ib(default=None)
  organization_id = attr.ib(default=None)
  tags = attr.ib(default=None)
  suspended = attr.ib(default=None)
  role = attr.ib(default=None)
'''

USER_FIELD_ID = '_id'
USER_FIELD_URL = 'url'
USER_FIELD_EXTERNAL_ID = 'external_id'
USER_FIELD_NAME = 'name'
USER_FIELD_ALIAS = 'alias'
USER_FIELD_CREATED_AT = 'created_at'
USER_FIELD_ACTIVE = 'active'
USER_FIELD_VERIFIED = 'verified'
USER_FIELD_SHARED = 'shared'
USER_FIELD_LOCALE = 'locale'
USER_FIELD_TIMEZONE = 'timezone'
USER_FIELD_LAST_LOGIN_AT = 'last_login_at'
USER_FIELD_EMAIL = 'email'
USER_FIELD_PHONE = 'phone'
USER_FIELD_SIGNATURE = 'signature'
USER_FIELD_ORGANIZATION_ID = 'organization_id'
USER_FIELD_TAGS = 'tags'
USER_FIELD_SUSPENDED = 'suspended'
USER_FIELD_ROLE = 'role'

USER_FIELDS = [
    USER_FIELD_ID,
    USER_FIELD_URL,
    USER_FIELD_EXTERNAL_ID,
    USER_FIELD_NAME,
    USER_FIELD_ALIAS,
    USER_FIELD_CREATED_AT,
    USER_FIELD_ACTIVE,
    USER_FIELD_VERIFIED,
    USER_FIELD_SHARED,
    USER_FIELD_LOCALE,
    USER_FIELD_TIMEZONE,
    USER_FIELD_LAST_LOGIN_AT,
    USER_FIELD_EMAIL,
    USER_FIELD_PHONE,
    USER_FIELD_SIGNATURE,
    USER_FIELD_ORGANIZATION_ID,
    USER_FIELD_TAGS,
    USER_FIELD_SUSPENDED,
    USER_FIELD_ROLE
]


# Ticket
'''
Ticket:
  _id = attr.ib(default=None)
  url = attr.ib(default=None)
  external_id = attr.ib(default=None)
  created_at = attr.ib(default=None)
  type = attr.ib(default=None)
  subject = attr.ib(default=None)
  description = attr.ib(default=None)
  priority = attr.ib(default=None)
  status = attr.ib(default=None)
  submitter_id = attr.ib(default=None)
  assignee_id = attr.ib(default=None)
  organization_id = attr.ib(default=None)
  tags = attr.ib(default=None)
  has_incidents = attr.ib(default=None)
  due_at = attr.ib(default=None)
  via = attr.ib(default=None)
'''

TICKET_FIELD_ID = '_id'
TICKET_FIELD_URL = 'url'
TICKET_FIELD_EXTERNAL_ID = 'external_id'
TICKET_FIELD_CREATED_AT = 'created_at'
TICKET_FIELD_TYPE = 'type'
TICKET_FIELD_SUBJECT = 'subject'
TICKET_FIELD_DESCRIPTION = 'description'
TICKET_FIELD_PRIORITY = 'priority'
TICKET_FIELD_STATUS = 'status'
TICKET_FIELD_SUBMITTER_ID = 'submitter_id'
TICKET_FIELD_ASSIGNEE_ID = 'assignee_id'
TICKET_FIELD_ORGANIZATION_ID = 'organization_id'
TICKET_FIELD_TAGS = 'tags'
TICKET_FIELD_HAS_INCIDENTS = 'has_incidents'
TICKET_FIELD_DUE_AT = 'due_at'
TICKET_FIELD_VIA = 'via'

TICKET_FIELDS = [
    TICKET_FIELD_ID,
    TICKET_FIELD_URL,
    TICKET_FIELD_EXTERNAL_ID,
    TICKET_FIELD_CREATED_AT,
    TICKET_FIELD_TYPE,
    TICKET_FIELD_SUBJECT,
    TICKET_FIELD_DESCRIPTION,
    TICKET_FIELD_PRIORITY,
    TICKET_FIELD_STATUS,
    TICKET_FIELD_SUBMITTER_ID,
    TICKET_FIELD_ASSIGNEE_ID,
    TICKET_FIELD_ORGANIZATION_ID,
    TICKET_FIELD_TAGS,
    TICKET_FIELD_HAS_INCIDENTS,
    TICKET_FIELD_DUE_AT,
    TICKET_FIELD_VIA
]


def valid_field(fields, field):
    if field in fields:
        return True
    return False
