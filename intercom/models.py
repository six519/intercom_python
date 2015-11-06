from .base import IntercomBaseModel

class IntercomUser(IntercomBaseModel):

    def __init__(self, base_request_url, app_id, app_api_key):
        self.base_request_url = base_request_url
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.name = "users"

class IntercomCompany(IntercomBaseModel):

    def __init__(self, base_request_url, app_id, app_api_key):
        self.base_request_url = base_request_url
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.name = "companies"

class IntercomContact(IntercomBaseModel):

    def __init__(self, base_request_url, app_id, app_api_key):
        self.base_request_url = base_request_url
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.name = "contacts"

class IntercomAdmin(IntercomBaseModel):

    def __init__(self, base_request_url, app_id, app_api_key):
        self.base_request_url = base_request_url
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.name = "admins"

class IntercomTag(IntercomBaseModel):

    def __init__(self, base_request_url, app_id, app_api_key):
        self.base_request_url = base_request_url
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.name = "tags"

class IntercomSegment(IntercomBaseModel):

    def __init__(self, base_request_url, app_id, app_api_key):
        self.base_request_url = base_request_url
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.name = "segments"