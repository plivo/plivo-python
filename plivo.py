import base64
import hmac
from hashlib import sha1

import requests

import plivoxml as XML


try:
    import json
except ImportError:
    import simplejson as json


PLIVO_VERSION = "v1"


class PlivoError(Exception):
    pass


def validate_signature(uri, post_params, signature, auth_token):
    for k, v in sorted(post_params.items()):
        uri += k + v
    return base64.encodestring(hmac.new(auth_token, uri, sha1).digest()).strip() == signature





class RestAPI(object):
    def __init__(self, auth_id, auth_token, url='https://api.plivo.com', version=PLIVO_VERSION):
        self.version = version
        self.url = url.rstrip('/') + '/' + self.version
        self.auth_id = auth_id
        self.auth_token = auth_token
        self._api = self.url + '/Account/%s' % self.auth_id
        self.headers = {'User-Agent':'PythonPlivo'}
        self.Call = Call(self)
        self.Number = Number(self)
        self.Account = Account(self)
        self.SubAccount = SubAccount(self)
        self.Application = Application(self)
        self.Carrier = Carrier(self)
        self.Message = Message(self)
        self.Pricing = Pricing(self)
        self.EndPoint = EndPoint(self)
        self.Recording = Recording(self)
        self.Conference = Conference(self)
        self.ConferenceMember = ConferenceMember(self)

    def _request(self, method, path, data={}):
        path = path.rstrip('/') + '/'
        if method == 'POST':
            headers = {'content-type': 'application/json'}
            headers.update(self.headers)
            r = requests.post(self._api + path, headers=headers,
                              auth=(self.auth_id, self.auth_token),
                              data=json.dumps(data))
        elif method == 'GET':
            r = requests.get(self._api + path, headers=self.headers,
                             auth=(self.auth_id, self.auth_token),
                             params=data)
        elif method == 'DELETE':
            r = requests.delete(self._api + path, headers=self.headers,
                                auth=(self.auth_id, self.auth_token),
                                params=data)
        elif method == 'PUT':
            headers = {'content-type': 'application/json'}
            headers.update(self.headers)
            r = requests.put(self._api + path, headers=headers,
                             auth=(self.auth_id, self.auth_token),
                             data=json.dumps(data))
        content = r.content
        if content:
            try:
                response = json.loads(content)
            except ValueError:
                response = content
        else:
            response = content
        return (r.status_code, response)

    @staticmethod
    def get_param(params, key):
        try:
            return params[key]
        except KeyError:
            raise PlivoError("missing mandatory parameter %s" % key)

    ## Accounts ##
    def get_account(self, params=None):
        if not params: params = {}
        return self._request('GET', '', data=params)

    def modify_account(self, params=None):
        if not params: params = {}
        return self._request('POST', '', data=params)

    def get_subaccounts(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Subaccount/', data=params)

    def create_subaccount(self, params=None):
        if not params: params = {}
        return self._request('POST', '/Subaccount/', data=params)

    def get_subaccount(self, params=None):
        if not params: params = {}
        subauth_id = params.pop("subauth_id")
        return self._request('GET', '/Subaccount/%s/' % subauth_id, data=params)

    def modify_subaccount(self, params=None):
        if not params: params = {}
        subauth_id = params.pop("subauth_id")
        return self._request('POST', '/Subaccount/%s/' % subauth_id, data=params)

    def delete_subaccount(self, params=None):
        if not params: params = {}
        subauth_id = params.pop("subauth_id")
        return self._request('DELETE', '/Subaccount/%s/' % subauth_id, data=params)

    ## Applications ##
    def get_applications(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Application/', data=params)

    def create_application(self, params=None):
        if not params: params = {}
        return self._request('POST', '/Application/', data=params)

    def get_application(self, params=None):
        if not params: params = {}
        app_id = params.pop("app_id")
        return self._request('GET', '/Application/%s/' % app_id, data=params)

    def modify_application(self, params=None):
        if not params: params = {}
        app_id = params.pop("app_id")
        return self._request('POST', '/Application/%s/' % app_id, data=params)

    def delete_application(self, params=None):
        if not params: params = {}
        app_id = params.pop("app_id")
        return self._request('DELETE', '/Application/%s/' % app_id, data=params)

    ## Numbers ##
    def get_numbers(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Number/', data=params)

    def search_numbers(self, params=None):
        raise PendingDeprecationWarning("This API is deprecated. Consider "
                                        "using get_number_group_details")
        if not params: params = {}
        return self._request('GET', '/AvailableNumber/', data=params)

    def search_phone_numbers(self, params=None):
        if not params: params = {}
        return self._request('GET', '/PhoneNumber/', data=params)

    def get_number(self, params=None):
        if not params: params = {}
        number = params.pop("number")
        return self._request('GET', '/Number/%s/' % number, data=params)

    def rent_number(self, params=None):
        raise PendingDeprecationWarning("This API is deprecated. Consider "
                                        "using rent_from_number_group")
        if not params: params = {}
        number = params.pop("number")
        return self._request('POST', '/AvailableNumber/%s/' % number, data=params)

    def buy_phone_number(self, params=None):
        if not params: params = {}
        number = params.pop("number")
        return self._request('POST', '/PhoneNumber/%s/' % number, data=params)

    def unrent_number(self, params=None):
        if not params: params = {}
        number = params.pop("number")
        return self._request('DELETE', '/Number/%s/' % number, data=params)

    def add_carrier_number(self, params=None):
        if not params: params = {}
        return self._request('POST', '/Number/', data=params)

    def modify_number(self, params=None):
        if not params: params = {}
        number = params.pop("number")
        return self._request('POST', '/Number/%s/' % number, data=params)

    def link_application_number(self, params=None):
        if not params: params = {}
        number = params.pop("number")
        return self._request('POST', '/Number/%s/' % number, data=params)

    def unlink_application_number(self, params=None):
        if not params: params = {}
        number = params.pop("number")
        params = {'app_id':''}
        return self._request('POST', '/Number/%s/' % number, data=params)

    def get_number_group(self, params=None):
        if not params: params = {}
        return self._request('GET', '/AvailableNumberGroup/', data=params)

    def get_number_group_details(self, params=None):
        if not params: params = {}
        group_id = params.pop('group_id')
        return self._request('GET', '/AvailableNumberGroup/%s/' % group_id, data=params)

    def rent_from_number_group(self, params=None):
        if not params: params = {}
        group_id = params.pop('group_id')
        return self._request('POST', '/AvailableNumberGroup/%s/' % group_id, data=params)

    ## Calls ##
    def get_cdrs(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Call/', data=params)

    def get_cdr(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('GET', '/Call/%s/' % call_uuid, data=params)

    def get_live_calls(self, params=None):
        if not params: params = {}
        params['status'] = 'live'
        return self._request('GET', '/Call/', data=params)

    def get_live_call(self, params=None):
        if not params: params={}
        params['status'] = 'live'
        call_uuid = params.pop('call_uuid')
        return self._request('GET', '/Call/%s/' % call_uuid, data=params)

    def make_call(self, params=None):
        if not params: params = {}
        return self._request('POST', '/Call/', data=params)

    def hangup_all_calls(self, params=None):
        if not params: params = {}
        return self._request('DELETE', '/Call/', data=params)

    def transfer_call(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/' % call_uuid, data=params)

    def hangup_call(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('DELETE', '/Call/%s/' % call_uuid, data=params)

    def record(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/Record/' % call_uuid, data=params)

    def stop_record(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('DELETE', '/Call/%s/Record/' % call_uuid, data=params)

    def play(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/Play/' % call_uuid, data=params)

    def stop_play(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('DELETE', '/Call/%s/Play/' % call_uuid, data=params)

    def speak(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/Speak/' % call_uuid, data=params)

    def stop_speak(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('DELETE', '/Call/%s/Speak/' % call_uuid, data=params)

    def send_digits(self, params=None):
        if not params: params = {}
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/DTMF/' % call_uuid, data=params)

    ## Calls requests ##
    def hangup_request(self, params=None):
        if not params: params = {}
        request_uuid = params.pop('request_uuid')
        return self._request('DELETE', '/Request/%s/' % request_uuid, data=params)

    ## Conferences ##
    def get_live_conferences(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Conference/', data=params)

    def hangup_all_conferences(self, params=None):
        if not params: params = {}
        return self._request('DELETE', '/Conference/', data=params)

    def get_live_conference(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        return self._request('GET', '/Conference/%s/' % conference_name, data=params)

    def hangup_conference(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        return self._request('DELETE', '/Conference/%s/' % conference_name, data=params)

    def hangup_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/' % (conference_name, member_id), data=params)

    def play_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Play/' % (conference_name, member_id), data=params)

    def stop_play_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/Play/' % (conference_name, member_id), data=params)

    def speak_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Speak/' % (conference_name, member_id), data=params)

    def deaf_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Deaf/' % (conference_name, member_id), data=params)

    def undeaf_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/Deaf/' % (conference_name, member_id), data=params)

    def mute_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Mute/' % (conference_name, member_id), data=params)

    def unmute_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/Mute/' % (conference_name, member_id), data=params)

    def kick_member(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Kick/' % (conference_name, member_id), data=params)

    def record_conference(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        return self._request('POST', '/Conference/%s/Record/' % conference_name, data=params)

    def stop_record_conference(self, params=None):
        if not params: params = {}
        conference_name = params.pop('conference_name')
        return self._request('DELETE', '/Conference/%s/Record/' % conference_name, data=params)

    ## Recordings ##
    def get_recordings(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Recording/', data=params)

    def get_recording(self, params=None):
        if not params: params = {}
        recording_id = params.pop('recording_id')
        return self._request('GET', '/Recording/%s/' % recording_id, data=params)

    def delete_recording(self, params=None):
        if not params: params = {}
        recording_id = params.pop('recording_id')
        return self._request('DELETE', '/Recording/%s/' % recording_id, data=params)

    ## Endpoints ##
    def get_endpoints(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Endpoint/', data=params)

    def create_endpoint(self, params=None):
        if not params: params = {}
        return self._request('POST', '/Endpoint/', data=params)

    def get_endpoint(self, params=None):
        if not params: params = {}
        endpoint_id = params.pop('endpoint_id')
        return self._request('GET', '/Endpoint/%s/' % endpoint_id, data=params)

    def modify_endpoint(self, params=None):
        if not params: params = {}
        endpoint_id = params.pop('endpoint_id')
        return self._request('POST', '/Endpoint/%s/' % endpoint_id, data=params)

    def delete_endpoint(self, params=None):
        if not params: params = {}
        endpoint_id = params.pop('endpoint_id')
        return self._request('DELETE', '/Endpoint/%s/' % endpoint_id, data=params)

    ## Incoming Carriers ##
    def get_incoming_carriers(self, params=None):
        if not params: params = {}
        return self._request('GET', '/IncomingCarrier/', data=params)

    def create_incoming_carrier(self, params=None):
        if not params: params = {}
        return self._request('POST', '/IncomingCarrier/', data=params)

    def get_incoming_carrier(self, params=None):
        if not params: params = {}
        carrier_id = params.pop('carrier_id')
        return self._request('GET', '/IncomingCarrier/%s/' % carrier_id, data=params)

    def modify_incoming_carrier(self, params=None):
        if not params: params = {}
        carrier_id = params.pop('carrier_id')
        return self._request('POST', '/IncomingCarrier/%s/' % carrier_id, data=params)

    def delete_incoming_carrier(self, params=None):
        if not params: params = {}
        carrier_id = params.pop('carrier_id')
        return self._request('DELETE', '/IncomingCarrier/%s/' % carrier_id, data=params)

    ## Outgoing Carriers ##
    def get_outgoing_carriers(self, params=None):
        if not params: params = {}
        return self._request('GET', '/OutgoingCarrier/', data=params)

    def create_outgoing_carrier(self, params=None):
        if not params: params = {}
        return self._request('POST', '/OutgoingCarrier/', data=params)

    def get_outgoing_carrier(self, params=None):
        if not params: params = {}
        carrier_id = params.pop('carrier_id')
        return self._request('GET', '/OutgoingCarrier/%s/' % carrier_id, data=params)

    def modify_outgoing_carrier(self, params=None):
        if not params: params = {}
        carrier_id = params.pop('carrier_id')
        return self._request('POST', '/OutgoingCarrier/%s/' % carrier_id, data=params)

    def delete_outgoing_carrier(self, params=None):
        if not params: params = {}
        carrier_id = params.pop('carrier_id')
        return self._request('DELETE', '/OutgoingCarrier/%s/' % carrier_id, data=params)

    ## Carrier Routings ##
    def get_outgoing_carrier_routings(self, params=None):
        if not params: params = {}
        return self._request('GET', '/OutgoingCarrierRouting/', data=params)

    def add_outgoing_carrier_routings(self, params=None):
        if not params: params = {}
        return self._request('POST', '/OutgoingCarrierRouting/', data=params)

    def get_outgoing_carrier_routing(self, params=None):
        if not params: params = {}
        routing_id = params.pop('routing_id')
        return self._request('GET', '/OutgoingCarrierRouting/%s/' % routing_id, data=params)

    def modify_outgoing_carrier_routing(self, params=None):
        if not params: params = {}
        routing_id = params.pop('routing_id')
        return self._request('POST', '/OutgoingCarrierRouting/%s/' % routing_id, data=params)

    def delete_outgoing_carrier_routing(self, params=None):
        if not params: params = {}
        routing_id = params.pop('routing_id')
        return self._request('DELETE', '/OutgoingCarrierRouting/%s/' % routing_id, data=params)

    ## Pricing ##
    def pricing(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Pricing/', data=params)

    ## Outgoing Carriers ##

    ## To be added here ##

    ## Message ##
    def send_message(self, params=None):
        if not params: params = {}
        return self._request('POST', '/Message/', data=params)

    def get_messages(self, params=None):
        if not params: params = {}
        return self._request('GET', '/Message/', data=params)

    def get_message(self, params=None):
        if not params: params = {}
        message_uuid = params.pop('message_uuid')
        return self._request('GET', '/Message/%s/' % message_uuid, data=params)


class PlivoResponse(object):
    def __init__(self, rest_api=None, response=None):
        "Create a response class from json and httpresponse"
        if response:
            self.status_code = response[0]
            self.json_data = response[1]
        if rest_api:
            self.rest_api = rest_api

    @classmethod
    def get_objects_from_response(cls, rest_api=None, response=None):
        objects = response[1]['objects']
        return_objects = []
        for obj in objects:
           response_tuple = (response[0], obj)
           return_objects.append(cls(response=response_tuple, rest_api=rest_api))
        return return_objects

    def __getattr__(self, k):
        if k in self.json_data:
            return self.json_data[k]
        else:
            raise AttributeError(k)

    def __repr__(self):
        return "Status: %s \nData: %s"%(self.status_code, self.json_data)


class Call(PlivoResponse):

    def send(self, src, to, answer_url, **optional_params):
        if not optional_params: optional_params = {}
        optional_params.update({
            'from': src,
            'to': to,
            'answer_url': answer_url,
        })
        return Call(response=self.rest_api.make_call(optional_params),
                    rest_api=self.rest_api)

    def get(self, call_uuid, status=None, **optional_params):
        if not optional_params: optional_params = {}
        if status == 'live':
            optional_params['status'] = 'live'
        optional_params['call_uuid'] = call_uuid
        return Call(response=self.rest_api.get_cdr(optional_params),
                    rest_api=self.rest_api)

    def get_all(self, status=None, **optional_params):
        if not optional_params: optional_params = {}
        if status == 'live':
            optional_params['status'] = 'live'
        return Call.get_objects_from_response(
            response=self.rest_api.get_cdrs(optional_params),
            rest_api=self.rest_api
        )



    def hang(self, call_uuid=None):
        if not call_uuid:
            call_uuid = self.call_uuid
        optional_params = {}
        if not call_uuid:
            call_uuid = self.call_uuid
        optional_params['call_uuid'] = call_uuid
        return Call(response=self.rest_api.hangup_call(optional_params),
                    rest_api=self.rest_api)

    def transfer(self, call_uuid, **optional_params):
        if not call_uuid:
            call_uuid = self.call_uuid
        if not optional_params: optional_params = {}
        optional_params['call_uuid'] = call_uuid
        return Call(response=self.rest_api.transfer_call(optional_params),
                    rest_api=self.rest_api)


class Number(PlivoResponse):

    def add(self, numbers, carrier, region, **optional_params):
        optional_params.update({
            'numbers': numbers,
            'carrier': carrier,
            'region': region
        })
        return Number(
            response=self.rest_api.add_carrier_number(optional_params),
            rest_api=self.rest_api,
        )

    def edit(self, number, **optional_params):
        optional_params.update({
            'number': number,
        })
        return Number(response=self.rest_api.modify_number(optional_params),
                      rest_api=self.rest_api)

    def get(self, number, **optional_params):
        ''' Get Details of a number '''
        if not optional_params: optional_params = {}
        optional_params['number'] = number
        return Number(response=self.rest_api.get_number(optional_params),
                      rest_api=self.rest_api)

    def get_all(self, **optional_params):
        ''' Get details of all numbers '''
        return Number.get_objects_from_response(
            response=self.rest_api.get_numbers(optional_params),
            rest_api=self.rest_api
        )

    def search(self, country_iso, **optional_params):
        ''' Search numbers '''
        optional_params['country_iso'] = country_iso
        return Number.get_objects_from_response(
            response=self.rest_api.get_number_group(optional_params),
            rest_api=self.rest_api
        )

    def rent(self, group_id, **optional_params):
        ''' Rent Number '''
        optional_params['group_id'] = group_id
        return Number(
            response=self.rest_api.rent_from_number_group(optional_params),
            rest_api=self.rest_api
        )


class Account(PlivoResponse):

    def get(self, **optional_params):
        return Account(response=self.rest_api.get_account(optional_params),
                       rest_api=self.rest_api)

    def modify(self, **optional_params):
        return Account(response=self.rest_api.modify_account(optional_params),
                       rest_api=self.rest_api)


class SubAccount(PlivoResponse):

    def create(self, name, enabled, **optional_params):
        optional_params['name'] = name
        optional_params['enabled'] = enabled
        return SubAccount(response=self.rest_api.create_subaccount(optional_params),
                       rest_api=self.rest_api)

    def get(self, subauth_id=None, **optional_params):
        if not subauth_id:
            subauth_id = self.auth_id
        optional_params['subauth_id'] = subauth_id
        return SubAccount(response=self.rest_api.get_subaccount(optional_params),
                       rest_api=self.rest_api)

    def get_all(self, **optional_params):
        return SubAccount.get_objects_from_response(
            response=self.rest_api.get_subaccounts(optional_params),
            rest_api=self.rest_api
        )

    def modify(self, enabled, subauth_id=None, **optional_params):
        if not subauth_id:
            subauth_id = self.auth_id
        optional_params['subauth_id'] = subauth_id
        optional_params['enabled'] = enabled
        return SubAccount(response=self.rest_api.modify_subaccount(optional_params),
                       rest_api=self.rest_api)

    def delete(self, subauth_id=None, **optional_params):
        if not subauth_id:
            subauth_id = self.auth_id
        optional_params['subauth_id'] = subauth_id
        return SubAccount(response=self.rest_api.delete_subaccount(optional_params),
                       rest_api=self.rest_api)


class Application(PlivoResponse):

    def create(self, app_name, answer_url, **optional_params):
        '''create an application'''
        optional_params.update({
            'app_name': app_name,
            'answer_url': answer_url,
        })
        return Application(response=self.rest_api.create_application(optional_params),
                           rest_api=self.rest_api)

    def get(self, app_id=None, **optional_params):
        ''' get details of an application'''
        if not app_id:
            app_id = self.app_id
        optional_params['app_id'] = app_id
        return Application(response=self.rest_api.get_application(optional_params),
                           rest_api=self.rest_api)

    def get_all(self, **optional_params):
        ''' get details of all applications '''
        return Application.get_objects_from_response(
            response=self.rest_api.get_applications(optional_params),
                rest_api=self.rest_api
            )

    def modify(self, app_id=None, **optional_params):
        ''' Modify an application '''
        if not app_id:
            app_id = self.app_id
        optional_params['app_id'] = app_id
        return Application(response=self.rest_api.modify_application(optional_params),
                           rest_api=self.rest_api)

    def delete(self, app_id=None, **optional_params):
        ''' Delete an application '''
        if not app_id:
            app_id = self.app_id
        optional_params['app_id'] = app_id
        return Application(response=self.rest_api.delete_application(optional_params),
                           rest_api=self.rest_api)


class Carrier(PlivoResponse):

    def create(self, name, ip_set, **optional_params):
        optional_params.update({
            'name': name,
            'ip_set': ip_set
        })
        return Carrier(response=self.rest_api.create_incoming_carrier(optional_params),
                       rest_api=self.rest_api)

    def get(self, carrier_id=None, **optional_params):
        if not carrier_id:
            carrier_id = self.carrier_id
        optional_params['carrier_id'] = carrier_id
        return Carrier(response=self.rest_api.get_incoming_carrier(optional_params),
                       rest_api=self.rest_api)

    def get_all(self, **optional_params):
        return Carrier.get_objects_from_response(
            response=self.rest_api.get_incoming_carriers(optional_params),
            rest_api=self.rest_api
        )

    def modify(self, carrier_id=None, **optional_params):
        if not carrier_id:
            carrier_id = self.carrier_id
        optional_params['carrier_id'] = carrier_id
        return Carrier(response=self.rest_api.modify_incoming_carrier(optional_params),
                       rest_api=self.rest_api)

    def delete(self, carrier_id=None, **optional_params):
        if not carrier_id:
            carrier_id = self.carrier_id
        optional_params['carrier_id'] = carrier_id
        return Carrier(response=self.rest_api.delete_incoming_carrier(optional_params),
                       rest_api=self.rest_api)


class Message(PlivoResponse):

    def send(self, src, dst, text, url, message_type="sms", method="POST", **optional_params):
        optional_params.update({
                'src': src,
                'dst': dst,
                'text': text,
                'type': message_type,
                'url': url,
                'method': method,
            })
        return Message(response=self.rest_api.send_message(optional_params),
                       rest_api=self.rest_api)

    def get(self, message_uuid=None, **optional_params):
        if not message_uuid:
            if type(self.message_uuid) == list:
                message_uuid = self.message_uuid[0]
            else:
                message_uuid = self.message_uuid

        optional_params['message_uuid'] = message_uuid
        return Message(response=self.rest_api.get_message(optional_params),
                       rest_api=self.rest_api)

    def get_all(self, **optional_params):
        return Message.get_objects_from_response(
            response=self.rest_api.get_messages(optional_params),
            rest_api=self.rest_api
        )


class Pricing(PlivoResponse):

    def get(self, country_iso, **optional_params):
        optional_params['country_iso'] = country_iso
        return Pricing(response=self.rest_api.pricing(optional_params),
                       rest_api=self.rest_api)


class EndPoint(PlivoResponse):

    def create(self, username, password, alias, **optional_params):
        optional_params.update({
            'username': username,
            'password': password,
            'alias': alias
        })
        return EndPoint(response=self.rest_api.create_endpoint(optional_params),
                        rest_api=self.rest_api)

    def get(self, endpoint_id=None, **optional_params):
        if not endpoint_id:
            endpoint_id = self.endpoint_id
        optional_params['endpoint_id'] = endpoint_id
        return EndPoint(response=self.rest_api.get_endpoint(optional_params),
                        rest_api=self.rest_api)

    def get_all(self, **optional_params):
        return EndPoint.get_objects_from_response(
            response=self.rest_api.get_endpoints(optional_params),
            rest_api=self.rest_api
        )

    def modify(self, endpoint_id=None, **optional_params):
        if not endpoint_id:
            endpoint_id = self.endpoint_id
        optional_params['endpoint_id'] = endpoint_id
        return EndPoint(response=self.rest_api.modify_account(optional_params),
                        rest_api=self.rest_api)

    def delete(self, endpoint_id=None, **optional_params):
        if not endpoint_id:
            endpoint_id = self.endpoint_id
        optional_params['endpoint_id'] = endpoint_id
        return EndPoint(response=self.rest_api.delete_endpoint(optional_params),
                        rest_api=self.rest_api)


class Recording(PlivoResponse):

    def get(self, recording_id, **optional_params):
        optional_params['recording_id'] = recording_id
        return Recording(response=self.rest_api.get_recording(optional_params),
                         rest_api=self.rest_api)

    def get_all(self, **optional_params):
        return Recording.get_objects_from_response(
            response=self.rest_api.get_recordings(optional_params),
            rest_api=self.rest_api
        )


class Conference(PlivoResponse):

    @classmethod
    def get_conference_objects_from_response(cls, rest_api=None, response=None):
        objects = response[1]['conferences']
        return_objects = []
        for conference_name in objects:
            response_tuple = (response[0],
                {'conference_name': conference_name}
            )
            return_objects.append(cls(response=response_tuple, rest_api=rest_api))
        return return_objects

    def create(self, src, to, answer_url, **optional_params):
        if not optional_params: optional_params = {}
        optional_params.update({
            'from': src,
            'to': to,
            'answer_url': answer_url,
        })
        return Conference(response=self.rest_api.make_call(optional_params),
                    rest_api=self.rest_api)

    def get_all(self, **optional_params):
        return Conference.get_conference_objects_from_response(
            response=self.rest_api.get_live_conferences(optional_params),
            rest_api=self.rest_api
        )

    def get(self, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params['conference_name'] = conference_name
        return Conference(
            response=self.rest_api.get_live_conference(optional_params),
            rest_api=self.rest_api
        )

    def hang_all(self, **optional_params):
        return Conference(
            response=self.rest_api.hangup_all_conferences(optional_params),
            rest_api=self.rest_api
        )

    def hang(self, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params['conference_name'] = conference_name
        return Conference(
            response=self.rest_api.hangup_conference(optional_params),
            rest_api=self.rest_api
        )

    def record(self, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
        })
        return Conference(
            response=self.rest_api.record_conference(optional_params),
            rest_api=self.rest_api
        )

    def stop_record(self, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
        })
        return Conference(
            response=self.rest_api.stop_record_conference(optional_params),
            rest_api=self.rest_api
        )


class ConferenceMember(PlivoResponse):

    def get(self, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params['conference_name'] = conference_name
        return ConferenceMember(
            response=self.rest_api.get_live_conference(optional_params),
            rest_api=self.rest_api
        )

    def create(self, src, to, answer_url, **optional_params):
        if not optional_params: optional_params = {}
        optional_params.update({
            'from': src,
            'to': to,
            'answer_url': answer_url,
        })
        return ConferenceMember(
            response=self.rest_api.make_call(optional_params),
            rest_api=self.rest_api
        )


    def hangup(self, member_id, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
        })
        return ConferenceMember(
            response=self.rest_api.hangup_member(optional_params),
            rest_api=self.rest_api
        )

    def kick(self, member_id, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
        })
        return ConferenceMember(
            response=self.rest_api.kick_member(optional_params),
            rest_api=self.rest_api
        )

    def mute(self, member_id, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
        })
        return ConferenceMember(
            response=self.rest_api.mute_member(optional_params),
            rest_api=self.rest_api
        )

    def unmute(self, member_id, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
        })
        return ConferenceMember(
            response=self.rest_api.unmute_member(optional_params),
            rest_api=self.rest_api
        )

    def deaf(self, member_id, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
        })
        return ConferenceMember(
            response=self.rest_api.deaf_member(optional_params),
            rest_api=self.rest_api
        )

    def undeaf(self, member_id, conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
        })
        return ConferenceMember(
            response=self.rest_api.undeaf_member(optional_params),
            rest_api=self.rest_api
        )

    def speak(self, call_uuid, text, member_id,
              conference_name=None, **optional_params):
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
            'call_uuid': call_uuid,
            'text': text,
        })
        return ConferenceMember(
            response=self.rest_api.speak_member(optional_params),
            rest_api=self.rest_api
        )

    def play(self, url, member_id, conference_name=None, **optional_params):
        ''' Start playing sound to member(s) '''
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
            'url': url,
        })
        return ConferenceMember(
            response=self.rest_api.play_member(optional_params),
            rest_api=self.rest_api
        )

    def stop_play(self, member_id, conference_name=None, **optional_params):
        ''' Stop stop_playing sound to member(s) '''
        if not conference_name:
            conference_name = self.conference_name
        optional_params.update({
            'conference_name': conference_name,
            'member_id': member_id,
        })
        return ConferenceMember(
            response=self.rest_api.stop_play_member(optional_params),
            rest_api=self.rest_api
        )
