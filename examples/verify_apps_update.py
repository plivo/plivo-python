import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

app_uuid = 'your-app-uuid'

response = client.verify_apps.update(
    app_uuid,
    name='UpdatedAppName',
    otp_length=8,
    enable_fraudshield=True,
    fs_protection_level='high',
)

print(response)