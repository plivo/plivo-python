# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface, ResponseObject
from ..exceptions import *
from ..utils import *


class VerifyApp(PlivoResource):
    _name = 'VerifyApp'
    _identifier_string = 'app_uuid'

    def get(self):
        return self.client.verify_apps.get(self.id)

    def update(self,
               name=None,
               brand_name=None,
               otp_type=None,
               otp_length=None,
               otp_expiry=None,
               otp_attempts=None,
               max_validation_attempts=None,
               sms_channel=None,
               voice_channel=None,
               wa_channel=None,
               waba_id=None,
               waba_phone_number=None,
               waba_template_id=None,
               template_uuid=None,
               is_default=None,
               message_redaction=None,
               enable_fraudshield=None,
               fs_protection_level=None,
               customer_app_hash=None,
               client=None):
        return self.client.verify_apps.update(
            self.id,
            name=name,
            brand_name=brand_name,
            otp_type=otp_type,
            otp_length=otp_length,
            otp_expiry=otp_expiry,
            otp_attempts=otp_attempts,
            max_validation_attempts=max_validation_attempts,
            sms_channel=sms_channel,
            voice_channel=voice_channel,
            wa_channel=wa_channel,
            waba_id=waba_id,
            waba_phone_number=waba_phone_number,
            waba_template_id=waba_template_id,
            template_uuid=template_uuid,
            is_default=is_default,
            message_redaction=message_redaction,
            enable_fraudshield=enable_fraudshield,
            fs_protection_level=fs_protection_level,
            customer_app_hash=customer_app_hash,
            client=client,
        )

    def delete(self):
        return self.client.verify_apps.delete(self.id)


class ListVerifyAppsResponseObject(ResponseObject):
    def __init__(self, client, dct):
        super(ListVerifyAppsResponseObject, self).__init__(dct)
        self.error = dct.get('error', None)
        self.verify_apps = dct.get('verify_apps', None)
        self.meta = dct.get('meta', None)
        self.api_id = dct.get('api_id', None)

    def __iter__(self):
        if self.verify_apps is not None:
            return self.verify_apps.__iter__()
        else:
            return iter([])

    def __len__(self):
        if self.verify_apps is not None:
            return len(self.verify_apps)
        else:
            return 0

    def __str__(self):
        import pprint
        if self.verify_apps is not None:
            response_dict = {
                'api_id': self.api_id,
                'meta': self.meta,
                'verify_apps': self.verify_apps,
            }
            return pprint.pformat(response_dict)
        else:
            return str(self.error)

    def __repr__(self):
        if self.verify_apps is not None:
            response_dict = {
                'api_id': self.api_id,
                'meta': self.meta,
                'verify_apps': self.verify_apps,
            }
            return str(response_dict)
        else:
            return str(self.error)

    def has_error(self):
        return self.error is not None


class VerifyApps(PlivoResourceInterface):
    _resource_type = VerifyApp

    @validate_args(
        name=[of_type(six.text_type)],
        brand_name=[optional(of_type(six.text_type))],
        otp_type=[optional(of_type(six.text_type))],
        otp_length=[optional(of_type(*six.integer_types))],
        otp_expiry=[optional(of_type(*six.integer_types))],
        otp_attempts=[optional(of_type(*six.integer_types))],
        max_validation_attempts=[optional(of_type(*six.integer_types))],
        sms_channel=[optional(of_type_exact(bool))],
        voice_channel=[optional(of_type_exact(bool))],
        wa_channel=[optional(of_type_exact(bool))],
        waba_id=[optional(of_type(six.text_type))],
        waba_phone_number=[optional(of_type(six.text_type))],
        waba_template_id=[optional(of_type(six.text_type))],
        template_uuid=[optional(of_type(six.text_type))],
        is_default=[optional(of_type_exact(bool))],
        message_redaction=[optional(of_type_exact(bool))],
        enable_fraudshield=[optional(of_type_exact(bool))],
        fs_protection_level=[optional(of_type(six.text_type))],
        customer_app_hash=[optional(of_type(six.text_type))],
        number_pool=[optional(of_type(six.text_type))],
    )
    def create(self,
               name,
               brand_name=None,
               otp_type=None,
               otp_length=None,
               otp_expiry=None,
               otp_attempts=None,
               max_validation_attempts=None,
               sms_channel=None,
               voice_channel=None,
               wa_channel=None,
               waba_id=None,
               waba_phone_number=None,
               waba_template_id=None,
               template_uuid=None,
               is_default=None,
               message_redaction=None,
               enable_fraudshield=None,
               fs_protection_level=None,
               customer_app_hash=None,
               number_pool=None):
        return self.client.request(
            'POST', ('Verify', 'App'),
            to_param_dict(self.create, locals()))

    @validate_args(
        name=[optional(of_type(six.text_type))],
        subaccount=[optional(of_type(six.text_type))],
        limit=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda limit: 0 < limit <= 20, '0 < limit <= 20')))
        ],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ],
        created_at=[optional(of_type(six.text_type))],
        created_at__lt=[optional(of_type(six.text_type))],
        created_at__lte=[optional(of_type(six.text_type))],
        created_at__gt=[optional(of_type(six.text_type))],
        created_at__gte=[optional(of_type(six.text_type))],
    )
    def list(self,
             name=None,
             subaccount=None,
             limit=None,
             offset=None,
             created_at=None,
             created_at__lt=None,
             created_at__lte=None,
             created_at__gt=None,
             created_at__gte=None):
        return self.client.request(
            'GET', ('Verify', 'App'),
            to_param_dict(self.list, locals()),
            response_type=ListVerifyAppsResponseObject)

    def list_templates(self):
        return self.client.request(
            'GET', ('Verify', 'App', 'templates'), response_type=None)

    @validate_args(app_uuid=[of_type(six.text_type)])
    def get(self, app_uuid):
        return self.client.request(
            'GET', ('Verify', 'App', app_uuid), response_type=VerifyApp)

    @validate_args(
        app_uuid=[of_type(six.text_type)],
        name=[optional(of_type(six.text_type))],
        brand_name=[optional(of_type(six.text_type))],
        otp_type=[optional(of_type(six.text_type))],
        otp_length=[optional(of_type(*six.integer_types))],
        otp_expiry=[optional(of_type(*six.integer_types))],
        otp_attempts=[optional(of_type(*six.integer_types))],
        max_validation_attempts=[optional(of_type(*six.integer_types))],
        sms_channel=[optional(of_type_exact(bool))],
        voice_channel=[optional(of_type_exact(bool))],
        wa_channel=[optional(of_type_exact(bool))],
        waba_id=[optional(of_type(six.text_type))],
        waba_phone_number=[optional(of_type(six.text_type))],
        waba_template_id=[optional(of_type(six.text_type))],
        template_uuid=[optional(of_type(six.text_type))],
        is_default=[optional(of_type_exact(bool))],
        message_redaction=[optional(of_type_exact(bool))],
        enable_fraudshield=[optional(of_type_exact(bool))],
        fs_protection_level=[optional(of_type(six.text_type))],
        customer_app_hash=[optional(of_type(six.text_type))],
        client=[optional(of_type(six.text_type))],
    )
    def update(self,
               app_uuid,
               name=None,
               brand_name=None,
               otp_type=None,
               otp_length=None,
               otp_expiry=None,
               otp_attempts=None,
               max_validation_attempts=None,
               sms_channel=None,
               voice_channel=None,
               wa_channel=None,
               waba_id=None,
               waba_phone_number=None,
               waba_template_id=None,
               template_uuid=None,
               is_default=None,
               message_redaction=None,
               enable_fraudshield=None,
               fs_protection_level=None,
               customer_app_hash=None,
               client=None):
        return self.client.request(
            'POST', ('Verify', 'App', app_uuid),
            to_param_dict(self.update, locals()))

    @validate_args(app_uuid=[of_type(six.text_type)])
    def delete(self, app_uuid):
        return self.client.request('DELETE', ('Verify', 'App', app_uuid))