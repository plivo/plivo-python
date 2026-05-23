# -*- coding: utf-8 -*-
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.rcs_assistant_events.create()

print(response)