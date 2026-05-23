# -*- coding: utf-8 -*-
"""
Example: Delete a WhatsApp template by ID and name.
"""
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.whatsapp_templates.delete(
    waba_id='<waba_id>',
    template_id='<template_id>',
    name='my_template',
)

print(response)