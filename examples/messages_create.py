# Example of sending a message using Plivo API with AllowDTMF option
# Note: Replace 'your_auth_id' and 'your_auth_token' with your actual Plivo auth credentials

from plivo import RestClient

client = RestClient('your_auth_id', 'your_auth_token')

response = client.messages.create(
    src='1415XXXXXXX',  # The phone number sending the message
    dst='1415XXXXXXX',  # The phone number receiving the message
    text='Hello, this is a test message',  # Your SMS message
    allow_dtmf=True  # Optional parameter to allow DTMF
)

print(response)