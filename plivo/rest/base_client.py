# -*- coding: utf-8 -*-
"""
Base client, used for all API requests.
"""

import os
import platform
from collections import namedtuple

from plivo.base import ResponseObject
from plivo.exceptions import (AuthenticationError, InvalidRequestError,
                              PlivoRestError, PlivoServerError,
                              ResourceNotFoundError, ValidationError)
from plivo.utils import is_valid_mainaccount, is_valid_subaccount
from plivo.version import __version__
from requests import Request, Session

AuthenticationCredentials = namedtuple('AuthenticationCredentials',
                                       'auth_id auth_token')

PLIVO_API = 'https://api.plivo.com'
PLIVO_API_BASE_URI = '/'.join([PLIVO_API, 'v1/Account'])


def get_user_agent():
    return 'plivo-python/%s (Python: %s)' % (__version__,
                                             platform.python_version())


def fetch_credentials(auth_id, auth_token):
    """Fetches the right credentials either from params or from environment"""

    if not (auth_id and auth_token):
        try:
            auth_id = os.environ['PLIVO_AUTH_ID']
            auth_token = os.environ['PLIVO_AUTH_TOKEN']
        except KeyError:
            raise AuthenticationError('The Plivo Python SDK '
                                      'could not find your auth credentials.')

    if not (is_valid_mainaccount(auth_id) or is_valid_subaccount(auth_id)):
        raise AuthenticationError('Invalid auth_id supplied: %s' % auth_id)

    return AuthenticationCredentials(auth_id=auth_id, auth_token=auth_token)


class BaseClient(object):
    def __init__(self, auth_id=None, auth_token=None, proxies=None, timeout=5):
        """
        The Plivo API client.

        Deals with all the API requests to be made.
        """

        self.base_uri = PLIVO_API_BASE_URI
        self.session = Session()
        self.session.headers.update({
            'User-Agent': get_user_agent(),
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })
        self.session.auth = fetch_credentials(auth_id, auth_token)
        self.multipart_session = Session()
        self.multipart_session.headers.update({
            'User-Agent': get_user_agent(),
            'Cache-Control': 'no-cache',
            'Content-Type': 'multipart/form-data',
        })
        self.multipart_session.auth = fetch_credentials(auth_id, auth_token)
        self.proxies = proxies
        self.timeout = timeout

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.multipart_session.close()

    def process_response(self,
                         method,
                         response,
                         response_type=None,
                         objects_type=None):
        """Processes the API response based on the status codes and method used
        to access the API
        """

        try:
            response_json = response.json(
                object_hook=lambda x: ResponseObject(x) if isinstance(x, dict) else x)
            if response_type:
                r = response_type(self, response_json.__dict__)
                response_json = r

            if 'objects' in response_json and objects_type:
                response_json.objects = [
                    objects_type(self, obj.__dict__)
                    for obj in response_json.objects
                ]
        except ValueError:
            response_json = None

        if response.status_code == 400:
            if response_json and 'error' in response_json:
                raise ValidationError(response_json.error)
            raise ValidationError(
                'A parameter is missing or is invalid while accessing resource'
                'at: {url}'.format(url=response.url))

        if response.status_code == 401:
            if response_json and 'error' in response_json:
                raise AuthenticationError(response_json.error)
            raise AuthenticationError(
                'Failed to authenticate while accessing resource at: '
                '{url}'.format(url=response.url))

        if response.status_code == 404:
            if response_json and 'error' in response_json:
                raise ResourceNotFoundError(response_json.error)
            raise ResourceNotFoundError(
                'Resource not found at: {url}'.format(url=response.url))

        if response.status_code == 405:
            if response_json and 'error' in response_json:
                raise InvalidRequestError(response_json.error)
            raise InvalidRequestError(
                'HTTP method "{method}" not allowed to access resource at: '
                '{url}'.format(method=method, url=response.url))

        if response.status_code == 500:
            if response_json and 'error' in response_json:
                raise PlivoServerError(response_json.error)
            raise PlivoServerError(
                'A server error occurred while accessing resource at: '
                '{url}'.format(url=response.url))

        if method == 'DELETE':
            if response.status_code != 204:
                raise PlivoRestError('Resource at {url} could not be '
                                     'deleted'.format(url=response.url))

        elif response.status_code not in [200, 201, 202]:
            raise PlivoRestError(
                'Received status code {status_code} for the HTTP method '
                '"{method}"'.format(
                    status_code=response.status_code, method=method))

        return response_json

    def create_request(self, method, path=None, data=None):
        path = path or []
        req = Request(method, '/'.join([self.base_uri, self.session.auth[0]] +
                                       list([str(p) for p in path])) + '/',
                      **({
                             'params': data
                         } if method == 'GET' else {
                          'json': data
                      }))
        return self.session.prepare_request(req)

    def create_multipart_request(self,
                                 method,
                                 path=None,
                                 data=None,
                                 files=None):
        path = path or []

        data_args = {}
        if method == 'GET':
            data_args['params'] = data
        else:
            data_args['data'] = data
            if files and 'file' in files and files['file'] != '':
                data_args['files'] = files

        req = Request(method,
                      '/'.join([self.base_uri, self.multipart_session.auth[0]]
                               + list([str(p) for p in path])) + '/', **(
                data_args))
        return self.multipart_session.prepare_request(req)

    def send_request(self, request, **kwargs):
        if 'session' in kwargs:
            session = kwargs['session']
            del kwargs['session']
        else:
            session = self.session

        return session.send(
            request, proxies=self.proxies, timeout=self.timeout, **kwargs)

    def request(self,
                method,
                path=None,
                data=None,
                response_type=None,
                objects_type=None,
                files=None,
                **kwargs):
        if files is not None:
            req = self.create_multipart_request(method, path, data, files)
            session = self.multipart_session
        else:
            req = self.create_request(method, path, data)
            session = self.session
        kwargs['session'] = session
        res = self.send_request(req, **kwargs)
        return self.process_response(method, res, response_type, objects_type)
