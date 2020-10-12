# -*- coding: utf-8 -*-
from unittest import TestCase

from httmock import HTTMock, all_requests

from plivo import RestClient
from plivo.rest.phlo_client import PhloClient as PhloRestClient


@all_requests
def plivo_mock(url, request):
    return request


class PlivoTestClient(RestClient):
    def __init__(self,
                 auth_id=None,
                 auth_token=None,
                 proxies=None,
                 timeout=None):
        super(PlivoTestClient, self).__init__(auth_id, auth_token, proxies,
                                              timeout)
        self.set_expected_response(500, {})

    def set_expected_response(self, status_code, data_to_return):
        self.expected_response = {
            'status_code': status_code,
            'content': data_to_return
        }

    def mock_request(self, url, request):
        self.current_request = request
        return self.expected_response

    def send_request(self, req, **kwargs):
        with HTTMock(self.mock_request):
            return super(PlivoTestClient, self).send_request(req, **kwargs)


try:
    import urlparse
    from urllib import urlencode, unquote_plus, quote_plus
except ImportError:
    from urllib import parse as urlparse
    from urllib.parse import urlencode, unquote_plus, quote_plus


class PlivoResourceTestCase(TestCase):
    def setUp(self):
        self.client = PlivoTestClient(
            auth_id='MA' + 'X' * 18, auth_token='AbcdEfghIjklMnop1234')

    def assertUrlEqual(self, expected, actual, message=None):
        expected_url, actual_url = (urlparse.urlparse(x)._asdict()
                                    for x in (expected, actual))
        expected_qs, actual_qs = map(
            lambda x: sorted(urlparse.parse_qsl(x['query'])), (expected_url,
                                                               actual_url))
        expected_url['query'], actual_url['query'] = '', ''
        expected_url['path'], actual_url['path'] = map(
            unquote_plus, [expected_url['path'], actual_url['path']])

        self.assertEqual(expected_url, actual_url, message)
        self.assertEqual(expected_qs, actual_qs, message)

    def assertResponseMatches(self, obj, expected_response=None):
        expected_response = expected_response or self.expected_response
        id_str = getattr(obj, '_identifier_string', None)
        if id_str:
            self.assertEqual(expected_response[id_str], obj.id)

    def get_url(self, *args, **kwargs):
        return 'https://api.plivo.com/v1/Account/' + \
               self.client.session.auth[0] + \
               '/' + '/'.join([quote_plus(arg)
                               for arg in args]) + '/?' + urlencode(kwargs)

    def get_voice_url(self, *args, **kwargs):
        return 'https://voice.plivo.com/v1/Account/' + \
               self.client.session.auth[0] + \
               '/' + '/'.join([quote_plus(arg)
                               for arg in args]) + '/?' + urlencode(kwargs)

    def get_voice_fallback1_url(self, *args, **kwargs):
        return 'https://voice-usw1.plivo.com/v1/Account/' + \
               self.client.session.auth[0] + \
               '/' + '/'.join([quote_plus(arg)
                               for arg in args]) + '/?' + urlencode(kwargs)

    def get_voice_fallback2_url(self, *args, **kwargs):
        return 'https://voice-use1.plivo.com/v1/Account/' + \
               self.client.session.auth[0] + \
               '/' + '/'.join([quote_plus(arg)
                               for arg in args]) + '/?' + urlencode(kwargs)


class PlivoRequestTest(TestCase):
    def setUp(self):
        self.timeout = 1
        self.proxies = {
            'http': 'http://0.0.0.0:8888',
            'https': 'http://0.0.0.0:8080',
        }
        self.client = PlivoTestClient(
            auth_id='MA' + 'X' * 18,
            auth_token='AbcdEfghIjklMnol1234',
            proxies=self.proxies,
            timeout=self.timeout)

    def test_timeout_value(self):
        self.assertEqual(self.client.timeout, self.timeout)

    def test_proxy_value(self):
        self.assertEqual(self.client.proxies, self.proxies)


class PlivoPhlosTestClient(PhloRestClient):
    """
        Plivo Phlos rest client test case
    """
    def __init__(self,
                 auth_id=None,
                 auth_token=None,
                 proxies=None,
                 timeout=None):
        super(PlivoPhlosTestClient, self).__init__(auth_id, auth_token, proxies,
                                                   timeout)
        self.set_expected_response(500, {})

    def set_expected_response(self, status_code, data_to_return):
        self.expected_response = {
            'status_code': status_code,
            'content': data_to_return
        }

    def mock_request(self, url, request):
        self.current_request = request
        return self.expected_response

    def send_request(self, req, **kwargs):
        with HTTMock(self.mock_request):
            return super(PlivoPhlosTestClient, self).send_request(req, **kwargs)


class PlivoPhlosResourceTestCase(TestCase):
    def setUp(self):
        self.client = PlivoPhlosTestClient(
            auth_id='MA' + 'X' * 18, auth_token='AbcdEfghIjklMnol1234'
        )

    def assertUrlEqual(self, expected, actual, message=None):
        expected_url, actual_url = (urlparse.urlparse(x)._asdict()
                                    for x in (expected, actual))
        expected_qs, actual_qs = map(
            lambda x: sorted(urlparse.parse_qsl(x['query'])), (expected_url,
                                                               actual_url))
        expected_url['query'], actual_url['query'] = '', ''
        expected_url['path'], actual_url['path'] = map(
            unquote_plus, [expected_url['path'], actual_url['path']])

        self.assertEqual(expected_url, actual_url, message)
        self.assertEqual(expected_qs, actual_qs, message)

    def assertResponseMatches(self, obj, expected_response=None):
        expected_response = expected_response or self.expected_response
        id_str = getattr(obj, '_identifier_string', None)
        if id_str:
            self.assertEqual(expected_response[id_str], obj.id)

    def get_url(self, *args, **kwargs):
        return 'https://phlorunner.plivo.com/v1/account/' + \
               self.client.session.auth[0] + \
               '/' + '/'.join([quote_plus(arg)
                               for arg in args]) + '/?' + urlencode(kwargs)
