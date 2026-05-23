import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.verify_apps.update(
    app_uuid='your-app-uuid',
    name='UpdatedAppName',
    otp_length=4,
    sms_channel=True,
)

print(response)