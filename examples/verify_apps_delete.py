import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.verify_apps.delete(app_uuid='your-app-uuid')

print(response)