# -*- coding: utf-8 -*-
from plivo.utils import to_param_dict
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface


class Address(PlivoResource):
    _name = 'Address'
    _identifier_string = 'id'

    def update(self,
               salutation=None,
               first_name=None,
               last_name=None,
               country_iso=None,
               address_line1=None,
               address_line2=None,
               city=None,
               region=None,
               postal_code=None,
               alias=None,
               file_to_upload=None,
               auto_correct_address=None,
               callback_url=None):
        return self.client.addresses.update(
            self.id, salutation, first_name, last_name, country_iso,
            address_line1, address_line2, city, region, postal_code, alias,
            file_to_upload, auto_correct_address, callback_url)

    def delete(self):
        return self.client.addresses.delete(self.id)


class Addresses(PlivoResourceInterface):
    _resource_type = Address

    @validate_args(
        country_iso=[of_type(six.text_type)],
        salutation=[all_of(of_type(six.text_type), is_in(('Mr', 'Ms')))],
        first_name=[of_type(six.text_type)],
        last_name=[of_type(six.text_type)],
        address_line1=[of_type(six.text_type)],
        address_line2=[of_type(six.text_type)],
        city=[of_type(six.text_type)],
        region=[of_type(six.text_type)],
        postal_code=[of_type(six.text_type)],
        address_proof_type=[
            all_of(
                of_type(six.text_type),
                is_in(('national_id', 'passport', 'business_id', 'NIF', 'NIE',
                       'DNI', 'others')))
        ],
        alias=[optional(of_type(six.text_type))],
        file_to_upload=[optional(of_type(six.text_type))],
        auto_correct_address=[optional(of_type_exact(bool))],
        fiscal_identification_code=[optional(of_type(six.text_type))],
        street_code=[optional(of_type(six.text_type))],
        municipal_code=[optional(of_type(six.text_type))])
    def create(self,
               country_iso,
               salutation,
               first_name,
               last_name,
               address_line1,
               address_line2,
               city,
               region,
               postal_code,
               address_proof_type,
               alias=None,
               file_to_upload=None,
               auto_correct_address=None,
               fiscal_identification_code=None,
               street_code=None,
               municipal_code=None,
               callback_url=None):
        if country_iso == 'ES' and not fiscal_identification_code:
            raise ValidationError(
                'The parameter fiscal_identification_code is required for Spain numbers'
            )

        if country_iso == 'DK' and not all(street_code, municipal_code):
            raise ValidationError(
                'The parameters street_code and municipal_code are required for Denmark numbers'
            )

        if file_to_upload:
            file_extension = file_to_upload.strip().split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'png', 'pdf']:
                raise ValidationError(
                    'File format of the file to be uploaded should be one of JPG, JPEG, PNG or PDF'
                )

            content_types = {
                'jpeg': 'image/jpeg',
                'jpg': 'image/jpeg',
                'png': 'image/png',
                'pdf': 'application/pdf',
            }

            import os

            files = {
                'file': (file_to_upload.split(os.sep)[-1], open(
                    file_to_upload, 'rb'), content_types[file_extension])
            }
        else:
            files = {'file': ''}
        data_to_send = to_param_dict(self.create, locals())
        return self.client.request(
            'POST', ('Verification', 'Address'), data_to_send, files=files)

    @validate_args(
        address_id=[of_type(six.text_type)],
        salutation=[all_of(of_type(six.text_type), is_in(('Mr', 'Ms')))],
        first_name=[of_type(six.text_type)],
        last_name=[of_type(six.text_type)],
        country_iso=[optional(of_type(six.text_type))],
        address_line1=[optional(of_type(six.text_type))],
        address_line2=[optional(of_type(six.text_type))],
        city=[optional(of_type(six.text_type))],
        region=[optional(of_type(six.text_type))],
        postal_code=[optional(of_type(six.text_type))],
        alias=[optional(of_type(six.text_type))],
        file_to_upload=[optional(of_type(six.text_type))],
        auto_correct_address=[optional(of_type_exact(bool))], )
    def update(self,
               address_id,
               salutation=None,
               first_name=None,
               last_name=None,
               country_iso=None,
               address_line1=None,
               address_line2=None,
               city=None,
               region=None,
               postal_code=None,
               alias=None,
               file_to_upload=None,
               auto_correct_address=None,
               callback_url=None):
        if file_to_upload:
            file_extension = file_to_upload.strip().split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'png', 'pdf']:
                raise ValidationError(
                    'File format of the file to be uploaded should be one of JPG, JPEG, PNG or PDF'
                )

            content_types = {
                'jpeg': 'image/jpeg',
                'jpg': 'image/jpeg',
                'png': 'image/png',
                'pdf': 'application/pdf',
            }

            import os

            files = {
                'file': (file_to_upload.split(os.sep)[-1], open(
                    file_to_upload, 'rb'), content_types[file_extension])
            }
        else:
            files = {'file': ''}

        data_to_send = to_param_dict(self.create, locals())
        return self.client.request(
            'POST', ('Verification', 'Address', address_id),
            data_to_send,
            files=files)

    @validate_args(address_id=[of_type(six.text_type)])
    def get(self, address_id):
        return self.client.request(
            'GET', ('Verification', 'Address', address_id),
            response_type=Address)

    @validate_args(
        country_iso=[optional(of_type(six.text_type))],
        customer_name=[optional(of_type(six.text_type))],
        alias=[optional(of_type(six.text_type))],
        verification_status=[
            optional(
                all_of(
                    of_type(six.text_type),
                    is_in(('pending', 'accepted', 'rejected', ))))
        ],
        validation_status=[
            optional(
                all_of(
                    of_type(six.text_type),
                    is_in(('pending', 'accepted', 'rejected', ))))
        ],
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
        ])
    def list(self,
             country_iso=None,
             customer_name=None,
             alias=None,
             verification_status=None,
             validation_status=None,
             limit=20,
             offset=0):
        return self.client.request(
            'GET', ('Verification', 'Address', ),
            to_param_dict(self.list, locals()),
            response_type=ListResponseObject,
            objects_type=Address)

    @validate_args(address_id=[of_type(six.text_type)])
    def delete(self, address_id):
        return self.client.request('DELETE', ('Verification', 'Address',
                                              address_id))
