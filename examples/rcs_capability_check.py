# -*- coding: utf-8 -*-
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

# Check if a phone number is RCS-enabled
response = client.rcs_capability.check(
    phone_number='+14151234567',
    agent_uuid='your-agent-uuid',  # optional
)

print('API ID:', response.api_id)
print('Phone Number:', response.phone_number)
print('Is RCS Capable:', response.is_capable)
print('Features:', response.features)
print('Message:', response.message)
if response.error:
    print('Error:', response.error)