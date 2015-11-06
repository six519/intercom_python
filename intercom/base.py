import json

try:
    import requests
    from requests.auth import HTTPBasicAuth
except:
    pass

class IntercomBaseModel(object):

    def __init__(self, base_request_url, app_id, app_api_key):

        self.app_id = app_id
        self.app_api_key = app_api_key
        self.base_request_url = base_request_url
        self.name = ""

    def get_list(self, *args, **kwargs):
        ret = requests.get("%s%s" % (self.base_request_url, self.name), auth=HTTPBasicAuth(self.app_id, self.app_api_key), headers={'content-type': 'application/json', 'accept': 'application/json'})

        return ret.json()

    def create(self, request_dict={}):
        ret = requests.post("%s%s" % (self.base_request_url, self.name), json.dumps(request_dict), auth=HTTPBasicAuth(self.app_id, self.app_api_key), headers={'content-type': 'application/json', 'accept': 'application/json'})

        return ret.json()
