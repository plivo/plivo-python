# -*- coding: utf-8 -*-
"""
Example: Update an existing WhatsApp message template.
"""
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.whatsapp_templates.update(
    waba_id='<waba_id>',
    template_id='<template_id>',
    category='UTILITY',
    components=[
        {
            'type': 'BODY',
            'text': 'Updated template body.',
        }
    ],
)

print(response)