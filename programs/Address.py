import plivo

client = plivo.RestClient('MAYMI3MZA5MZAWNJUXMD','YWU1MzJiMjBiZjBiMDQ4OTcyZDQ4YzBlZWEyZjgx')
#Create address:
"""
response = client.addresses.create(
    country_iso='DK',
    salutation='Mr',
    first_name='Kiran',
    last_name='Wayne',
    address_line1='854',
    address_line2='RUE DU COMMANDANT GUILBAUD',
    city='PARIS',
    region='PARIS',
    postal_code='75016',
    address_proof_type='others',
    phone_number_country='UK',
    number_type='Local')
print(response)

Observation : In docs we have mentioned "auto_correct_address" in doc in SDK we set the value to 'None'
and "callback_url" is not mentioned in the list of parameters. Also, the mandatory parameter "phone_number_country","number_type" is not
a part of allowed args in SDK.
 return self.client.addresses.update(
            self.id,
            salutation
	        first_name,
            last_name,
            country_iso,
            address_line1,
            address_line2,
            city,
            region,
            postal_code,
            alias,
            file_to_upload,
            auto_correct_address,
            callback_url
        )
Also, when "phone_number_country" is not used a validation error is returned.
----------------
Logs: https://www.scalyr.com/events?filter=%27phone_number_country%27&teamToken=G6OgJJW2i5fjksxFW6bwDg--&startTime=1556108383775&endTime=1556110278512
Response:
plivo.exceptions.ValidationError: {u'error': u'phone_number_country field is mandatory.',
 u'message': u'Could not complete address verification.',
 u'status': u'error'}
This response is retunred by our servers.
----------------

Test1:
When contry code is "ES" the validation works and Validation error is
returned "plivo.exceptions.ValidationError: The parameter fiscal_identification_code is required for Spain numbers"
Test2:
When country code is 'DK' the validation fails.
Response:
TypeError: all() takes exactly one argument (2 given)
Test3:
Any different contry code:
The Request is accepted. But the address does not show up.
Response:
{u'api_id': u'd5fc05a6-6699-11e9-8d11-0242ac110003',
 u'message': u'Your request has been accepted.'}

I have changed the code in addresses.py. There are no errors now.
"""
