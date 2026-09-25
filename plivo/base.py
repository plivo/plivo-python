# -*- coding: utf-8 -*-
"""
Base classes, used to deal with every Plivo resource.
"""

import pprint

from plivo.exceptions import InvalidRequestError

try:
    from urllib.parse import parse_qs, urlparse
except ImportError:
    from urlparse import parse_qs, urlparse

DEFAULT_PAGE_LIMIT = 20

# Outcomes of _next_page_params() that aren't a params dict.
_END_OF_PAGES = object()  # meta says there is no next page
_NO_PAGE_HINT = object()  # response carried no meta to follow


def _attr(obj, key):
    """Read a key off a response fragment, dict or ResponseObject alike."""
    if isinstance(obj, dict):
        return obj.get(key)
    # getattr, not []: ResponseObject.__getitem__ falls back to
    # self.objects on a miss, which is not what we want here.
    return getattr(obj, key, None)


def _next_page_params(response, limit):
    """Derive the next page's request params from a list response's meta.

    meta.next is a relative URL whose query string carries either an
    opaque cursor or a plain offset, depending on which pagination mode
    the deployment happens to be serving:

        '/v1/.../Call/?limit=20&cursor=<opaque>'   cursor / hybrid
        '/v1/.../Call/?limit=20&offset=20'         offset (legacy)

    Reading whichever param is present is what lets one walk stay correct
    in all three modes without the SDK knowing which one is live.

    Returns a params dict, or _END_OF_PAGES / _NO_PAGE_HINT.
    """
    meta = _attr(response, 'meta')
    if meta is None:
        return _NO_PAGE_HINT

    next_url = _attr(meta, 'next')
    if not next_url:
        return _END_OF_PAGES

    query = parse_qs(urlparse(str(next_url)).query)

    next_limit = query.get('limit', [None])[0]
    if next_limit is not None:
        try:
            limit = int(next_limit)
        except ValueError:
            pass

    cursor = query.get('cursor', [None])[0]
    if cursor:
        # A cursor supersedes offset, and offset must not ride along with
        # it: under hybrid the server still applies a supplied offset,
        # which would pin the walk to page 1 forever.
        return {'limit': limit, 'cursor': cursor, 'offset': None}

    offset = query.get('offset', [None])[0]
    if offset is not None:
        try:
            return {'limit': limit, 'offset': int(offset)}
        except ValueError:
            return _END_OF_PAGES

    # meta.next is there but carries neither param we understand.
    return _NO_PAGE_HINT


class Meta:
    def __init__(self):
        self.limit = None
        self.next = None
        self.offset = None
        self.previous = None
        self.total_count = None


class PlivoGenericResponse(object):
    """A generic response to cover it all!

    This provides a generic blanket response based on what is received from
    Plivo servers.

    This will be used only during POST and DELETE requests.
    """

    def __init__(self, params_dict, id_string=None):
        for i in params_dict:
            self.__dict__[i] = params_dict[i]

        if id_string and id_string in params_dict:
            self.__dict__['id'] = params_dict[id_string]


class ResponseObject(object):
    def __init__(self, dct):
        self.__dict__.update(dct)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, item):
        try:
            return self.__dict__.__getitem__(item)
        except KeyError:
            return self.objects.__getitem__(item)

    def __setitem__(self, key, value):
        self.__dict__.__setitem__(key, value)

    def __delitem__(self, key):
        del self.__dict__

    def __str__(self):
        return pprint.pformat(self.__dict__)

    def __repr__(self):
        return pprint.pformat(self.__dict__)


class ListSessionResponseObject(ResponseObject):
    def __init__(self, client, dct):
        super(ListSessionResponseObject, self).__init__(dct)
        self.error = dct.get('error', None)
        self.sessions = dct.get('sessions', None)
        self.meta = dct.get('meta', None)
        self.apiID = dct.get('api_id', None)
    def __iter__(self):
        if self.sessions is not None:
            return self.sessions.__iter__()
        else:
            return iter([])

    def __len__(self):
        if self.sessions is not None:
            return len(self.sessions)
        else:
            return 0  # Return 0 for error case

    def __str__(self):
        if self.sessions is not None:
            response_dict = {'api_id': self.apiID, 'meta': self.meta, 'sessions': self.sessions}
            return pprint.pformat(response_dict)
        else:
            return str(self.error)  # Display error message for error case

    def __repr__(self):
        if self.sessions is not None:
            response_dict = {'api_id': self.apiID, 'meta': self.meta, 'sessions': [session for session in self.sessions]}
            return str(response_dict)
        else:
            return str(self.error)  # Display error message for error case

    def has_error(self):
        return self.error is not None


class ListMessagesResponseObject(ResponseObject):
    def __init__(self, client, dct):
        super(ListMessagesResponseObject, self).__init__(dct)
        self.error = dct.get('error', None)
        self.objects = dct.get('objects', None)
        self.meta = dct.get('meta', None)
        self.apiID = dct.get('api_id', None)

    def __iter__(self):
        if self.objects is not None:
            return self.objects.__iter__()
        else:
            return iter([])

    def __len__(self):
        if self.objects is not None:
            return len(self.objects)
        else:
            return 0  # Return 0 for error case

    def __str__(self):
        if self.objects is not None:
            response_dict = {'api_id': self.apiID, 'meta': self.meta, 'objects': self.objects}
            return pprint.pformat(response_dict)
        else:
            return str(self.error)  # Display error message for error case

    def __repr__(self):
        if self.objects is not None:
            response_dict = {'api_id': self.apiID, 'meta': self.meta, 'objects': [session for session in self.objects]}
            return str(response_dict)
        else:
            return str(self.error)  # Display error message for error case

    def has_error(self):
        return self.error is not None


class ListResponseObject(ResponseObject):
    def __init__(self, client, dct):
        super(ListResponseObject, self).__init__(dct)

    def __iter__(self):
        return self.objects.__iter__()

    def __len__(self):
        return len(self.objects)

    def __str__(self):
        return pprint.pformat(self.objects)

    def __repr__(self):
        return str([object for object in self.objects])

class ListTollfreeVerificationResponseObject(ResponseObject):
    def __init__(self, client, dct):
        super(ListTollfreeVerificationResponseObject, self).__init__(dct)
        self.error = dct.get('error', None)
        self.objects = dct.get('objects', [])
        self.meta = dct.get('meta', None)
        self.apiID = dct.get('api_id', None)

    def __iter__(self):
        if self.objects is not None:
            return self.objects.__iter__()
        else:
            return iter([])

    def __len__(self):
        if self.objects is not None:
            return len(self.objects)
        else:
            return 0  # Return 0 for error case

    def __str__(self):
        if self.objects is not None:
            response_dict = {'api_id': self.apiID, 'meta': self.meta, 'objects': self.objects}
            return pprint.pformat(response_dict)
        else:
            return str(self.error)  # Display error message for error case

    def __repr__(self):
        if self.objects is not None:
            response_dict = {'api_id': self.apiID, 'meta': self.meta, 'objects': [session for session in self.objects]}
            return str(response_dict)
        else:
            return str(self.error)  # Display error message for error case

    def has_error(self):
        return self.error is not None

class PlivoResource(ResponseObject):
    """The Plivo resource object

    This provides an interface to deal with all Plivo resources and
    sub-resources
    """

    _identifier_string = None

    @property
    def id(self):
        value = self.__dict__.get(self._identifier_string, None)
        if not value:
            raise ValueError('{} must be set'.format(self._identifier_string))
        return value

    def __init__(self, client, data):
        """Sets up the resource URI along with a hack for Account resource"""

        super(PlivoResource, self).__init__(data)
        self._name = self._name or self.__class__.__name__
        self.client = client

    def __str__(self):
        # return '{class_name}({identifier})'.format(
        #    class_name=self._name, identifier=self.id)

        return pprint.pformat(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def update(self, params, path, **kwargs):
        """
        Test Update
        :param params:
        :param path:
        :param random:
        """
        self.client.request('POST', params, path, **kwargs)

    def _update(self, params):
        if not self.id:
            raise InvalidRequestError(
                'Cannot update a {resource_type} resource without an '
                'identifier'.format(resource_type=self._name))

        response_json = self.client.send_request(
            self.__resource_uri, method='POST', data=params)

        for key in params:
            self.__dict__[key] = params[key]

        for key in response_json:
            self.__dict__[key] = response_json[key]

        return self

    def _execute_action(self,
                        action=None,
                        method='GET',
                        params=None,
                        parse=False):
        if not action:
            response = self.client.send_request(
                self.__resource_uri, method=method, data=params)
        else:
            response = self.client.send_request(
                self.__resource_uri + action + '/', method=method, data=params)

        if not parse:
            return response

        self.__resource_json = response
        self.__parse_json()

        try:
            self.id = response[self._identifier_string]
        except AttributeError:
            pass

        if method == 'POST':
            self.__resource_json = params
            self.__parse_json()
        return self

    def delete(self):
        if not self.id:
            raise InvalidRequestError(
                'Cannot delete a {resource_type} resource without an '
                'identifier'.format(resource_type=self._name))

        return PlivoGenericResponse(
            self.client.send_request(self.__resource_uri, method='DELETE'))

    def get(self):
        if not self.id:
            raise InvalidRequestError(
                'Cannot get a {resource_type} resource without an '
                'identifier'.format(resource_type=self._name))

        self.__resource_json = self.client.send_request(self.__resource_uri)
        self.__parse_json()
        return self

    def create(self, params):
        if self.id:
            raise InvalidRequestError(
                'Cannot create a {resource_type} resource because another'
                ' {resource_type} resource exists with the same '
                'identifier: {identifier}.'.format(
                    resource_type=self._name, identifier=self.id))

        id_string = None
        if self._identifier_string:
            id_string = self._identifier_string

        return PlivoGenericResponse(
            self.client.send_request(
                self.__resource_uri, data=params, method='POST'), id_string)


class SecondaryPlivoResource(PlivoResource):
    """
        SecondaryPlivoResource resource object
        This provides an interface to deal with resources where identifier is has a mid level parent
    """
    _secondary_identifier_string = None

    @property
    def secondary_id(self):
        value = self.__dict__.get(self._secondary_identifier_string, None)
        if not value:
            raise ValueError('{} must be set'.format(self._secondary_identifier_string))
        return value

    def __init__(self, client, data):
        """Sets up the PlivoResource"""
        super(SecondaryPlivoResource, self).__init__(client, data)
        self._name = self._name or self.__class__.__name__
        self.client = client


class PlivoResourceInterface(object):
    _iterable = True

    def __init__(self, client, **kwargs):
        self.client = client

    def __iter__(self):
        """Walks every page of this resource, one record at a time.

        Follows meta.next rather than computing its own offsets, so the
        walk stays correct whether the deployment applies offset, ignores
        it in favour of cursors, or serves the hybrid of the two. Falls
        back to incrementing offset only for responses that carry no meta.
        """
        if not getattr(self, 'list', None) or not self.__class__._iterable:
            raise NotImplementedError(
                'list is not supported for this resource')

        def gen():
            limit = DEFAULT_PAGE_LIMIT
            params = {'limit': limit, 'offset': 0}

            while True:
                response = self.list(**params)
                if not _attr(response, 'objects'):
                    return

                for item in response:
                    yield item

                next_params = _next_page_params(response, limit)

                if next_params is _END_OF_PAGES:
                    return

                if next_params is _NO_PAGE_HINT:
                    # No usable meta. If we were walking by offset we can
                    # carry on and stop on the first empty page; if we
                    # were following a cursor there is nothing to follow.
                    if params.get('offset') is None:
                        return
                    next_params = dict(params)
                    next_params['offset'] += limit

                if next_params == params:
                    # Never re-request the page we just consumed. A server
                    # that ignores our paging params would otherwise hand
                    # back page 1 forever.
                    return

                params = next_params
                limit = params.get('limit') or limit

        return gen()
