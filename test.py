#!/usr/bin/env python
"""
 There's no Python client library for Intercom API so I created one

 https://github.com/six519/intercom_python
"""
from intercom import IntercomClient

client = IntercomClient("<APP_ID>", "<APP_API_KEY>")

print client.conversations.get_list()