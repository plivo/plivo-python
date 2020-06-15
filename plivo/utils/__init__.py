# -*- coding: utf-8 -*-
import inspect
import re
from datetime import datetime

from base64 import encodestring
from hmac import new as hnew
from hashlib import sha256
from .signature_v3 import validate_v3_signature

try:
    from urllib.parse import urlparse, urlunparse
except ImportError:
    from urlparse import urlparse, urlunparse


def validate_signature(uri, nonce, signature, auth_token=''):
    """
    Validates requests made by Plivo to your servers.

    :param uri: Your server URL
    :param nonce: X-Plivo-Signature-V2-Nonce
    :param signature: X-Plivo-Signature-V2 header
    :param auth_token: Plivo Auth token
    :return: True if the request matches signature, False otherwise
    """

    auth_token = bytes(auth_token.encode('utf-8'))
    nonce = bytes(nonce.encode('utf-8'))
    signature = bytes(signature.encode('utf-8'))

    parsed_uri = urlparse(uri.encode('utf-8'))
    base_url = urlunparse((parsed_uri.scheme.decode('utf-8'),
                           parsed_uri.netloc.decode('utf-8'),
                           parsed_uri.path.decode('utf-8'), '', '',
                           '')).encode('utf-8')

    return encodestring(hnew(auth_token, base_url + nonce, sha256)
                        .digest()).strip() == signature


def is_valid_time_comparison(time):
    if isinstance(time, datetime):
        return True
    return False


def is_valid_subaccount(subaccount):
    subaccount_string = str(subaccount)
    if len(subaccount_string) == 20 and subaccount_string[:2] == 'SA':
        return True
    return False


def is_valid_mainaccount(mainaccount):
    mainaccount_string = str(mainaccount)
    if len(mainaccount_string) == 20 and mainaccount_string[:2] == 'MA':
        return True
    return False


def to_param_dict(func, vals, exclude_none=True, func_args_check=True):
    args, varargs, kwargs, _ = inspect.getargspec(func)
    arg_names = list(args)
    # The bit of regex magic below is for arguments that are keywords in
    # Python, like from. These can't be used directly, so our convention is to
    # add "_" suffixes to them. This strips them out.
    pd = {
        re.sub(r'^(.*)_+$', r'\1', key): value
        for key, value in vals.items()
        if key != 'self' and (key in arg_names or func_args_check==False) and (
            value is not None or exclude_none is False)
    }
    return pd
