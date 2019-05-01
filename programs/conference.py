import plivo
client = plivo.RestClient('MAYMI3MZA5MZAWNJUXMD','YWU1MzJiMjBiZjBiMDQ4OTcyZDQ4YzBlZWEyZjgx')

"""
response = client.conferences.record(
    conference_name='testing',
    transcription_url='qigryfbeuor')
print(response)
-----------
Response:
plivo.exceptions.ValidationError: ['transcription_url should match format
(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|None) (actual value: qigryfbeuor)']
"""
