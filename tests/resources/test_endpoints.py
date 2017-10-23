# -*- coding: utf-8 -*-
from tests import PlivoResourceTestCase
from tests.decorators import with_response


class EndpointTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        self.client.endpoints.create(
            username='test', password='test', alias='test')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Endpoint'), self.client.current_request.url)

    @with_response(200)
    def test_list(self):
        endpoints = self.client.endpoints.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(endpoints)), 2)
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_url('Endpoint'), self.client.current_request.url)

    @with_response(200)
    def test_get(self):
        uuid = '4d04c52e-cea3-4458-bbdb-0bfc314ee7cd'
        endpoint = self.client.endpoints.get(uuid)
        self.assertResponseMatches(endpoint)
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_url('Endpoint', uuid), self.client.current_request.url)

    @with_response(202)
    def test_update(self):
        uuid = '4d04c52e-cea3-4458-bbdb-0bfc314ee7cd'
        self.client.endpoints.update(uuid, alias='test')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Endpoint', uuid), self.client.current_request.url)

    @with_response(204)
    def test_delete(self):
        uuid = '4d04c52e-cea3-4458-bbdb-0bfc314ee7cd'
        self.client.endpoints.delete(uuid)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Endpoint', uuid), self.client.current_request.url)
