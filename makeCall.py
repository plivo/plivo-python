import plivo

client = plivo.RestClient('MAYJI2ZJDIMTVIODIWYJ','OTI2NWFmNGI4MmZjZjZkOTQ0YjNkYTQwMzY2ZDJl')
response = client.calls.create(
    from_='+919999323467',
    to_='sip:ajaydjv902035012689385@phone-qa.voice.plivodev.com',
    answer_url='https://s3.amazonaws.com/static.plivo.com/answer.xml',
    answer_method='GET', )
print(response)