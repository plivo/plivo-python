import unittest
import os
import random
import string
import time

import plivo

try:
    import urlparse
    from urllib import urlencode
except:
    # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

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
        while (1):
            if random_cashcredit != res['cash_credits']:
                break
            random_cashcredit = "".join(random.sample('97654', 4))

        params = {
            'name': random_name,
            'city': random_city,
            'address': random_address,
            'account_type': 'dasghfdsg',
            'auth_id': 'gadfgsfsdfdsgs',
            'auto_recharge': not (res['auto_recharge']),
            'cash_credits': random_cashcredit,
            'created': "1952-05-04",
            'enabled': not (res['enabled']),
            'resource_uri': '/akjslsjkls/dsfg',
            'state': random_state,
            'timezone': random_timezone,
        }
        self.client.modify_account(params)

        r = self.client.get_account()[1]

        # These params should be modified
        self.assertEqual(r['name'], params['name'])
        self.assertEqual(r['city'], params['city'])
        self.assertEqual(r['address'], params['address'])
        self.assertEqual(r['state'], params['state'])
        self.assertEqual(r['timezone'], params['timezone'])

        # These params should not be modified
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
        # check modified details
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
                  'app_name': random_string(20)}
        response = self.client.create_application(params)
        self.assertEqual(201, response[0])

        app_id = response[1]['app_id']
        response = self.client.get_application({'app_id': app_id})
        self.assertEqual(response[1]['app_name'], params['app_name'])
        self.assertEqual(200, response[0])

        new_params = {'app_name': 'some new test name', 'app_id': app_id}
        response = self.client.modify_application(new_params)
        self.assertEqual(202, response[0])

        # check whether app_name modified or not
        response = self.client.get_application({'app_id': app_id})
        self.assertEqual(response[1]['app_name'], new_params['app_name'])

        # delete application
        response = self.client.delete_application({'app_id': app_id})
        self.assertEqual(204, response[0])

        # deleted application should not be available
        response = self.client.get_application({'app_id': app_id})
        self.assertEqual(404, response[0])
        self.assertEqual('not found', response[1]['error'])


class TestCallRestApi(PlivoTest):
    def setUp(self):
        super(TestCallRestApi, self).setUp()
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
        # wait some time
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
        # check created endpoint details
        self.assertEqual(response[1]['alias'], params['alias'])

        # modify endpoint
        new_params = {'alias': 'new alias fasda', 'endpoint_id': endpoint_id}
        response = self.client.modify_endpoint(new_params)
        self.assertEqual(202, response[0])

        # check modified details
        response = self.client.get_endpoint({'endpoint_id': endpoint_id})
        self.assertEqual(response[1]['alias'], new_params['alias'])

        # delete endpoint
        response = self.client.delete_endpoint({'endpoint_id': endpoint_id})
        self.assertEqual(204, response[0])

        # deleted endpoint should not be available
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
        if (len(response[1]['objects'])) > 0:
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
        super(TestCarrierRestApi, self).setUp()
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

        # create incoming carrier
        response = self.client.create_incoming_carrier(params)
        self.assertEqual(201, response[0])
        carrier_id = response[1]['carrier_id']

        # get created carrier and check its details
        response = self.client.get_incoming_carrier({'carrier_id': carrier_id})
        self.assertEqual(200, response[0])
        self.assertEqual(response[1]['name'], params['name'])
        self.assertEqual(response[1]['ip_set'], params['ip_set'])

        # modify carrier
        new_params = {'name': 'hdsfgdsfg', 'ip_set': '192.168.1.124',
                      'carrier_id': carrier_id}
        response = self.client.modify_incoming_carrier(new_params)
        self.assertEqual(202, response[0])

        # check modified carrier details
        response = self.client.get_incoming_carrier({'carrier_id': carrier_id})
        self.assertEqual(response[1]['name'], new_params['name'])
        self.assertEqual(response[1]['ip_set'], new_params['ip_set'])

        # delete incoming carrier
        response = self.client.delete_incoming_carrier({'carrier_id':
                                                            carrier_id})
        self.assertEqual(204, response[0])

        # deleted carrier should not be available
        response = self.client.get_incoming_carrier({'carrier_id': carrier_id})
        self.assertEqual(404, response[0])
        self.assertTrue("error" in response[1])


class TestConferenceRestApi(PlivoTest):
    def setUp(self):
        super(TestConferenceRestApi, self).setUp()
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
        # wait some time
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
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # 2 members in conference
        self.assertEqual(2, len(response[1]['members']))
        member_id = response[1]['members'][0]['member_id']
        another_member_id = response[1]['members'][1]['member_id']
        response = self.client.hangup_member({'member_id': member_id,
                                              'conference_name': 'plivo'})
        self.assertEqual(204, response[0])
        # Not working as of now, should be uncommeted once fixed
        # self.assertEqual(response[1]['message'], "hangup")
        # self.assertEqual(member_id, response[1]['member_id'])
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # 1 member in conference as one member is made to hangup
        self.assertEqual(1, len(response[1]['members']))
        self.assertEqual(another_member_id,
                         response[1]['members'][0]['member_id'])

    def test_members_kick_member_member_id(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # 2 members in conference
        self.assertEqual(2, len(response[1]['members']))
        member_id = response[1]['members'][0]['member_id']
        another_member_id = response[1]['members'][1]['member_id']
        response = self.client.kick_member({'member_id': member_id,
                                            'conference_name': 'plivo'})
        self.assertEqual(202, response[0])
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # 1 member in conference as one member is kicked
        self.assertEqual(1, len(response[1]['members']))
        self.assertEqual(another_member_id,
                         response[1]['members'][0]['member_id'])

    def test_members_kick_member_comma_separated_member_ids(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # 2 members in conference
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
        # Returns 404 since no more members in the conference
        # (hence no conference)
        self.check_status_and_keys(404, valid_keys, response)

    def test_members_kick_member_all(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # 2 members in conference
        self.assertEqual(2, len(response[1]['members']))
        response = self.client.kick_member({'member_id': 'all',
                                            'conference_name': 'plivo'})
        self.assertEqual(202, response[0])
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        valid_keys = ['api_id', 'error']
        # Returns 404 since all are kicked from the conference
        # (hence no conference)
        self.check_status_and_keys(404, valid_keys, response)

    def test_members_mute_unmute(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']

        # mute member1
        response = self.client.mute_member({'conference_name': 'plivo',
                                            'member_id': member1})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 should be muted, member2 not
        self.assertTrue(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

        # unmute member1
        response = self.client.unmute_member({'conference_name': 'plivo',
                                              'member_id': member1})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should not be muted
        self.assertFalse(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

        # mute member1 and member2 using comma separated params
        both_members = "%s, %s" % (member1, member2)
        response = self.client.mute_member({'conference_name': 'plivo',
                                            'member_id': both_members})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should be muted
        self.assertTrue(response[1]['members'][0]['muted'])
        self.assertTrue(response[1]['members'][1]['muted'])

        # unmute member1 and member2
        response = self.client.unmute_member({'conference_name': 'plivo',
                                              'member_id': both_members})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should not be muted
        self.assertFalse(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

        # mute all members
        response = self.client.mute_member({'conference_name': 'plivo',
                                            'member_id': 'all'})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should be muted
        self.assertTrue(response[1]['members'][0]['muted'])
        self.assertTrue(response[1]['members'][1]['muted'])

        # unmute all members
        response = self.client.unmute_member({'conference_name': 'plivo',
                                              'member_id': 'all'})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should not be muted
        self.assertFalse(response[1]['members'][0]['muted'])
        self.assertFalse(response[1]['members'][1]['muted'])

    def test_sound(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']
        # play to member1
        response = self.client.play_member({'conference_name': 'plivo',
                                            'member_id': member1,
                                            'url': self.sound_url})
        self.assertEqual(202, response[0])

        # stop play to member1
        response = self.client.stop_play_member({'conference_name': 'plivo',
                                                 'member_id': member1,
                                                 'url': self.sound_url})
        self.assertEqual(204, response[0])

        # play to both (via comma separated param)
        response = self.client.play_member({'conference_name': 'plivo',
                                            'member_id':
                                                "%s, %s" % (member1, member2),
                                            'url': self.sound_url})
        self.assertEqual(202, response[0])

        # stop play to both (via comma separated param)
        response = self.client.stop_play_member({'conference_name': 'plivo',
                                                 'member_id':
                                                     "%s, %s" % (member1, member2),
                                                 'url': self.sound_url})
        self.assertEqual(204, response[0])

        # play to all (via param 'all')
        response = self.client.play_member({'conference_name': 'plivo',
                                            'member_id': 'all',
                                            'url': self.sound_url})
        self.assertEqual(202, response[0])

        # stop play to all (via 'all' param)
        response = self.client.stop_play_member({'conference_name': 'plivo',
                                                 'member_id': 'all',
                                                 'url': self.sound_url})
        self.assertEqual(204, response[0])

    def test_deaf(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']

        # deaf member1
        response = self.client.deaf_member({'conference_name': 'plivo',
                                            'member_id': member1})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 should be deaf, member2 not
        self.assertTrue(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

        # undeaf member1
        response = self.client.undeaf_member({'conference_name': 'plivo',
                                              'member_id': member1})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should not be deaf
        self.assertFalse(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

        # deaf member1 and member2 using comma separated params
        both_members = "%s, %s" % (member1, member2)
        response = self.client.deaf_member({'conference_name': 'plivo',
                                            'member_id': both_members})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should be deaf
        self.assertTrue(response[1]['members'][0]['deaf'])
        self.assertTrue(response[1]['members'][1]['deaf'])

        # undeaf member1 and member2
        response = self.client.undeaf_member({'conference_name': 'plivo',
                                              'member_id': both_members})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should not be deaf
        self.assertFalse(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

        # deaf all members
        response = self.client.deaf_member({'conference_name': 'plivo',
                                            'member_id': 'all'})
        self.assertEqual(202, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should be deaf
        self.assertTrue(response[1]['members'][0]['deaf'])
        self.assertTrue(response[1]['members'][1]['deaf'])

        # undeaf all members
        response = self.client.undeaf_member({'conference_name': 'plivo',
                                              'member_id': 'all'})
        self.assertEqual(204, response[0])

        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        # check: member1 and member2 should not be deaf
        self.assertFalse(response[1]['members'][0]['deaf'])
        self.assertFalse(response[1]['members'][1]['deaf'])

    def test_speech(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        self.call_params['to'] = DEFAULT_TO_NUMBER2
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)
        response = self.client.get_live_conference({'conference_name':
                                                        'plivo'})
        member1 = response[1]['members'][0]['member_id']
        member2 = response[1]['members'][1]['member_id']

        speak_params = {'conference_name': 'plivo',
                        'member_id': member1,
                        'text': 'Hello'
                        }

        # make member1 listen to speech
        response = self.client.speak_member(speak_params.copy())
        self.assertEqual(202, response[0])

        # make both member1 and member2 listen to speech
        speak_params['member_id'] = member2
        response = self.client.speak_member(speak_params.copy())
        self.assertEqual(202, response[0])

        # make all listen to speech
        speak_params['member_id'] = 'all'
        response = self.client.speak_member(speak_params.copy())
        self.assertEqual(202, response[0])

    def test_recording(self):
        # hangup conference at the beginning
        self.client.hangup_conference({'conference_name':
                                           'plivo'})
        self.client.make_call(self.call_params)
        # wait some time
        time.sleep(8)

        # Record conference
        response = self.client.record_conference({'conference_name': 'plivo'})
        valid_keys = ['url', 'message', 'api_id']
        self.check_status_and_keys(202, valid_keys, response)

        # Stop recording conference
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
        self.client.get_message({"message_uuid": message_uuid})


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


class TestNumber(PlivoTest):
    def setUp(self):
        super(TestNumber, self).setUp()
        self.search_response = self.client.Number.search('US')
        self.group_id = self.search_response[0].group_id

    def test_search(self):
        self.assertEqual(200, self.search_response[0].status_code)
        valid_keys = [
            'group_id', 'number_type', 'prefix', 'region', 'rental_rate',
            'resource_uri', 'setup_rate', 'sms_enabled', 'sms_rate', 'stock',
            'voice_enabled', 'voice_rate'
        ]

        self.check_keys(valid_keys, self.search_response[0])

    def test_all(self):
        # Rent
        response = self.client.Number.rent(self.group_id)
        self.assertEqual(201, response.status_code)
        valid_keys = ['numbers', 'status', 'api_id']
        self.check_keys(valid_keys, response)
        number = response.numbers[0]['number']

        # Get
        response = response.get(number)
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'voice_enabled', 'sms_enabled',
            'region', 'fax_enabled', 'carrier', 'sms_rate', 'sub_account',
            'number', 'api_id', 'application', 'number_type', 'added_on',
            'resource_uri'
        ]

        self.check_keys(valid_keys, response)

        # Edit
        response = response.edit(number)
        self.assertEqual(202, response.status_code)
        valid_keys = ['message', 'api_id']
        self.check_keys(valid_keys, response)

    def test_get_all(self):
        response = self.client.Number.get_all()
        self.assertEqual(200, response[0].status_code)
        valid_keys = [
            'voice_enabled', 'sms_enabled',
            'region', 'fax_enabled', 'carrier', 'sms_rate', 'sub_account',
            'number', 'application', 'number_type', 'added_on',
            'resource_uri'
        ]
        self.check_keys(valid_keys, response[0])


class TestAccount(PlivoTest):
    def test_get(self):
        response = self.client.Account.get()
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'account_type', 'address', 'auth_id', 'auto_recharge',
            'cash_credits', 'city', 'created', 'enabled', 'modified',
            'name', 'resource_uri', 'state', 'timezone'
        ]
        self.check_keys(valid_keys, response)

    def test_modify(self):
        response = self.client.Account.modify()
        self.assertEqual(202, response.status_code)
        valid_keys = [
            'message', 'api_id',
        ]
        self.check_keys(valid_keys, response)


class TestSubAccount(PlivoTest):
    def setUp(self):
        super(TestSubAccount, self).setUp()
        random_name = random_string(10)
        self.response = self.client.SubAccount.create(name=random_name,
                                                      enabled=True)

    def test_create(self):
        self.assertEqual(201, self.response.status_code)
        valid_keys = [
            'auth_token', 'message', 'api_id', 'auth_id'
        ]
        self.check_keys(valid_keys, self.response)

    def test_get_without_params(self):
        response = self.response.get()
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'account', 'name', 'created', 'auth_token',
            'enabled', 'modified', 'api_id', 'auth_id', 'resource_uri'
        ]
        self.check_keys(valid_keys, response)

    def test_get(self):
        response = self.client.SubAccount.get(
            subauth_id=self.response.auth_id
        )
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'account', 'name', 'created', 'auth_token',
            'enabled', 'modified', 'api_id', 'auth_id', 'resource_uri'
        ]
        self.check_keys(valid_keys, response)

    def test_get_all(self):
        response = self.client.SubAccount.get_all()
        self.assertEqual(200, response[0].status_code)
        valid_keys = [
            'account', 'name', 'created',
            'enabled', 'modified', 'auth_id', 'resource_uri'
        ]
        self.check_keys(valid_keys, response[0])

    def test_modify_without_params(self):
        response = self.response.modify(True)
        self.assertEqual(202, response.status_code)

    def test_modify(self):
        response = self.response.modify(
            enabled=True, subauth_id=self.response.auth_id
        )
        self.assertEqual(202, response.status_code)

    def test_delete_without_params(self):
        response = self.response.delete()
        self.assertEqual(204, response.status_code)

        response = self.response.get()
        self.assertEqual(404, response.status_code)

    def test_delete(self):
        response = self.response.delete(
            subauth_id=self.response.auth_id
        )
        self.assertEqual(204, response.status_code)

        response = self.response.get()
        self.assertEqual(404, response.status_code)


class TestApplication(PlivoTest):
    def setUp(self):
        super(TestApplication, self).setUp()
        app_name = random_string(10)
        answer_url = 'http://localhost.com'
        self.create_response = self.client.Application.create(
            app_name=app_name, answer_url=answer_url
        )

    def test_create(self):
        self.assertEqual(201, self.create_response.status_code)
        valid_keys = [
            'message', 'app_id', 'api_id'
        ]
        self.check_keys(valid_keys, self.create_response)

    def test_get_without_params(self):
        response = self.create_response.get()
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'fallback_method', 'default_app', 'app_name',
            'production_app', 'app_id', 'hangup_url', 'answer_url',
            'message_url', 'resource_uri', 'hangup_method', 'message_method',
            'fallback_answer_url', 'answer_method'
        ]
        self.check_keys(valid_keys, response)

    def test_get(self):
        response = self.client.Application.get(
            app_id=self.create_response.app_id
        )
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'fallback_method', 'default_app', 'app_name',
            'production_app', 'app_id', 'hangup_url', 'answer_url',
            'message_url', 'resource_uri', 'hangup_method', 'message_method',
            'fallback_answer_url', 'answer_method'
        ]
        self.check_keys(valid_keys, response)

    def test_get_all(self):
        response = self.client.Application.get_all()
        self.assertEqual(200, response[0].status_code)
        valid_keys = [
            'fallback_method', 'default_app', 'app_name',
            'production_app', 'app_id', 'hangup_url', 'answer_url',
            'message_url', 'resource_uri', 'hangup_method', 'message_method',
            'fallback_answer_url', 'answer_method', 'enabled', 'public_uri',
            'sip_uri', 'sub_account'
        ]
        self.check_keys(valid_keys, response[0])

    def test_modify_without_params(self):
        response = self.create_response.modify()
        self.assertEqual(202, response.status_code)

    def test_modify(self):
        response = self.create_response.modify(
            app_id=self.create_response.app_id
        )
        self.assertEqual(202, response.status_code)

    def test_delete_without_params(self):
        response = self.create_response.delete()
        self.assertEqual(204, response.status_code)

        response = self.create_response.get()
        self.assertEqual(404, response.status_code)

    def test_delete(self):
        response = self.create_response.delete(
            app_id=self.create_response.app_id
        )
        self.assertEqual(204, response.status_code)

        response = self.create_response.get()
        self.assertEqual(404, response.status_code)


class TestCarrier(PlivoTest):
    def setUp(self):
        super(TestCarrier, self).setUp()
        # Delete all carriers first
        carriers = self.client.Carrier.get_all()
        for carrier in carriers:
            carrier.delete()

        # Create a new one
        name = random_string(10)
        ip_set = '192.168.13.24'
        self.create_response = self.client.Carrier.create(
            name=name, ip_set=ip_set,
        )

    def test_create(self):
        self.assertEqual(201, self.create_response.status_code)
        valid_keys = [
            'message', 'carrier_id', 'api_id'
        ]
        self.check_keys(valid_keys, self.create_response)

    def test_get_without_params(self):
        response = self.create_response.get()
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'carrier_id', 'ip_set', 'name', 'resource_uri', 'sms', 'voice'
        ]
        self.check_keys(valid_keys, response)

    def test_get(self):
        response = self.client.Carrier.get(
            carrier_id=self.create_response.carrier_id
        )
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'carrier_id', 'ip_set', 'name', 'resource_uri', 'sms', 'voice'
        ]
        self.check_keys(valid_keys, response)

    def test_get_all(self):
        response = self.client.Carrier.get_all()
        self.assertEqual(200, response[0].status_code)
        valid_keys = [
            'carrier_id', 'ip_set', 'name', 'resource_uri', 'sms', 'voice'
        ]
        self.check_keys(valid_keys, response[0])

    def test_modify_without_params(self):
        response = self.create_response.modify()
        self.assertEqual(202, response.status_code)

    def test_modify(self):
        response = self.create_response.modify(
            carrier_id=self.create_response.carrier_id
        )
        self.assertEqual(202, response.status_code)

    def test_delete_without_params(self):
        response = self.create_response.delete()
        self.assertEqual(204, response.status_code)

        response = self.create_response.get()
        self.assertEqual(404, response.status_code)

    def test_delete(self):
        response = self.create_response.delete(
            carrier_id=self.create_response.carrier_id
        )
        self.assertEqual(204, response.status_code)

        response = self.create_response.get()
        self.assertEqual(404, response.status_code)


class TestMessage(PlivoTest):
    def setUp(self):
        super(TestMessage, self).setUp()
        self.send_response = self.client.Message.send(
            src=DEFAULT_FROM_NUMBER,
            dst=DEFAULT_TO_NUMBER,
            text=random_string(30),
            url='http://localhost.com',
        )

    def test_send(self):
        self.assertEqual(202, self.send_response.status_code)
        valid_keys = [
            'message', 'message_uuid', 'api_id'
        ]
        self.check_keys(valid_keys, self.send_response)

    def test_get(self):
        response = self.client.Message.get(
            message_uuid=self.send_response.message_uuid[0]
        )

        self.assertEqual(200, response.status_code)
        valid_keys = [
            'meta', 'api_id', 'objects'
        ]
        self.check_keys(valid_keys, response)

    def test_get_without_params(self):
        response = self.send_response.get()
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'meta', 'api_id', 'objects'
        ]
        self.check_keys(valid_keys, response)

    def test_get_all(self):
        response = self.client.Message.get_all()
        self.assertEqual(200, response[0].status_code)

        valid_keys = [
            'message_direction', 'to_number', 'message_state',
            'total_amount', 'total_rate', 'from_number', 'message_uuid',
            'message_time', 'resource_uri', 'message_type'
        ]
        self.check_keys(valid_keys, response[0])


class TestPricing(PlivoTest):
    def test_pricing(self):
        response = self.client.Pricing.get(country_iso='US')
        valid_keys = ["country", "api_id", 'country_code', 'country_iso',
                      'phone_numbers', 'voice', 'message']
        self.assertEqual(200, response.status_code)
        self.check_keys(valid_keys, response)

    def test_invalid_country(self):
        response = self.client.Pricing.get(country_iso='ajskfd')
        self.assertEqual(200, response.status_code)
        self.assertTrue(hasattr(response, "error"))


class TestEndPoint(PlivoTest):
    def setUp(self):
        super(TestEndPoint, self).setUp()
        # Create a new one
        username = random_string(10)
        password = username
        alias = "%shdf" % username
        self.create_response = self.client.EndPoint.create(
            username=username, password=password, alias=alias
        )

    def test_create(self):
        self.assertEqual(201, self.create_response.status_code)
        valid_keys = [
            'message', 'endpoint_id', 'api_id'
        ]
        self.check_keys(valid_keys, self.create_response)
        # Delete
        self.create_response.delete()

    def test_get_without_params(self):
        response = self.create_response.get()
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'endpoint_id', 'resource_uri', 'alias', 'password',
            'username', 'sip_uri'
        ]
        self.check_keys(valid_keys, response)
        # Delete
        self.create_response.delete()

    def test_get(self):
        response = self.client.EndPoint.get(
            endpoint_id=self.create_response.endpoint_id
        )
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'endpoint_id', 'resource_uri', 'alias', 'password',
            'username', 'sip_uri'
        ]
        self.check_keys(valid_keys, response)
        # Delete
        self.create_response.delete()

    def test_get_all(self):
        response = self.client.EndPoint.get_all()
        self.assertEqual(200, response[0].status_code)
        valid_keys = [
            'endpoint_id', 'resource_uri', 'alias', 'password',
            'username', 'sip_uri'
        ]
        self.check_keys(valid_keys, response[0])
        # Delete
        self.create_response.delete()

    def test_modify_without_params(self):
        response = self.create_response.modify()
        self.assertEqual(202, response.status_code)

        # Delete
        self.create_response.delete()

    def test_modify(self):
        response = self.create_response.modify(
            endpoint_id=self.create_response.endpoint_id
        )
        self.assertEqual(202, response.status_code)

        # Delete
        self.create_response.delete()

    def test_delete_without_params(self):
        response = self.create_response.delete()
        self.assertEqual(204, response.status_code)

        response = self.create_response.get()
        self.assertEqual(404, response.status_code)

    def test_delete(self):
        response = self.create_response.delete(
            endpoint_id=self.create_response.endpoint_id
        )
        self.assertEqual(204, response.status_code)

        response = self.create_response.get()
        self.assertEqual(404, response.status_code)


class TestRecording(PlivoTest):
    def setUp(self):
        super(TestRecording, self).setUp()
        self.all_response = self.client.Recording.get_all()
        if len(self.all_response) > 0:
            self.recording_id = self.all_response[0].recording_id

    def test_get_all(self):
        self.assertEqual(200, self.all_response[0].status_code)
        valid_keys = [
            'call_uuid', 'recording_id', 'recording_type', 'recording_format',
            'conference_name', 'recording_url', 'resource_uri', 'add_time'
        ]
        self.check_keys(valid_keys, self.all_response[0])

    def test_get(self):
        if not self.recording_id:
            return
        response = self.client.Recording.get(self.recording_id)
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'call_uuid', 'recording_id', 'recording_type', 'recording_format',
            'conference_name', 'recording_url', 'resource_uri', 'add_time'
        ]
        self.check_keys(valid_keys, response)

    def test_get_without_params(self):
        if not self.recording_id:
            return
        response = self.all_response[0].get(self.recording_id)
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'call_uuid', 'recording_id', 'recording_type', 'recording_format',
            'conference_name', 'recording_url', 'resource_uri', 'add_time'
        ]
        self.check_keys(valid_keys, response)


class TestConference(PlivoTest):
    def setUp(self):
        super(TestConference, self).setUp()
        # Create a new one
        self.src = DEFAULT_FROM_NUMBER
        self.to = DEFAULT_TO_NUMBER
        self.answer_url = 'https://guarded-island.herokuapp.com/conference/'
        self.create_response = self.client.Conference.create(
            src=self.src, to=self.to, answer_url=self.answer_url,
            time_limit=80
        )
        time.sleep(8)

        self.get_response = self.client.Conference.get(
            conference_name="plivo"
        )

    def test_create(self):
        self.assertEqual(201, self.create_response.status_code)

    def test_get_without_params(self):
        response = self.get_response.get()
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'conference_name', 'conference_run_time', 'members',
            'conference_member_count', 'api_id'
        ]
        self.check_keys(valid_keys, response)

    def test_get(self):
        response = self.client.Conference.get(
            conference_name=self.get_response.conference_name
        )
        self.assertEqual(200, response.status_code)
        valid_keys = [
            'conference_name', 'conference_run_time', 'members',
            'conference_member_count', 'api_id'
        ]
        self.check_keys(valid_keys, response)

    def test_get_all(self):
        response = self.client.Conference.get_all()
        self.assertEqual(200, response[0].status_code)
        valid_keys = [
            'conference_name',
        ]
        self.check_keys(valid_keys, response[0])

    def test_hang_without_params(self):
        response = self.get_response.hang()
        self.assertEqual(204, response.status_code)

    def test_hang(self):
        response = self.get_response.hang(
            conference_name=self.get_response.conference_name
        )
        self.assertEqual(204, response.status_code)

    def test_record_without_params(self):
        response = self.get_response.record()
        self.assertEqual(202, response.status_code)

    def test_record(self):
        response = self.get_response.record(
            conference_name=self.get_response.conference_name
        )
        self.assertEqual(202, response.status_code)

    def test_stop_record_without_params(self):
        response = self.get_response.stop_record()
        self.assertEqual(204, response.status_code)

    def test_stop_record(self):
        response = self.get_response.stop_record(
            conference_name=self.get_response.conference_name
        )
        self.assertEqual(204, response.status_code)


class TestConferenceMember(PlivoTest):
    def setUp(self):
        super(TestConferenceMember, self).setUp()
        # Create a new one
        self.src = DEFAULT_FROM_NUMBER
        self.to = DEFAULT_TO_NUMBER
        self.answer_url = 'https://guarded-island.herokuapp.com/conference/'
        self.create_response = self.client.ConferenceMember.create(
            src=self.src, to=self.to, answer_url=self.answer_url,
            time_limit=80
        )
        time.sleep(8)

        self.get_response = self.client.ConferenceMember.get(
            conference_name="plivo"
        )
        self.sound_url = \
            "https://guarded-island.herokuapp.com/static/client_on_hold_music.mp3"

    def test_hangup(self):
        response = self.client.ConferenceMember.hangup(
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(204, response.status_code)

    def test_hangup_without_params(self):
        response = self.get_response.hangup(
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(204, response.status_code)

    def test_kick(self):
        response = self.client.ConferenceMember.kick(
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(202, response.status_code)

    def test_kick_without_params(self):
        response = self.get_response.kick(
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(202, response.status_code)

    def test_mute(self):
        response = self.client.ConferenceMember.mute(
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(202, response.status_code)

    def test_mute_without_params(self):
        response = self.get_response.mute(
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(202, response.status_code)

    def test_unmute(self):
        response = self.client.ConferenceMember.unmute(
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(204, response.status_code)

    def test_unmute_without_params(self):
        response = self.get_response.unmute(
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(204, response.status_code)

    def test_deaf(self):
        response = self.client.ConferenceMember.deaf(
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(202, response.status_code)

    def test_deaf_without_params(self):
        response = self.get_response.deaf(
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(202, response.status_code)

    def test_undeaf(self):
        response = self.client.ConferenceMember.undeaf(
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(204, response.status_code)

    def test_undeaf_without_params(self):
        response = self.get_response.undeaf(
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(204, response.status_code)

    def test_speak(self):
        response = self.client.ConferenceMember.speak(
            self.get_response.members[0]['call_uuid'],
            'Hello',
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(202, response.status_code)

    def test_speak_without_params(self):
        response = self.get_response.speak(
            self.get_response.members[0]['call_uuid'],
            'Hello',
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(202, response.status_code)

    def test_play(self):
        response = self.client.ConferenceMember.play(
            self.sound_url,
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(202, response.status_code)

    def test_play_without_params(self):
        response = self.get_response.play(
            self.sound_url,
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(202, response.status_code)

    def test_stop_play(self):
        response = self.client.ConferenceMember.stop_play(
            member_id=self.get_response.members[0]['member_id'],
            conference_name="plivo"
        )
        self.assertEqual(204, response.status_code)

    def test_stop_play_without_params(self):
        response = self.get_response.stop_play(
            member_id=self.get_response.members[0]['member_id'],
        )
        self.assertEqual(204, response.status_code)


class TestXML(unittest.TestCase):
    def test_attributes(self):
        self.assertTrue(hasattr(plivo.XML, "Message"))
        self.assertTrue(hasattr(plivo.XML, "Response"))
        self.assertTrue(hasattr(plivo.XML, "Message"))

    def test_response(self):
        r = plivo.XML.Response()
        file_name = "https://s3.amazonaws.com/plivocloud/Trumpet.mp3"
        p = r.addPlay(file_name)
        r.addHangup()
        self.assertTrue(file_name in r.to_xml())
        self.assertTrue("<Hangup />" in r.to_xml())


class TestValidateRequestSignature(unittest.TestCase):
    def setUp(self):
        super(TestValidateRequestSignature, self).setUp()
        self.test_auth_token = 'MySuperCoolSekritAuthToken'

    def test_get_request(self):
        # Get request
        uri = 'http://requestb.in/1gzeupi1?Direction=inbound&From=Anonymous&CallerName=Anonymous&BillRate=0.0085&' \
              'To=14154830338&CallUUID=c490f944-013f-4baa-b0eb-af87113bc8f7&CallStatus=ringing&Event=StartApp'
        expected_signature = 'iIzksJrgZggVf4VK54n9HWPm8SU='
        is_valid = plivo.validate_request_signature(uri, expected_signature, self.test_auth_token, None)
        self.assertTrue(is_valid)

    def test_post_request(self):
        # normal post request
        uri = 'http://requestb.in/1gzeupi1'
        form_data = 'Direction=inbound&From=Anonymous&CallerName=Anonymous&BillRate=0.0085&To=14154830338&' \
                    'CallUUID=69ffdb0d-27b6-424e-8e85-e733ddbd9e6a&CallStatus=ringing&Event=StartApp'
        expected_signature = '8SYmxFaaIfQvvfdxjYJobpI57wg='
        params = dict(urlparse.parse_qsl(form_data, keep_blank_values=True))
        is_valid = plivo.validate_request_signature(uri, expected_signature, self.test_auth_token, params=params)
        self.assertTrue(is_valid)

    # with UTF-8 in query params.
    def test_unicode_query_params(self):
        uri = 'http://requestb.in/1gzeupi1?To=14154830338&From=14087289654&TotalRate=0&Units=1&' \
              'Text=Hello+%C3%BCml%C3%A6t&TotalAmount=0&Type=sms&MessageUUID=2d47019a-9c66-11e6-8c60-02daa5941325'
        expected_signature = 'p4r7pkCIbkExPJYZnT6Rahni5vA='
        is_valid = plivo.validate_request_signature(uri, expected_signature, self.test_auth_token, None)
        self.assertTrue(is_valid)

    # with empty POST params
    def test_empty_post_params(self):
        uri = 'http://requestb.in/1nlmo4p1'
        form_data = 'TotalCost=0.00000&Direction=inbound&BillDuration=0&From=Anonymous&CallerName=Anonymous&' \
            'HangupCause=USER_BUSY&BillRate=0.0085&To=14154830338&AnswerTime=&StartTime=2016-10-26+18%3A51%3A45&' \
            'Duration=0&CallUUID=260e1bb4-5c1c-4e31-9035-8381d7639e2e&EndTime=2016-10-26+18%3A51%3A45&CallStatus=busy&' \
            'Event=Hangup'
        params = dict(urlparse.parse_qsl(form_data, keep_blank_values=True))
        expected_signature = 'WhLBwG3YobWjhg7mf/RARVDgg+w='
        is_valid = plivo.validate_request_signature(uri, expected_signature,
                                                    'ODE1ZmJkNzI3MzIwMmNmMDBiMDFiNjkxMDhlMjZj', params)
        self.assertTrue(is_valid)


def get_client(AUTH_ID, AUTH_TOKEN):
    return plivo.RestAPI(AUTH_ID, AUTH_TOKEN)

if __name__ == "__main__":
    unittest.main()
