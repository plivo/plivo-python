import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

app_uuid = 'your-app-uuid'

response = client.verify_apps.get(app_uuid)

print(response)