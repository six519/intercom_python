intercom-python
===============

A not official python bindings to Intercom API

Installation
============

``pip install intercom_python``

Usage
=====
::

	from intercom import IntercomClient
	client = IntercomClient("", "")

	# create user
	print client.users.create({"email": "ferdinandsilva@ferdinandsilva.com"})

	# list user
	print client.users.get_list()
	
	# delete user
	print client.users.delete({"email": "ferdinandsilva@ferdinandsilva.com"})

Warning
=======

Not yet done!!!!!