# -*- coding: utf-8 -*-
"""
Example: List WhatsApp templates for a given WABA.
"""
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.whatsapp_templates.list(
    waba_id='<waba_id>',
    template_name='my_template',
    limit=20,
    offset=0,
)

print(response)