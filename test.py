#!/usr/bin/env python
from intercom import IntercomClient

client = IntercomClient("<APP_ID>", "<APP_API_KEY>")

print client.tags.get_list()