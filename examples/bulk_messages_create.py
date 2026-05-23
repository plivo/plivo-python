# -*- coding: utf-8 -*-
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.bulk_messages.create(
    src='+14155551234',
    dst='+14155550001<+14155550002<+14155550003',
    text='Hello from Plivo Bulk Messaging!',
    type_='sms',
    url='https://example.com/delivery_status',
    method='POST',
    log=False,
)

print('API ID:', response.api_id)
print('Message UUIDs:', response.message_uuid)
print('Status:', response.message)