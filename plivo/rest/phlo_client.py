# -*- coding: utf-8 -*-
"""
Phlo client, used for Phlo API requests.
"""
from plivo.resources import Phlos
from plivo.rest.base_client import BaseClient
from requests import Request

PHLO_API = 'https://phlorunner.plivo.com'
PHLO_API_BASE_URI = '/'.join([PHLO_API, 'v1'])


class PhloClient(BaseClient):
    def __init__(self, auth_id=None, auth_token=None, proxies=None, timeout=5):
        """
        The Plivo API client.

        Deals with all the API requests to be made.
        """
        BaseClient.__init__(self, auth_id, auth_token, proxies, timeout)

        self.phlo_base_uri = PHLO_API_BASE_URI
        self.phlo = Phlos(self)

    def create_request(self, method, path=None, data=None):
        path = path or []

        req = Request(method, '/'.join([self.phlo_base_uri] +
                                       list([str(p) for p in path])) + '/',
                      **({
                          'params': data
                      } if method == 'GET' else {
                          'json': data
                      }))
        return self.session.prepare_request(req)