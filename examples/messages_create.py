# Example of sending a message with allow_dtmf using Plivo API

import plivo

client = plivo.RestClient("auth_id", "auth_token")

response = client.messages.create(
    src='14151234567',  # Sender's phone number with country code
    dst='14157654321',  # Receiver's phone number with country code
    text='Test message with DTMF allowed',
    allow_dtmf=True
)

print(response)