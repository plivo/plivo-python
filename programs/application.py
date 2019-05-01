import plivo

client = plivo.RestClient('MAYMI3MZA5MZAWNJUXMD','YWU1MzJiMjBiZjBiMDQ4OTcyZDQ4YzBlZWEyZjgx')

"""
response = client.applications.create(
    app_name='Test Application' ,)

-------------
Response:
{u'api_id': u'd25eb2d0-669a-11e9-b12a-0242ac110005',
 u'app_id': u'28049981997530414',
 u'message': u'created'}

Test1:
If the answer_url or app_name is missing
Below error is returned:
Traceback (most recent call last):
  File "application.py", line 7, in <module>
    app_name='Test Application' ,)
TypeError: create() takes at least 3 arguments (2 given)
"""
"""
response = client.applications.delete(
    app_id='31485478729817310', )
print(response)
Observation: No issues
"""
"""
response = client.applications.update(
    app_id='28949038654699014',
    answer_url='http://updated.answer.url', )
print(response)
--------------------
Test1: If the app is notfound error is retunred.
Response: plivo.exceptions.ResourceNotFoundError: not found
Test2: Updating app works.
Response:
{u'api_id': u'4ce95cf0-669e-11e9-8d11-0242ac110003', u'message': u'changed'}
"""
