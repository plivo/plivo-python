# -*- coding: utf-8 -*-
class PlivoRestError(Exception):
    pass


class AuthenticationError(PlivoRestError):
    pass


class InvalidRequestError(PlivoRestError):
    pass


class PlivoServerError(PlivoRestError):
    pass


class PlivoXMLError(PlivoRestError):
    pass


class ResourceNotFoundError(PlivoRestError):
    pass


class ValidationError(PlivoRestError):
    pass
