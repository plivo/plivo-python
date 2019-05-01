import plivo

client = plivo.RestClient('MAYMI3MZA5MZAWNJUXMD','YWU1MzJiMjBiZjBiMDQ4OTcyZDQ4YzBlZWEyZjgx')

"""
response = client.numbers.search(country_iso='GB',
limit='2',offset='3')
print(response)


api_id: "9b5d1346-6747-11e9-b12a-0242ac110005"
api_id: "d23cf340-6747-11e9-8d11-0242ac110003"

"""
"""
response = client.numbers.search(country_iso='GB',
limit='0',offset='0')
print(response)

Test1: limit='0'
plivo.exceptions.ValidationError: ['0 < limit <= 20 (actual value: 0)']
Test2: offset='0'

"""
response = client.numbers.list(
    limit=5,
    offset=0,
    type='fixed', )
print(response)

"""
--------------
Response:
plivo.exceptions.ValidationError: ['0 <= offset (actual value: -1)']
"""
