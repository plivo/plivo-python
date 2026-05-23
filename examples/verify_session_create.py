# -*- coding: utf-8 -*-
"""
Example: Create a Verify Session (generate OTP)
"""
import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

# Minimal creation — no optional params required
response = client.verify_session.create()
print(response)

# Full creation with all optional params
response = client.verify_session.create(
    app_hash='android_app_hash_value',
    brand_name='MyBrand',
    code_length=6,
    dlt_entity_id='dlt_entity_id_value',
    dlt_sender_id='dlt_sender_id_value',
    dlt_template_category='transactional',
    dlt_template_id='dlt_template_id_value',
    dlt_text='Your OTP is {otp}',
    dtmf=1,
    fraud_check='medium',
    text='Your OTP is {otp}. It is valid for 10 minutes.',
)
print(response)