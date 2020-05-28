import sys
from hmac import new as sign
from hashlib import sha256
from .validators import *

PY2 = True if sys.version_info.major == 2 else False

if PY2:
    from urlparse import urlparse, urlunparse, parse_qs
    from base64 import encodestring as encode
else:
    from urllib.parse import urlparse, urlunparse, parse_qs
    from base64 import encodebytes as encode



def string_format(value):
    if isinstance(value, bytes):
        return ''.join(chr(x) for x in bytearray(value))
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, list):
        return [string_format(x) for x in value]
    if PY2 == True and isinstance(value, unicode):
        return value.decode('utf-8')
    return value


def get_map_from_query(query):
    res_map = dict()
    for key, value in parse_qs(query, keep_blank_values=True).items():
        res_map[string_format(key)] = string_format(value)
    return res_map


def get_sorted_query_string(params):
    keys = sorted(params.keys())
    res_params = []
    for key in keys:
        value = params[key]
        if isinstance(value, list):
            res_params.append(
                '&'.join(['{}={}'.format(string_format(key), val) for val in sorted(string_format(value))]))
        else:
            res_params.append('{}={}'.format(string_format(key), string_format(value)))
    return '&'.join(res_params)


def get_sorted_params_string(params):
    keys = sorted(params.keys())
    res_params = []
    for key in keys:
        value = params[key]
        if isinstance(value, list):
            res_params.append(
                ''.join(['{}{}'.format(string_format(key), val) for val in sorted(string_format(value))]))
        elif isinstance(value, dict):
            res_params.append('{}{}'.format(string_format(key), get_sorted_params_string(value)))
        else:
            res_params.append('{}{}'.format(string_format(key), string_format(value)))
    return ''.join(res_params)


def construct_get_url(uri, params, empty_post_params=True):
    parsed_uri = urlparse(uri.encode('utf-8'))
    base_url = urlunparse((parsed_uri.scheme.decode('utf-8'),
                           parsed_uri.netloc.decode('utf-8'),
                           parsed_uri.path.decode('utf-8'), '', '',
                           '')).encode('utf-8')

    params.update(get_map_from_query(parsed_uri.query))
    query_params = get_sorted_query_string(params)
    if len(query_params) > 0 or not empty_post_params:
        base_url = base_url + bytearray('?' + query_params, 'utf-8')
    if len(query_params) > 0 and not empty_post_params:
        base_url = base_url + bytearray('.', 'utf-8')
    return base_url


def construct_post_url(uri, params):
    base_url = construct_get_url(uri, dict(), True if len(params) == 0 else False)
    return base_url + bytearray(get_sorted_params_string(params), 'utf-8')


def get_signature_v3(auth_token, base_url, nonce):
    base_url = bytearray('{}.{}'.format(string_format(base_url), string_format(nonce)), 'utf-8')
    try:
        return encode(sign(auth_token, base_url, sha256).digest()).strip()
    except TypeError:
        return encode(sign(bytearray(auth_token, 'utf-8'), base_url, sha256).digest()).strip()


@validate_args(
    method=[all_of(of_type(six.text_type), is_in(('POST', 'GET'), case_sensitive=False))],
    uri=[is_url()],
    params=[optional(of_type(dict))],
    nonce=[of_type(six.text_type)],
    auth_token=[of_type(six.text_type)],
    v3_signature=[of_type(six.text_type)],
)
def validate_v3_signature(method, uri, nonce, auth_token, v3_signature, params=None):
    """
        Validates V3 Signature received from Plivo to your server

        :param method: Your callback method
        :param uri: Your callback URL
        :param params: Params received in callback from Plivo
        :param nonce: X-Plivo-Signature-V3-Nonce header
        :param v3_signature: X-Plivo-Signature-V3 header
        :param auth_token: (Sub)Account auth token

        :return: True if the request matches signature, False otherwise
    """
    if params is None:
        params = dict()
    auth_token = bytes(auth_token.encode('utf-8'))
    nonce = bytes(nonce.encode('utf-8'))
    v3_signature = bytes(v3_signature.encode('utf-8'))
    base_url = construct_get_url(uri, params) if method == 'GET' else construct_post_url(uri, params)
    signature = get_signature_v3(auth_token, base_url, nonce)
    return signature in v3_signature.split(b',')
