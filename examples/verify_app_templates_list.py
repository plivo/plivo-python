# -*- coding: utf-8 -*-
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.verify_app_templates.list()

print('API ID:', response.api_id)
print('Templates:')
for template in response:
    print(' -', template)