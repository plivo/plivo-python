# -*- coding: utf-8 -*-
"""
Example: Retrieve a WhatsApp template by its ID.
"""
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.whatsapp_templates.get(
    waba_id='<waba_id>',
    template_id='<template_id>',
)

print(response)