import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

response = client.verify_apps.list(
    limit=20,
    offset=0,
    status='active',
)

print(response)