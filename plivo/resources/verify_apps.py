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
               sms_channel=None,
               voice_channel=None,
               wa_channel=None,
               is_default=None,
               template_uuid=None,
               message_redaction=None,
               customer_app_hash=None,
               max_validation_attempts=None,
               enable_fraudshield=None,
               fs_protection_level=None,
               waba_id=None,
               waba_phone_number=None,
               waba_template_id=None):
        return self.client.verify_apps.update(
            self.id,
            name=name,
            brand_name=brand_name,
            otp_type=otp_type,
            otp_length=otp_length,
            otp_expiry=otp_expiry,
            otp_attempts=otp_attempts,
            sms_channel=sms_channel,
            voice_channel=voice_channel,
            wa_channel=wa_channel,
            is_default=is_default,
            template_uuid=template_uuid,
            message_redaction=message_redaction,
            customer_app_hash=customer_app_hash,
            max_validation_attempts=max_validation_attempts,
            enable_fraudshield=enable_fraudshield,
            fs_protection_level=fs_protection_level,
            waba_id=waba_id,
            waba_phone_number=waba_phone_number,
            waba_template_id=waba_template_id,
        )

    def delete(self):
        return self.client.verify_apps.delete(self.id)


class ListVerifyAppsResponse(ResponseObject):
    def __init__(self, client, dct):
        super(ListVerifyAppsResponse, self).__init__(dct)
        self.error = dct.get('error', None)
        self.verify_apps = dct.get('verify_apps', None)
        self.meta = dct.get('meta', None)
        self.apiID = dct.get('api_id', None)

    def __iter__(self):
        if self.verify_apps is not None:
            return self.verify_apps.__iter__()
        return iter([])

    def __len__(self):
        if self.verify_apps is not None:
            return len(self.verify_apps)
        return 0

    def __str__(self):
        import pprint
        if self.verify_apps is not None:
            response_dict = {
                'api_id': self.apiID,
                'meta': self.meta,
                'verify_apps': self.verify_apps,
            }
            return pprint.pformat(response_dict)
        return str(self.error)

    def __repr__(self):
        if self.verify_apps is not None:
            response_dict = {
                'api_id': self.apiID,
                'meta': self.meta,
                'verify_apps': [app for app in self.verify_apps],
            }
            return str(response_dict)
        return str(self.error)

    def has_error(self):
        return self.error is not None


class VerifyApps(PlivoResourceInterface):
    _resource_type = VerifyApp

    @validate_args(
        name=[of_type(six.text_type)],
        otp_type=[optional(of_type(six.text_type))],
        otp_length=[optional(of_type(*six.integer_types))],
        otp_expiry=[optional(of_type(*six.integer_types))],
        otp_attempts=[optional(of_type(*six.integer_types))],
        brand_name=[optional(of_type(six.text_type))],
        sms_channel=[optional(of_type_exact(bool))],
        voice_channel=[optional(of_type_exact(bool))],
        wa_channel=[optional(of_type_exact(bool))],
        is_default=[optional(of_type_exact(bool))],
        template_uuid=[optional(of_type(six.text_type))],
        message_redaction=[optional(of_type_exact(bool))],
        customer_app_hash=[optional(of_type(six.text_type))],
        max_validation_attempts=[optional(of_type(*six.integer_types))],
        enable_fraudshield=[optional(of_type_exact(bool))],
        fs_protection_level=[optional(of_type(six.text_type))],
        waba_id=[optional(of_type(six.text_type))],
        waba_phone_number=[optional(of_type(six.text_type))],
        waba_template_id=[optional(of_type(six.text_type))],
    )
    def create(self,
               name,
               otp_type=None,
               otp_length=None,
               otp_expiry=None,
               otp_attempts=None,
               brand_name=None,
               sms_channel=None,
               voice_channel=None,
               wa_channel=None,
               is_default=None,
               template_uuid=None,
               message_redaction=None,
               customer_app_hash=None,
               max_validation_attempts=None,
               enable_fraudshield=None,
               fs_protection_level=None,
               waba_id=None,
               waba_phone_number=None,
               waba_template_id=None):
        return self.client.request(
            'POST', ('Verify', 'App'),
            to_param_dict(self.create, locals()))

    @validate_args(
        name=[optional(of_type(six.text_type))],
        app_uuid=[optional(of_type(six.text_type))],
        channel=[optional(of_type(six.text_type))],
        status=[optional(of_type(six.text_type))],
        limit=[optional(of_type(*six.integer_types))],
        offset=[optional(of_type(*six.integer_types))],
        created_at=[optional(of_type(six.text_type))],
        created_at__lt=[optional(of_type(six.text_type))],
        created_at__lte=[optional(of_type(six.text_type))],
        created_at__gt=[optional(of_type(six.text_type))],
        created_at__gte=[optional(of_type(six.text_type))],
        subaccount_auth_id=[optional(of_type(six.text_type))],
    )
    def list(self,
             name=None,
             app_uuid=None,
             channel=None,
             status=None,
             limit=None,
             offset=None,
             created_at=None,
             created_at__lt=None,
             created_at__lte=None,
             created_at__gt=None,
             created_at__gte=None,
             subaccount_auth_id=None):
        return self.client.request(
            'GET', ('Verify', 'App'),
            to_param_dict(self.list, locals()),
            response_type=ListVerifyAppsResponse,
            objects_type=VerifyApp)

    @validate_args(
        app_uuid=[of_type(six.text_type)],
    )
    def get(self, app_uuid):
        return self.client.request(
            'GET', ('Verify', 'App', app_uuid),
            response_type=VerifyApp)

    @validate_args(
        app_uuid=[of_type(six.text_type)],
        name=[optional(of_type(six.text_type))],
        brand_name=[optional(of_type(six.text_type))],
        otp_type=[optional(of_type(six.text_type))],
        otp_length=[optional(of_type(*six.integer_types))],
        otp_expiry=[optional(of_type(*six.integer_types))],
        otp_attempts=[optional(of_type(*six.integer_types))],
        sms_channel=[optional(of_type_exact(bool))],
        voice_channel=[optional(of_type_exact(bool))],
        wa_channel=[optional(of_type_exact(bool))],
        is_default=[optional(of_type_exact(bool))],
        template_uuid=[optional(of_type(six.text_type))],
        message_redaction=[optional(of_type_exact(bool))],
        customer_app_hash=[optional(of_type(six.text_type))],
        max_validation_attempts=[optional(of_type(*six.integer_types))],
        enable_fraudshield=[optional(of_type_exact(bool))],
        fs_protection_level=[optional(of_type(six.text_type))],
        waba_id=[optional(of_type(six.text_type))],
        waba_phone_number=[optional(of_type(six.text_type))],
        waba_template_id=[optional(of_type(six.text_type))],
    )
    def update(self,
               app_uuid,
               name=None,
               brand_name=None,
               otp_type=None,
               otp_length=None,
               otp_expiry=None,
               otp_attempts=None,
               sms_channel=None,
               voice_channel=None,
               wa_channel=None,
               is_default=None,
               template_uuid=None,
               message_redaction=None,
               customer_app_hash=None,
               max_validation_attempts=None,
               enable_fraudshield=None,
               fs_protection_level=None,
               waba_id=None,
               waba_phone_number=None,
               waba_template_id=None):
        return self.client.request(
            'POST', ('Verify', 'App', app_uuid),
            to_param_dict(self.update, locals()))

    @validate_args(
        app_uuid=[of_type(six.text_type)],
    )
    def delete(self, app_uuid):
        return self.client.request(
            'DELETE', ('Verify', 'App', app_uuid))