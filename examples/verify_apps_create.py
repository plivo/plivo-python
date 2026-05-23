import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.verify_apps.create(
    name='MyVerifyApp',
    brand_name='MyBrand',
    otp_type='numeric',
    otp_length=6,
    otp_expiry=300,
    otp_attempts=3,
    max_validation_attempts=5,
    sms_channel=True,
    voice_channel=False,
    wa_channel=False,
    is_default=False,
    message_redaction=False,
    enable_fraudshield=False,
    number_pool='my-number-pool',
)

print(response)