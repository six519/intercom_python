#!/usr/bin/env python
from intercom import IntercomClient

client = IntercomClient("xz7mkzq7", "5b79b8a73fa86637db14aea565cfe5d203310296")

print client.tags.get_list()