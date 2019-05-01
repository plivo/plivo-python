import plivo;

client = plivo.RestClient('MAYMI3MZA5MZAWNJUXMD','YWU1MzJiMjBiZjBiMDQ4OTcyZDQ4YzBlZWEyZjgx')
"""
Create subaccount:
response = client.subaccounts.create(
    name='Wayne Enterprises Subaccount',
    enabled=True, )
print(response)
--------------
Response:
{'_name': 'Subaccount',
 u'api_id': u'f1fe3490-6685-11e9-8d11-0242ac110003',
 u'auth_id': u'SAMJCXY2QZNZHHZTLHZW',
 u'auth_token': u'MTUzNGYzOTYwYjZmNzZkMDExMzhjZWZiYjA5ZWE1',
 'client': <plivo.rest.client.Client object at 0x106bac650>,
 u'message': u'created'}

obvervation: Subaccount was created.
"""

"""
Update Subaccount:
response = client.subaccounts.update(
    auth_id='SAMJCXY2QZNZHHZTLHZW',
    name='Updated Subaccount Name', )
print(response)

---------------
Response:
{u'api_id': u'a88d0892-6688-11e9-b12a-0242ac110005', u'message': u'changed'}
obvervation: Details were updated.
"""

"""
Delete Subaccount:
response = client.subaccounts.delete(
    auth_id='SAMJCXY2QZNZHHZTLHZW',
    cascade=True )
print(response)
----------------
Response:
None
obvervation: We should check why the response was empty.But the subaccount and the Phone number associated with the subaccount was deleted.
"""
"""
Update account details:
response = client.account.update(
    name='Lucius Fox',
    city='New York',
    address='Times Square', )
print(response)
----------------
Response:
{u'api_id': u'9b5ab36c-6689-11e9-8d11-0242ac110003', u'message': u'changed'}
obvervation: There was a delay in reflecting changes on console. 
"""

"""
Validation test successful
response = client.account.update(
    )
print(response)
-------
Response:
plivo.exceptions.ValidationError: One parameter of name, city and address is required
"""
