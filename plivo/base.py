# -*- coding: utf-8 -*-
"""
Base classes, used to deal with every Plivo resource.
"""

import pprint

from plivo.exceptions import InvalidRequestError


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
        if not getattr(self, 'list') or not self.__class__._iterable:
            raise NotImplementedError(
                'list is not supported for this resource')

        def gen():
            limit = 20
            offset = 0
            while True:
                response = self.list(limit=limit, offset=offset)
                if not response.objects:
                    return

                for item in response:
                    yield item
                offset += limit

        return gen()