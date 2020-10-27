# -*- coding: utf-8 -*-

import json
from plivo.base import (ListResponseObject)
from plivo.exceptions import ValidationError
from plivo.resources import MultiPartyCall, MultiPartyCallParticipant
from plivo.utils.signature_v3 import construct_get_url
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class MultiPartyCallsTest(PlivoResourceTestCase):

    def __assert_requests(self, expected_url, expected_method, expected_request_body=None, actual_response=None):
        self.maxDiff = None

        # Verifying the api hit
        self.assertEqual(expected_url, self.client.current_request.url)
        # Verifying the method used
        self.assertEqual(expected_method, self.client.current_request.method)
        if expected_request_body:
            # Verifying the request body sent
            self.assertDictEqual(expected_request_body, json.loads(self.client.current_request.body.decode('utf-8')))
        if actual_response:
            # Verifying the mock response
            self.assertResponseMatches(actual_response)

    def test_add_participant_validations(self):

        error_message = ''
        friendly_name = 'friendly_name'
        uuid = '1234-5678-9012-3456'
        try:
            self.client.multi_party_calls.add_participant(role='agent')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, 'specify either multi party call friendly name or uuid')

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', friendly_name=friendly_name, uuid=uuid)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, 'cannot specify both multi party call friendly name or uuid')

        try:
            self.client.multi_party_calls.add_participant(role='customer', uuid=uuid)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, 'specify either call_uuid or (from, to)')

        try:
            self.client.multi_party_calls.add_participant(role='customer', uuid=uuid, from_='123456', call_uuid=uuid)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, 'cannot specify call_uuid when (from, to) is provided')

        try:
            self.client.multi_party_calls.add_participant(role='agent', uuid=uuid, to_='123456')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, 'specify (from, to) when not adding an existing call_uuid '
                                        'to multi party participant')

        try:
            self.client.multi_party_calls.add_participant(role='manager')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"role should be in ('agent', 'supervisor', "
                                        "'customer') (actual value: manager)\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', friendly_name=1234)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"friendly_name should be of type: ['str']\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', uuid=1234)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"uuid should be of type: ['str']\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', call_status_callback_url='callback_python')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "['call_status_callback_url should match format "
                                        "(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|"
                                        "(?:%[0-9a-fA-F][0-9a-fA-F]))+|None) (actual value: callback_python)']")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', call_status_callback_method='HEAD')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"call_status_callback_method should be in "
                                        "('GET', 'POST') (actual value: HEAD)\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', confirm_key='K')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"confirm_key should be in ('0', '1', '2', '3', '4', '5', '6', '7', '8', "
                                        "'9', '#', '*') (actual value: K)\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', ring_timeout='2500')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"ring_timeout should be of type: ['int']\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', max_duration=29867)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "['300 < max_duration <= 28800 (actual value: 29867)']")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', status_callback_events='agent-transfer')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"status_callback_events should be among ('mpc-state-changes', "
                                        "'participant-state-changes', 'participant-speak-events', "
                                        "'participant-digit-input-events', 'add-participant-api-events'). multiple "
                                        "values should be COMMA(,) separated (actual value: agent-transfer)\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', stay_alone=1)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"stay_alone should be of type: ['bool']\"]")

        try:
            self.client.multi_party_calls.add_participant(role='supervisor', enter_sound='beep:3')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "enter_sound did not satisfy any of the required types")

    @with_response(200)
    def test_add_participant(self):

        request_body = {
            'exit_sound_method': 'GET',
            'exit_sound': 'beep:2',
            'enter_sound_method': 'GET',
            'enter_sound': 'beep:1',
            'relay_dtmf_inputs': False,
            'end_mpc_on_exit': False,
            'start_mpc_on_enter': True,
            'hold': False, 'mute': False,
            'coach_mode': True,
            'stay_alone': False,
            'status_callback_events': 'mpc-state-changes,participant-state-changes',
            'record_file_format': 'mp3',
            'record': False,
            'on_exit_action_method': 'POST',
            'status_callback_method': 'GET',
            'recording_callback_method': 'GET',
            'customer_hold_music_method': 'GET',
            'agent_hold_music_method': 'GET',
            'wait_music_method': 'GET',
            'max_participants': 10,
            'max_duration': 14400,
            'ring_timeout': 45,
            'dial_music': 'real',
            'confirm_key_sound_method': 'GET',
            'call_status_callback_method': 'POST',
            'call_uuid': '1234-5678-4321-0987',
            'role': 'agent'
        }

        add_participant_response = self.client.multi_party_calls.add_participant(friendly_name='Voice', role='agent',
                                                                                 call_uuid='1234-5678-4321-0987')

        self.__assert_requests(actual_response=add_participant_response, expected_method='POST',
                               expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/name_Voice/Participant/',
                               expected_request_body=request_body)

        # update the request body for next set of params
        request_body.pop('call_uuid', None)
        request_body['to'] = '180012341234'
        request_body['from'] = '918888888888'
        request_body['role'] = 'supervisor'
        request_body['coach_mode'] = False
        request_body['dial_music'] = 'http://music.plivo.com/bella-ciao.wav'
        request_body['status_callback_events'] = 'participant-speak-events'
        request_body['ring_timeout'] = 100
        request_body['max_duration'] = 25000
        request_body['max_participants'] = 5
        request_body['relay_dtmf_inputs'] = True
        request_body['customer_hold_music_url'] = 'http://music.plivo.com/bella-ciao.wav'
        request_body['customer_hold_music_method'] = 'POST'
        request_body['exit_sound_method'] = 'POST'
        request_body['record_file_format'] = 'wav'

        add_participant_response = self.client.multi_party_calls.add_participant(
            uuid='12345678-90123456', role='supervisor', to_='180012341234', from_='918888888888',
            coach_mode=False, dial_music='http://music.plivo.com/bella-ciao.wav', ring_timeout=100,
            status_callback_events='participant-speak-events', max_duration=25000, max_participants=5,
            relay_dtmf_inputs=True, customer_hold_music_url='http://music.plivo.com/bella-ciao.wav',
            customer_hold_music_method='post', exit_sound_method='Post', record_file_format='wav')

        self.__assert_requests(actual_response=add_participant_response, expected_method='POST',
                               expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/uuid_12345678-90123456/Participant/',
                               expected_request_body=request_body)

    @with_response(200)
    def test_start_MPC(self):

        request_body = {'status': 'active'}

        start_mpc_response = self.client.multi_party_calls.start(friendly_name='Voice')

        self.__assert_requests(actual_response=start_mpc_response, expected_method='POST',
                               expected_url='https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/name_Voice/',
                               expected_request_body=request_body)

        start_mpc_response = self.client.multi_party_calls.start(uuid='12345678-90123456')

        self.__assert_requests(actual_response=start_mpc_response, expected_method='POST',
                               expected_url='https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/uuid_12345678-90123456/',
                               expected_request_body=request_body)

    @with_response(200)
    def test_end_MPC(self):

        end_mpc_response = self.client.multi_party_calls.stop(friendly_name='Voice')

        self.__assert_requests(actual_response=end_mpc_response, expected_method='DELETE',
                               expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/name_Voice/')

        end_mpc_response = self.client.multi_party_calls.stop(uuid='12345678-90123456')

        self.__assert_requests(actual_response=end_mpc_response, expected_method='DELETE',
                               expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/uuid_12345678-90123456/')

    def test_list_mpc_validations(self):

        error_message = ''

        try:
            self.client.multi_party_calls.list(sub_account='Voice')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, 'sub_account did not satisfy any of the required types')

        try:
            self.client.multi_party_calls.list(status='terminating')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"status should be in ('active', 'initialized', 'ended') "
                                        "(actual value: terminating)\"]")

        try:
            self.client.multi_party_calls.list(termination_cause_code='2000')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "[\"termination_cause_code should be of type: ['int']\"]")

        try:
            self.client.multi_party_calls.list(end_time__lte='20-10-3 9:22')
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "['end_time__lte should match format ^\\\\d{4}-\\\\d{2}-\\\\d{2} \\\\d{2}:"
                                        "\\\\d{2}(:\\\\d{2}(\\\\.\\\\d{1,6})?)?$ (actual value: 20-10-3 9:22)']")

        try:
            self.client.multi_party_calls.list(limit=300)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "['0 < limit <= 20 (actual value: 300)']")

        try:
            self.client.multi_party_calls.list(offset=-1)
        except ValidationError as e:
            error_message = str(e)
        self.assertEqual(error_message, "['0 <= offset (actual value: -1)']")

    @with_response(200)
    def test_list_MPC(self):

        multi_party_calls = self.client.multi_party_calls.list()
        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/',
                               expected_method='GET')
        # check we received a list response
        self.assertIsInstance(multi_party_calls, ListResponseObject)
        # check if objects are case to MultiPartyCall
        self.assertIsInstance(multi_party_calls.objects[0], MultiPartyCall)
        self.assertIsInstance(multi_party_calls.objects[len(multi_party_calls.objects)-1], MultiPartyCall)
        # check if ID is correctly read in 5th random object
        self.assertEqual(multi_party_calls.objects[5].id, "9aad6d16-ed2c-4433-9313-26f8cfc4d99c")
        # check if friendly_name is correctly read in 18th random object
        self.assertEqual(multi_party_calls.objects[18].friendly_name, "Gasteiz / Vitoria")
        # check if termination_cause is correctly read in 13th random object
        self.assertEqual(multi_party_calls.objects[13].termination_cause, "Hangup API Triggered")
        # check if termination_cause_code is correctly read in 12th random object
        self.assertEqual(multi_party_calls.objects[12].termination_cause_code, 2000)
        # check if status is correctly read in 7th random object
        self.assertEqual(multi_party_calls.objects[7].status, "Active")
        # check if billed_amount is correctly read in 17th random object
        self.assertEqual(multi_party_calls.objects[17].billed_amount, 0.66)

        # check for case where filters are sent in request body and compare request body this time
        request_body = {
            'sub_account': 'SAWWWWWWWWWWWWWWWWWW',
            'friendly_name': 'axa',
            'status': 'active',
            'termination_cause_code': 1010,
            'end_time__gte': '2020-03-10 11:45',
            'start_time__lte': '2020-03-30 09:35',
            'limit': 15,
            'offset': 156
        }
        self.client.multi_party_calls.list(**request_body)

        # Construct sorted GET url for both cases
        expected_url = construct_get_url('https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/',
                                         params=request_body)
        actual_url = construct_get_url(self.client.current_request.url, params={})
        print(actual_url)
        self.assertEqual(expected_url, actual_url)
        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    def test_get_MPC(self):

        response = {
            'api_id': 'd0e000c6-9ace-11ea-97d8-1094bbeb5c2c',
            'friendly_name': 'Chamblee',
            'mpc_uuid': '9aad6d16-ed2c-4433-9313-26f8cfc4d99c',
            'participants': '/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/name_Chamblee/Participant/',
            'recording': 'not-recording',
            'resource_uri': '/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/name_Chamblee/',
            'start_time': '2020-05-18 22:02:51+05:30',
            'status': 'Active',
            'stay_alone': True
        }

        self.expected_response = response
        actual_response = self.client.set_expected_response(status_code=200, data_to_return=response)

        multi_party_call = self.client.multi_party_calls.get(friendly_name=response['friendly_name'])
        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/name_{}/'.format(response['friendly_name']),
                               expected_method='GET', actual_response=actual_response)
        # check we received a list response
        self.assertIsInstance(multi_party_call, MultiPartyCall)
        # check if ID is correctly read in object
        self.assertEqual(multi_party_call.id, response['mpc_uuid'])
        # check if friendly_name is correctly read in object
        self.assertEqual(multi_party_call.friendly_name, response['friendly_name'])
        # check if termination_cause is correctly read in 13th random object
        self.assertEqual(multi_party_call.recording, response['recording'])
        # check if billed_amount is correctly read in object
        self.assertEqual(multi_party_call.stay_alone, True)

    @with_response(200)
    def test_update_MPC_participant(self):

        participant_id = '10'
        uuid = '12345678-90123456'
        coach_mode = False
        mute = True

        update_response = self.client.multi_party_calls.update_participant(
            participant_id=participant_id,
            uuid=uuid,
            coach_mode=coach_mode,
            mute=mute
        )

        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/uuid_{}/Participant/{}/'.format(uuid, participant_id),
                               expected_method='POST', expected_request_body={'coach_mode': coach_mode, 'mute': mute},
                               actual_response=update_response)

    def test_kick_MPC_participant(self):
        self.client.set_expected_response(status_code=204, data_to_return=None)
        participant_id = 10
        uuid = '12345678-90123456'

        self.client.multi_party_calls.kick_participant(
            participant_id=participant_id,
            uuid=uuid
        )

        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/uuid_{}/Participant/{}/'.format(uuid, participant_id),
                               expected_method='DELETE')

    @with_response(200)
    def test_start_recording(self):

        file_format = 'wav'
        status_callback_url = 'https://plivo.com/status'
        start_recording_response = self.client.multi_party_calls.\
            start_recording(friendly_name='Voice', file_format=file_format, status_callback_url=status_callback_url)

        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/'
                                            'MultiPartyCall/name_{}/Record/'.format('Voice'),
                               expected_method='POST',
                               expected_request_body={'file_format': 'wav',
                                                      'status_callback_url': status_callback_url,
                                                      'status_callback_method': 'POST'},
                               actual_response=start_recording_response)

    def test_stop_recording(self):
        self.client.set_expected_response(status_code=204, data_to_return=None)
        self.client.multi_party_calls.stop_recording(friendly_name='Voice')
        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/'
                                            'name_{}/Record/'.format('Voice'), expected_method='DELETE')

    def test_pause_recording(self):
        self.client.set_expected_response(status_code=204, data_to_return=None)
        self.client.multi_party_calls.pause_recording(friendly_name='Voice')
        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/'
                                            'name_{}/Record/Pause/'.format('Voice'), expected_method='POST')

    def test_resume_recording(self):
        self.client.set_expected_response(status_code=204, data_to_return=None)
        self.client.multi_party_calls.resume_recording(friendly_name='Voice')
        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/'
                                            'name_{}/Record/Resume/'.format('Voice'), expected_method='POST')

    @with_response(200)
    def test_get_participant(self):

        participant_id = 49
        uuid = '18905d56-79c8-41d4-a840-25feff71070e'
        resp = self.client.multi_party_calls.get_participant(participant_id=participant_id, uuid=uuid)
        self.__assert_requests(expected_url='https://voice.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/MultiPartyCall/'
                                            'uuid_{}/Participant/{}/'.format(uuid, participant_id),
                               expected_method='GET')
        self.assertIsInstance(resp, MultiPartyCallParticipant)
        # Verify whether SecondaryResourceID has been set properly
        self.assertEqual(resp.secondary_id, str(participant_id))
        # Verify whether call_uuid has been set properly
        self.assertEqual(resp.call_uuid, '90de6710-9404-40d1-ba31-f26d2f7c533f')
        # Verify whether role has been set properly
        self.assertEqual(resp.role, 'customer')
        # Verify whether start_on_enter has been set properly
        self.assertEqual(resp.start_mpc_on_enter, True)
        # Verify whether duration has been set properly
        self.assertEqual(resp.duration, 30)
        # Verify whether billed_amount has been set properly
        self.assertEqual(resp.billed_amount, 0.005)
