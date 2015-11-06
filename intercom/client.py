from models import *

INTERCOM_API_BASE_URL = "https://api.intercom.io/"

class IntercomClient(object):

    def __init__(self, app_id, app_api_key):
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.users = IntercomUser(INTERCOM_API_BASE_URL, app_id, app_api_key)
        self.companies = IntercomCompany(INTERCOM_API_BASE_URL, app_id, app_api_key)
        self.contacts = IntercomContact(INTERCOM_API_BASE_URL, app_id, app_api_key)
        self.admins = IntercomAdmin(INTERCOM_API_BASE_URL, app_id, app_api_key)
        self.tags = IntercomTag(INTERCOM_API_BASE_URL, app_id, app_api_key)
        self.segments = IntercomSegment(INTERCOM_API_BASE_URL, app_id, app_api_key)