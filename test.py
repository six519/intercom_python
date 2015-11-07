#!/usr/bin/env python
"""
 There's no Python client library for Intercom API so I created one

 https://github.com/six519/intercom_python
"""
from intercom import IntercomClient

client = IntercomClient("xz7mkzq7", "5b79b8a73fa86637db14aea565cfe5d203310296")

#print client.users.create({"email": "ferdinandsilva@ferdinandsilva.com"})
#print client.users.get_list()

"""
print client.events.create({
  "event_name": 'Foo',
  "created_at": 1439826340,
  "user_id": 'bar'
})
"""

print client.users.delete({"email": "ferdinandsilva@ferdinandsilva.com"})