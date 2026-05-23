# -*- coding: utf-8 -*-
"""
Example: Create a WhatsApp message template.
"""
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.whatsapp_templates.create(
    waba_id='<waba_id>',
    name='my_template',
    category='MARKETING',
    language='en_US',
    components=[
        {
            'type': 'BODY',
            'text': 'Hello, this is a test template.',
        }
    ],
    allow_category_change=True,
)

print(response)