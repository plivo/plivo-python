from __future__ import absolute_import
import jwt, time
from plivo.utils.validators import *

"""
Class to represent plivo token for endpoint authentication
"""
class AccessToken:
    auth_id = ''
    username = ''
    valid_from = 0
    lifetime = 86400
    key = ''
    grants = {}
    uid = 0

    @validate_args(
        auth_id=[is_account_id()],
        auth_token=[optional(of_type(six.text_type))],
        username=[all_of(
            of_type(six.text_type),
            check(lambda username: len(username) > 0, 'empty username')
        )],
        valid_from=[optional(of_type(*six.integer_types))],
        lifetime=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda lifetime: 180 <= lifetime <= 86400,
                          '180 < lifetime <= 86400')))
        ],
        valid_till=[optional(of_type(*six.integer_types))],
    )
    def __init__(self,
                 auth_id,
                 auth_token,
                 username,
                 valid_from=None,
                 lifetime=None,
                 valid_till=None,
                 uid=None):
        self.auth_id = auth_id
        self.username = username
        if valid_from:
            self.valid_from = int(valid_from)
        else:
            self.valid_from = int(time.time())
        if lifetime:
            self.lifetime = int(lifetime)
            if valid_till is not None:
                raise ValidationError("use either lifetime or valid_till")
        elif valid_till:
            self.lifetime = valid_till - self.valid_from
            if self.lifetime < 0:
                raise ValidationError(
                    "validity expires %s seconds before it starts" %
                    self.lifetime)
            if self.lifetime < 180 or self.lifetime > 86400:
                raise ValidationError(
                    "validity of %s seconds is out of permitted range [180, 86400]" %
                    self.lifetime)

        self.key = auth_token

        if uid:
            self.uid = uid
        else:
            self.uid = "%s-%s" % (username, time.time())

    @validate_args(
        incoming=[optional(of_type_exact(bool))],
        outgoing=[optional(of_type_exact(bool))],
    )
    def add_voice_grants(self, incoming=False, outgoing=False):
        self.grants['voice'] = {
            'incoming_allow': incoming,
            'outgoing_allow': outgoing
        }

    def to_jwt(self):
        headers = {'typ': 'JWT', 'cty': 'plivo;v=1'}
        algorithm = 'HS256'
        claims = {
            'jti': self.uid,
            'iss': self.auth_id,
            'sub': self.username,
            'nbf': self.valid_from,
            'exp': self.valid_from + self.lifetime,
            'grants': self.grants
        }
        return jwt.encode(claims, self.key, algorithm, headers).decode('utf-8')
