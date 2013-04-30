import unittest
import os
import random
import string
import time

import plivo

try:
    from auth_secrets import AUTH_ID, AUTH_TOKEN
    from auth_secrets import DEFAULT_FROM_NUMBER, DEFAULT_TO_NUMBER, DEFAULT_TO_NUMBER2
except ImportError:
    AUTH_ID, AUTH_TOKEN = os.getenv("AUTH_ID"), os.getenv("AUTH_TOKEN")
    DEFAULT_FROM_NUMBER = os.getenv("DEFAULT_FROM_NUMBER")
    DEFAULT_TO_NUMBER = os.getenv("DEFAULT_TO_NUMBER")
    DEFAULT_TO_NUMBER2 = os.getenv("DEFAULT_TO_NUMBER2")
    if not (AUTH_ID and AUTH_TOKEN and
            DEFAULT_FROM_NUMBER and DEFAULT_TO_NUMBER):
        raise Exception("Create a auth_secrets.py file or set AUTH_ID "
                        "AUTH_TOKEN, DEFAULT_TO_NUMBER, DEFAULT_FROM_NUMBER "
                        "as environ values.")


client = None
random_letter = lambda: random.choice(string.ascii_letters)
random_string = lambda len: ''.join(random_letter() for i in range(len))


class PlivoTest(unittest.TestCase):
    "Adds a plivo client in setup"
    def setUp(self):
        self.client = get_client(AUTH_ID, AUTH_TOKEN)
        self.some_timezones = ['Pacific/Apia', 'Pacific/Midway']

    def check_status_and_keys(self, status, valid_keys, response):
        self.assertEqual(status, response[0])
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)

    def check_keys(self, keys, obj):
        keys.append("status_code")
        for key in keys:
            self.assertTrue(hasattr(obj, key))


class TestAccountsRestApi(PlivoTest):
    def test_get_account(self):
        response = self.client.get_account()
        self.assertEqual(200, response[0])
        valid_keys = ["account_type", "address", "auth_id", "auto_recharge",
                      "cash_credits", "city", "created", "enabled"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)

    def test_modify_account_name(self):
        random_name = random_string(10)
        params = {'name': random_name}
        self.client.modify_account(params)

        response = self.client.get_account()
        self.assertEqual(random_name, response[1]['name'])

    def test_modify_account_city(self):
        random_city = random_string(10)
        params = {'city': random_city}
        self.client.modify_account(params)

        response = self.client.get_account()
        self.assertEqual(random_city, response[1]['city'])

    def test_modify_account_address(self):
        random_address = random_string(20)
        params = {'address': random_address}
        self.client.modify_account(params)

        response = self.client.get_account()
        self.assertEqual(random_address, response[1]['address'])

    def test_modify_account_restricted_params(self):
        res = self.client.get_account()[1]

        random_name = random_string(10)
        random_city = random_string(10)
        random_address = random_string(10)
        random_state = random_string(6)

        random_timezone = ''
        if res['timezone'] in self.some_timezones:
            index = self.some_timezones.index(res['timezone'])
            if index != 0:
                random_timezone = self.some_timezones[0]
            else:
                random_timezone = self.some_timezones[1]
        else:
            random_timezone = self.some_timezones[0]

        random_cashcredit = "".join(random.sample('97654', 4))
        while(1):
            if random_cashcredit != res['cash_credits']:
                break
            random_cashcredit = "".join(random.sample('97654', 4))

        params = {
            'name': random_name,
            'city': random_city,
            'address': random_address,
            'account_type': 'dasghfdsg',
            'auth_id': 'gadfgsfsdfdsgs',
            'auto_recharge': not(res['auto_recharge']),
            'cash_credits': random_cashcredit,
            'created': "1952-05-04",
            'enabled': not(res['enabled']),
            'resource_uri': '/akjslsjkls/dsfg',
            'state': random_state,
            'timezone': random_timezone,
        }
        self.client.modify_account(params)

        r = self.client.get_account()[1]

        #These params should be modified
        self.assertEqual(r['name'], params['name'])
        self.assertEqual(r['city'], params['city'])
        self.assertEqual(r['address'], params['address'])
        self.assertEqual(r['state'], params['state'])
        self.assertEqual(r['timezone'], params['timezone'])

        #These params should not be modified
        self.assertEqual(r['account_type'], res['account_type'])
        self.assertEqual(r['auth_id'], res['auth_id'])
        self.assertEqual(r['auto_recharge'], res['auto_recharge'])
        self.assertEqual(r['created'], res['created'])
        self.assertEqual(r['enabled'], res['enabled'])
        self.assertEqual(r['resource_uri'], res['resource_uri'])

        self.assertNotEqual(r['account_type'], params['account_type'])
        self.assertNotEqual(r['auth_id'], params['auth_id'])
        self.assertNotEqual(r['auto_recharge'], params['auto_recharge'])
        self.assertNotEqual(r['created'], params['created'])
        self.assertNotEqual(r['enabled'], params['enabled'])
        self.assertNotEqual(r['resource_uri'], params['resource_uri'])

    def test_get_subaccounts(self):
        response = self.client.get_subaccounts()
        valid_keys = ["meta", "api_id", "objects"]
        self.check_status_and_keys(200, valid_keys, response)

    def test_subaccount_crud(self):
        temp_name = random_string(10)
        response = self.client.create_subaccount(dict(name=temp_name,
                                                 enabled=True))
        self.assertEqual(201, response[0])
        valid_keys = ["auth_id", "api_id", "auth_token"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)
        auth_id = json_response["auth_id"]
        response = self.client.get_subaccount(dict(subauth_id=auth_id))
        self.assertEqual(200, response[0])

        self.client.modify_subaccount({'subauth_id': auth_id,
                                       'name': temp_name,
                                       'enabled': False})
        response = self.client.get_subaccount({'subauth_id': auth_id})[1]
        #check modified details
        self.assertEqual(response['enabled'], False)
        self.assertEqual(response['name'], temp_name)

        response = self.client.delete_subaccount(dict(subauth_id=auth_id))
        self.assertEqual(204, response[0])
        # Deleted sub account should not exist
        response = self.client.get_subaccount({'subauth_id': auth_id})[1]
        self.assertEqual(response['error'], 'not found')


class TestApplicationRestApi(PlivoTest):
    def test_get_applications(self):
        response = self.client.get_applications()
        valid_keys = ["objects", "api_id", "meta"]
        self.check_status_and_keys(200, valid_keys, response)

    def test_applications_crud(self):
        params = {'answer_url': 'http://localhost.com',
                  'app_name': 'testappname'}
        response = self.client.create_application(params)
        self.assertEqual(201, response[0])

        app_id = response[1]['app_id']
        response = self.client.get_application({'app_id': app_id})
        self.assertEqual(response[1]['app_name'], params['app_name'])
        self.assertEqual(200, response[0])

        new_params = {'app_name': 'some new test name', 'app_id': app_id}
        response = self.client.modify_application(new_params)
        self.assertEqual(202, response[0])

        #check whether app_name modified or not
        response = self.client.get_application({'app_id': app_id})
        self.assertEqual(response[1]['app_name'], new_params['app_name'])

        #delete application
        response = self.client.delete_application({'app_id': app_id})
        self.assertEqual(204, response[0])

        #deleted application should not be available
        response = self.client.get_application({'app_id': app_id})
        self.assertEqual(404, response[0])
        self.assertEqual('not found', response[1]['error'])


class TestCallRestApi(PlivoTest):
    def setUp(self):
        super(TestCall, self).setUp()
        self.call_params = {'from': DEFAULT_FROM_NUMBER,
                            'to': DEFAULT_TO_NUMBER,
                            'answer_url':
                            'https://guarded-island.herokuapp.com/conference/',
                            'time_limit': 80
                            }

    def test_get_all_calls(self):
        response = self.client.get_cdrs()
        valid_keys = ['api_id', 'meta', 'objects']
        self.check_status_and_keys(200, valid_keys, response)

    def test_get_live_calls(self):
        response = self.client.get_live_calls()
        valid_keys = ['calls', 'api_id']
        self.check_status_and_keys(200, valid_keys, response)

    def test_make_outbound_call(self):
        response = self.client.make_call(self.call_params)
        self.assertEqual(201, response[0])

    def test_get_cdr(self):
        response = self.client.get_cdrs()
        if len(response[1]['objects']) > 0:
            call_uuid = response[1]['objects'][0]['call_uuid']
            response = self.client.get_cdr({"call_uuid": call_uuid})
            valid_keys = ['call_duration', 'billed_duration', 'total_amount',
                          'parent_call_uuid', 'call_direction', 'to_number',
                          'total_rate', 'api_id', 'from_number', 'end_time',
                          'call_uuid', 'resource_uri']
            self.check_status_and_keys(200, valid_keys, response)

    def test_hangup_request(self):
        response = self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.hangup_request({'request_uuid':
                                               response[1]['request_uuid']})
        self.assertEqual(204, response[0])


class TestEndpointRestApi(PlivoTest):
    def test_get_endpoints(self):
        response = self.client.get_endpoints()
        valid_keys = ["objects", "api_id", "meta"]
        self.check_status_and_keys(200, valid_keys, response)

    def test_endpoint_crud(self):
        params = {'username': 'agdrasg',
                  'password': 'ahfdsgdf',
                  'alias': 'asasddas'}
        response = self.client.create_endpoint(params)
        self.assertEqual(201, response[0])

        endpoint_id = response[1]['endpoint_id']

        response = self.client.get_endpoint({'endpoint_id': endpoint_id})
        self.assertEqual(200, response[0])
        #check created endpoint details
        self.assertEqual(response[1]['alias'], params['alias'])

        #modify endpoint
        new_params = {'alias': 'new alias fasda', 'endpoint_id': endpoint_id}
        response = self.client.modify_endpoint(new_params)
        self.assertEqual(202, response[0])

        #check modified details
        response = self.client.get_endpoint({'endpoint_id': endpoint_id})
        self.assertEqual(response[1]['alias'], new_params['alias'])

        #delete endpoint
        response = self.client.delete_endpoint({'endpoint_id': endpoint_id})
        self.assertEqual(204, response[0])

        #deleted endpoint should not be available
        response = self.client.get_endpoint({'endpoint_id': endpoint_id})
        self.assertEqual(404, response[0])
        self.assertEqual(response[1]['error'], 'not found')


class TestPricingRestApi(PlivoTest):
    def test_pricing(self):
        response = self.client.pricing({'country_iso': 'US'})
        valid_keys = ["country", "api_id", 'country_code', 'country_iso',
                      'phone_numbers', 'voice', 'message']
        self.check_status_and_keys(200, valid_keys, response)

    def test_invalid_country(self):
        response = self.client.pricing({'country_iso': 'USSDGF'})
        self.assertTrue("error" in response[1])


class TestRecordingRestApi(PlivoTest):
    def test_get_all_recordings(self):
        response = self.client.get_recordings()
        valid_keys = ['meta', 'objects', 'api_id']
        self.check_status_and_keys(200, valid_keys, response)

    def test_get_recording(self):
        response = self.client.get_recordings()
        if(len(response[1]['objects'])) > 0:
            recording_id = response[1]['objects'][0]['recording_id']
            response = self.client.get_recording({'recording_id':
                                                  recording_id})
            valid_keys = ['recording_id', 'api_id', 'conference_name',
                          'recording_type', 'recording_format', 'call_uuid',
                          'recording_url', 'resource_uri', 'add_time']
            self.check_status_and_keys(200, valid_keys, response)



class TestNumberRestApi(PlivoTest):
    def test_get_numbers(self):
        response = self.client.get_numbers()
        valid_keys = ['meta', 'objects', 'api_id']
        self.check_status_and_keys(200, valid_keys, response)

    def test_get_number(self):
        response = self.client.get_number({"number": DEFAULT_FROM_NUMBER})
        valid_keys = ["added_on", "api_id", "application", "carrier", "number",
                      "sms_enabled", "voice_enabled"]
        self.check_status_and_keys(200, valid_keys, response)
        self.assertEqual(DEFAULT_FROM_NUMBER, response[1]["number"])

    def test_number_crud(self):
        response = self.client.get_number_group({"country_iso": "US"})
        valid_keys = ["meta", "api_id", "objects"]
        self.check_status_and_keys(200, valid_keys, response)
        group_id = response[1]["objects"][0]["group_id"]
        response = self.client.rent_from_number_group({"group_id": group_id})
        valid_keys = ["numbers", "status"]
        self.check_status_and_keys(201, valid_keys, response)
        number = response[1]["numbers"][0]["number"]
        response = self.client.unrent_number({"number": number})


class TestCarrierRestApi(PlivoTest):
    def setUp(self):
        super(TestCarrier, self).setUp()
        response = self.client.get_incoming_carriers()
        carriers = response[1]
        for carrier in carriers['objects']:
            self.client.delete_incoming_carrier({
                'carrier_id': carrier['carrier_id']
            })

    def test_incoming_carriers(self):
        response = self.client.get_incoming_carriers()
        valid_keys = ['meta', 'objects', 'api_id']
        self.check_status_and_keys(200, valid_keys, response)

    def test_incoming_carrier_crud(self):
        random_name = random_string(10)
        params = {'name': random_name, 'ip_set': '192.168.1.144'}

        #create incoming carrier
        response = self.client.create_incoming_carrier(params)
        self.assertEqual(201, response[0])
        carrier_id = response[1]['carrier_id']

        #get created carrier and check its details
        response = self.client.get_incoming_carrier({'carrier_id': carrier_id})
        self.assertEqual(200, response[0])
        self.assertEqual(response[1]['name'], params['name'])
        self.assertEqual(response[1]['ip_set'], params['ip_set'])

        #modify carrier
        new_params = {'name': 'hdsfgdsfg', 'ip_set': '192.168.1.124',
                      'carrier_id': carrier_id}
        response = self.client.modify_incoming_carrier(new_params)
        self.assertEqual(202, response[0])

        #check modified carrier details
        response = self.client.get_incoming_carrier({'carrier_id': carrier_id})
        self.assertEqual(response[1]['name'], new_params['name'])
        self.assertEqual(response[1]['ip_set'], new_params['ip_set'])

        #delete incoming carrier
        response = self.client.delete_incoming_carrier({'carrier_id':
                                                        carrier_id})
        self.assertEqual(204, response[0])

        #deleted carrier should not be available
        response = self.client.get_incoming_carrier({'carrier_id': carrier_id})
        self.assertEqual(404, response[0])
        self.assertTrue("error" in response[1])


class TestConferenceRestApi(PlivoTest):
    def setUp(self):
        super(TestConference, self).setUp()
        self.call_params = {'from': DEFAULT_FROM_NUMBER,
                            'to': DEFAULT_TO_NUMBER,
                            'answer_url':
                            'https://guarded-island.herokuapp.com/conference/',
                            'time_limit': 80
                            }
        self.sound_url = \
            "https://guarded-island.herokuapp.com/static/client_on_hold_music.mp3"

    def test_get_all_conferences(self):
        response = self.client.get_live_conferences()
        valid_keys = ['conferences', 'api_id']
        self.check_status_and_keys(200, valid_keys, response)

    def test_conference_crud(self):
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        valid_keys = ['conference_name', 'conference_run_time',
                      'conference_member_count', 'members', 'api_id']
        self.check_status_and_keys(200, valid_keys, response)

        response = self.client.hangup_conference({'conference_name': 'plivo'})
        self.assertEqual(204, response[0])

        response = self.client.hangup_all_conferences()
        self.assertEqual(204, response[0])

    def test_members_hangup_member(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        #2 members in conference
        self.assertEqual(2, len(response[1]['members']))
        member_id = response[1]['members'][0]['member_id']
        another_member_id = response[1]['members'][1]['member_id']
        response = self.client.hangup_member({'member_id': member_id,
                                              'conference_name': 'plivo'})
        self.assertEqual(204, response[0])
        #Not working as of now, should be uncommeted once fixed
        #self.assertEqual(response[1]['message'], "hangup")
        #self.assertEqual(member_id, response[1]['member_id'])
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        #1 member in conference as one member is made to hangup
        self.assertEqual(1, len(response[1]['members']))
        self.assertEqual(another_member_id,
                         response[1]['members'][0]['member_id'])

    def test_members_kick_member_member_id(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        #2 members in conference
        self.assertEqual(2, len(response[1]['members']))
        member_id = response[1]['members'][0]['member_id']
        another_member_id = response[1]['members'][1]['member_id']
        response = self.client.kick_member({'member_id': member_id,
                                            'conference_name': 'plivo'})
        self.assertEqual(202, response[0])
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        #1 member in conference as one member is kicked
        self.assertEqual(1, len(response[1]['members']))
        self.assertEqual(another_member_id,
                         response[1]['members'][0]['member_id'])

    def test_members_kick_member_comma_separated_member_ids(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        #2 members in conference
        self.assertEqual(2, len(response[1]['members']))
        member_id = response[1]['members'][0]['member_id']
        another_member_id = response[1]['members'][1]['member_id']
        members_to_be_kicked = "%s, %s" % (member_id, another_member_id)
        response = self.client.kick_member({'member_id': members_to_be_kicked,
                                            'conference_name': 'plivo'})
        self.assertEqual(202, response[0])
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        valid_keys = ['api_id', 'error']
        #Returns 404 since no more members in the conference
        #(hence no conference)
        self.check_status_and_keys(404, valid_keys, response)

    def test_members_kick_member_all(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        #2 members in conference
        self.assertEqual(2, len(response[1]['members']))
        response = self.client.kick_member({'member_id': 'all',
                                            'conference_name': 'plivo'})
        self.assertEqual(202, response[0])
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        valid_keys = ['api_id', 'error']
        #Returns 404 since all are kicked from the conference
        #(hence no conference)
        self.check_status_and_keys(404, valid_keys, response)

    def test_members_mute_unmute(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']

        #mute member1
        response = self.client.mute_member({'conference_name': 'plivo',
                                            'member_id': member1})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 should be muted, member2 not
        self.assertTrue(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

        #unmute member1
        response = self.client.unmute_member({'conference_name': 'plivo',
                                              'member_id': member1})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should not be muted
        self.assertFalse(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

        #mute member1 and member2 using comma separated params
        both_members = "%s, %s" % (member1, member2)
        response = self.client.mute_member({'conference_name': 'plivo',
                                            'member_id': both_members})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should be muted
        self.assertTrue(response[1]['members'][0]['muted'])
        self.assertTrue(response[1]['members'][1]['muted'])

        #unmute member1 and member2
        response = self.client.unmute_member({'conference_name': 'plivo',
                                              'member_id': both_members})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should not be muted
        self.assertFalse(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

        #mute all members
        response = self.client.mute_member({'conference_name': 'plivo',
                                            'member_id': 'all'})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should be muted
        self.assertTrue(response[1]['members'][0]['muted'])
        self.assertTrue(response[1]['members'][1]['muted'])

        #unmute all members
        response = self.client.unmute_member({'conference_name': 'plivo',
                                              'member_id': 'all'})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should not be muted
        self.assertFalse(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

    def test_sound(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']
        #play to member1
        response = self.client.play_member({'conference_name': 'plivo',
                                            'member_id': member1,
                                            'url': self.sound_url})
        self.assertEqual(202, response[0])

        #stop play to member1
        response = self.client.stop_play_member({'conference_name': 'plivo',
                                                 'member_id': member1,
                                                 'url': self.sound_url})
        self.assertEqual(204, response[0])

        #play to both (via comma separated param)
        response = self.client.play_member({'conference_name': 'plivo',
                                            'member_id':
                                            "%s, %s" % (member1, member2),
                                            'url': self.sound_url})
        self.assertEqual(202, response[0])

        #stop play to both (via comma separated param)
        response = self.client.stop_play_member({'conference_name': 'plivo',
                                                 'member_id':
                                                 "%s, %s" % (member1, member2),
                                                 'url': self.sound_url})
        self.assertEqual(204, response[0])

        #play to all (via param 'all')
        response = self.client.play_member({'conference_name': 'plivo',
                                            'member_id': 'all',
                                            'url': self.sound_url})
        self.assertEqual(202, response[0])

        #stop play to all (via 'all' param)
        response = self.client.stop_play_member({'conference_name': 'plivo',
                                                 'member_id': 'all',
                                                 'url': self.sound_url})
        self.assertEqual(204, response[0])

    def test_deaf(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']

        #deaf member1
        response = self.client.deaf_member({'conference_name': 'plivo',
                                            'member_id': member1})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 should be deaf, member2 not
        self.assertTrue(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

        #undeaf member1
        response = self.client.undeaf_member({'conference_name': 'plivo',
                                              'member_id': member1})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should not be deaf
        self.assertFalse(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

        #deaf member1 and member2 using comma separated params
        both_members = "%s, %s" % (member1, member2)
        response = self.client.deaf_member({'conference_name': 'plivo',
                                            'member_id': both_members})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should be deaf
        self.assertTrue(response[1]['members'][0]['deaf'])
        self.assertTrue(response[1]['members'][1]['deaf'])

        #undeaf member1 and member2
        response = self.client.undeaf_member({'conference_name': 'plivo',
                                              'member_id': both_members})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should not be deaf
        self.assertFalse(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

        #deaf all members
        response = self.client.deaf_member({'conference_name': 'plivo',
                                            'member_id': 'all'})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should be deaf
        self.assertTrue(response[1]['members'][0]['deaf'])
        self.assertTrue(response[1]['members'][1]['deaf'])

        #undeaf all members
        response = self.client.undeaf_member({'conference_name': 'plivo',
                                              'member_id': 'all'})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                   'plivo'})
        #check: member1 and member2 should not be deaf
        self.assertFalse(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

    def test_speech(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                    'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']

        speak_params = {'conference_name': 'plivo',
                        'member_id': member1,
                        'text': 'Hello'
                        }

        #make member1 listen to speech
        response = self.client.speak_member(speak_params.copy())
        self.assertEqual(202, response[0])

        #make both member1 and member2 listen to speech
        speak_params['member_id'] = member2
        response = self.client.speak_member(speak_params.copy())
        self.assertEqual(202, response[0])

        #make all listen to speech
        speak_params['member_id'] = 'all'
        response = self.client.speak_member(speak_params.copy())
        self.assertEqual(202, response[0])

    def test_recording(self):
        #hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                       'plivo'})
        self.client.make_call(self.call_params)
        #wait some time
        time.sleep(8)

        #Record conference
        response = self.client.record_conference({'conference_name': 'plivo'})
        valid_keys = ['url', 'message', 'api_id']
        self.check_status_and_keys(202, valid_keys, response)

        #Stop recording conference
        response = self.client.stop_record_conference({'conference_name': 'plivo'})
        self.assertEqual(204, response[0])


class TestMessageRestApi(PlivoTest):
    def test_get_messages(self):
        response = self.client.get_messages()
        valid_keys = ['meta', 'objects', 'api_id']
        self.check_status_and_keys(200, valid_keys, response)

    def test_send_and_get_message(self):
        params = {"src": DEFAULT_FROM_NUMBER, "dst": DEFAULT_TO_NUMBER,
                  "text": "Testing"}
        response = self.client.send_message(params)
        valid_keys = ["message", "message_uuid", "api_id"]
        self.check_status_and_keys(202, valid_keys, response)
        message_uuid = response[1]["message_uuid"][0]
        self.client.get_message({"record_id": message_uuid})


class TestCall(PlivoTest):
    def setUp(self):
        super(TestCall, self).setUp()
        self.src = DEFAULT_FROM_NUMBER,
        self.to = DEFAULT_TO_NUMBER,
        self.answer_url = 'http://localhost'
        self.client.Call.send(src=self.src, to=self.to,
                              answer_url=self.answer_url)
        self.one_call_uuid = self.client.Call.get_all()[0].call_uuid

    def test_get_all(self):
        response = self.client.Call.get_all()
        self.assertEqual(200, response[0].status_code)
        self.assertEqual(type(response), list)
        self.assertEqual(type(response[0]), plivo.Call)

        valid_keys = [
            'call_duration', 'billed_duration', 'total_amount',
            'parent_call_uuid', 'call_direction', 'to_number',
            'total_rate', 'from_number', 'end_time', 'call_uuid',
            'resource_uri'
        ]
        self.check_keys(valid_keys, response[0])

    def test_get(self):
        response = self.client.Call.get(self.one_call_uuid)
        self.assertEqual(200, response.status_code)
        self.assertEqual(type(response), plivo.Call)

        valid_keys = [
            'call_duration', 'billed_duration', 'total_amount',
            'parent_call_uuid', 'call_direction', 'to_number',
            'total_rate', 'from_number', 'end_time', 'call_uuid',
            'resource_uri'
        ]
        self.check_keys(valid_keys, response)

    def test_send(self):
        response = self.client.Call.send(
            src=self.src, to=self.to, answer_url=self.answer_url
        )
        self.assertEqual(201, response.status_code)





def get_client(AUTH_ID, AUTH_TOKEN):
    return plivo.RestAPI(AUTH_ID, AUTH_TOKEN)

if __name__ == "__main__":
    unittest.main()
