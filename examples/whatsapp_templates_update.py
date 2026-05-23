# -*- coding: utf-8 -*-
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

# Update a WhatsApp template without application_id
response = client.whatsapp_templates.update(
    waba_id='your_waba_id',
    template_id='your_template_id',
    components=[
        {
            'type': 'BODY',
            'text': 'Hello, this is an updated template message.',
        }
    ],
)
print(response)

# Update a WhatsApp template with optional application_id
response = client.whatsapp_templates.update(
    waba_id='your_waba_id',
    template_id='your_template_id',
    components=[
        {
            'type': 'BODY',
            'text': 'Hello, this is an updated template message.',
        }
    ],
    application_id='your_application_id',
)
print(response)