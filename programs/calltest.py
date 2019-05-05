import plivo
client = plivo.RestClient('MAYMI3MZA5MZAWNJUXMD','YWU1MzJiMjBiZjBiMDQ4OTcyZDQ4YzBlZWEyZjgx')

"""
response = client.calls.create(
    from_='918548854984',
    to_='919538183813<918548854984',
    answer_url='http://s3.amazonaws.com/static.plivo.com/answer.xml',
    answer_method='GET', )
print(response)
---------------
Response:
Traceback (most recent call last):
  File "calltest.py", line 7, in <module>
    answer_method='GET', )
  File "<decorator-gen-12>", line 2, in create
  File "build/bdist.macosx-10.14-intel/egg/plivo/utils/validators.py", line 170, in wrapper
  File "build/bdist.macosx-10.14-intel/egg/plivo/resources/calls.py", line 199, in create
plivo.exceptions.ValidationError: src and destination cannot overlap

"""
"""
All the agrguments are correct ,
"""
"""
Get CDR of a call:
response = client.calls.get(
    call_uuid='bdfe1272-6690-11e9-9b65-77979dc81b25', )
print(response)

Response:

{u'answer_time': u'2019-04-24 12:59:24+00:00',
 u'api_id': u'0f92aeb2-66ba-11e9-b6d9-0242ac110005',
 u'bill_duration': 3,
 u'billed_duration': 60,
 u'call_direction': u'inbound',
 u'call_duration': 3,
 u'call_state': u'ANSWER',
 u'call_uuid': u'bdfe1272-6690-11e9-9b65-77979dc81b25',
 u'end_time': u'2019-04-24 12:59:27+00:00',
 u'from_number': u'sip:Demo123180918183311@phone.plivo.com',
 u'hangup_cause_code': 4010,
 u'hangup_cause_name': u'End Of XML Instructions',
 u'hangup_source': u'Plivo',
 u'initiation_time': u'2019-04-24 12:59:06+00:00',
 u'parent_call_uuid': None,
 u'resource_uri': u'/v1/Account/MAYMI3MZA5MZAWNJUXMD/Call/bdfe1272-6690-11e9-9b65-77979dc81b25/',
 u'to_number': u'493022957150',
 u'total_amount': u'0.00300',
 u'total_rate': u'0.00300'}
"""
"""
response = client.calls.create(
    from_='918548854988',
    to_='918548854984',
    answer_url='http://s3.amazonaws.com/static.plivo.com/answer.xml',
    answer_method='GET',)
print(response)
-------------
Response:
{u'api_id': u'bef91198-66ba-11e9-a08c-0242ac110005',
 u'message': u'call fired',
 u'request_uuid': u'a585a2f3-0de1-4261-af53-aaa933d894f7'}

"""
"""
response = client.calls.record(
    call_uuid='3a2e4c90-dcee-4931-8a59-f123ab507e60', )
print(response)
"""

"""
response = client.calls.create(
    from_='918548854988',
    to_='918548854984',
    answer_url='http://s3.amazonaws.com/static.plivo.com/answer.xml',
    answer_method='GET',)
print(response)

-------------
Response:
plivo.exceptions.ValidationError: ['0 < hangup_on_ring (actual value: 0)']
"""
"""
As per doc:
"Valid values are aleg, bleg or both. aleg will
transfer call_uuid. bleg will transfer the bridged leg of call_uuid.
both will transfer both aleg and bleg."
"""
"""
response = client.calls.transfer(
    legs='aleg',
    aleg_url='//aleg.',
    call_uuid='84fa44f0-4d90-4518-9df1-d4e50b01fb71', )
print(response)
--------------
Response:
plivo.exceptions.ValidationError: ['aleg_url should match format
(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|None) (actual value: //aleg.)']
"""
"""
response = client.calls.play(
    call_uuid='bc480f62-6d99-469e-b80e-090e620de824',)
print(response)
--------------
Response:
TypeError: play() takes at least 3 arguments (2 given)
"""
"""
response = client.calls.record(
    call_uuid='3a2e4c90-dcee-4931-8a59-f123ab507e60',
    callback_url='uerigrf' )
print(response)


Test1: transcription_url is not a url
Response:
plivo.exceptions.ValidationError: ['transcription_url should match format
(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|None) (actual value: uerigrf)']

Test2: callback_url is not a url
Response:
plivo.exceptions.ValidationError: ['callback_url should match format
(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|None) (actual value: uerigrf)']
"""

response = client.calls.list(
    limit=5,
    offset=0, )
print(response)
