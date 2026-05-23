# -*- coding: utf-8 -*-
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

# Create a WhatsApp template without application_id
response = client.whatsapp_templates.create(
    waba_id='your_waba_id',
    name='your_template_name',
    language='en_US',
    category='MARKETING',
    components=[
        {
            'type': 'BODY',
            'text': 'Hello, this is a template message.',
        }
    ],
)
print(response)

# Create a WhatsApp template with optional application_id
response = client.whatsapp_templates.create(
    waba_id='your_waba_id',
    name='your_template_name',
    language='en_US',
    category='MARKETING',
    components=[
        {
            'type': 'BODY',
            'text': 'Hello, this is a template message.',
        }
    ],
    application_id='your_application_id',
)
print(response)