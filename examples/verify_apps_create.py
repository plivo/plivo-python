import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.verify_apps.create(
    name='MyVerifyApp',
    otp_length=6,
    otp_expiry=3,
    otp_attempts=3,
    brand_name='MyBrand',
    sms_channel=True,
    voice_channel=False,
    wa_channel=False,
    is_default=False,
    message_redaction=False,
    max_validation_attempts=5,
    enable_fraudshield=True,
    fs_protection_level='medium',
)

print(response)