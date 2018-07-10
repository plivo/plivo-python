import plivo

client = plivo.RestAPI('MAYJRIYWM2MZE5YTRHMZ', 'YTA4M2JhNTYzODExZmEzZmQ5MDQzYzNjOTQ5YzMw')
# message_created = client.messages.create(
#     dst='918700484807',
#     text='Hello, testing message',
#     powerpack_uuid='479a8ac7-ecb4-434c-aa0a-95163736a1c4'
# )
params = {
    'src': '17049124420',
    'dst': '918700484807',
    'text': 'Hello, testing message',
    'powerpack_uuid': '479a8ac7-ecb4-434c-aa0a-95163736a1c4'
}
message_created = client.send_message(params)
print(message_created)
