# -*- coding: utf-8 -*-
from plivo.utils import to_param_dict
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface


class Identity(PlivoResource):
    _name = 'Identity'
    _identifier_string = 'id'

    def update(self,
               country_iso=None,
               salutation=None,
               first_name=None,
               last_name=None,
               birth_place=None,
               birth_date=None,
               nationality=None,
               id_nationality=None,
               id_issue_date=None,
               id_type=None,
               id_number=None,
               address_line1=None,
               address_line2=None,
               city=None,
               region=None,
               postal_code=None,
               alias=None,
               business_name=None,
               fiscal_identification_code=None,
               street_code=None,
               municipal_code=None,
               subaccount=None,
               file=None,
               auto_correct_address=None,
               callback_url=None):
        return self.client.identities.update(
            self.id, country_iso, salutation, first_name, last_name,
            birth_place, birth_date, nationality, id_nationality,
            id_issue_date, id_type, id_number, alias, business_name,
            subaccount, file, callback_url)

    def delete(self):
        return self.client.identities.delete(self.id)


class Identities(PlivoResourceInterface):
    _resource_type = Identity

    @validate_args(
        country_iso=[of_type(six.text_type)],
        salutation=[all_of(of_type(six.text_type), is_in(('Mr', 'Ms')))],
        first_name=[of_type(six.text_type)],
        last_name=[of_type(six.text_type)],
        birth_place=[of_type(six.text_type)],
        birth_date=[of_type(six.text_type)],
        nationality=[of_type(six.text_type)],
        id_nationality=[of_type(six.text_type)],
        id_issue_date=[of_type(six.text_type)],
        id_type=[of_type(six.text_type)],
        id_number=[of_type(six.text_type)],
        phone_number_country=[of_type(six.text_type)],
        number_type=[all_of(of_type(six.text_type),
                    is_in(("local", "national", "mobile", "tollfree")))
        ],
        address_line1=[of_type(six.text_type)],
        address_line2=[of_type(six.text_type)],
        city=[of_type(six.text_type)],
        region=[of_type(six.text_type)],
        postal_code=[of_type(six.text_type)],
        callback_url=[optional(of_type(six.text_type))],
        proof_type=[
          all_of(
              of_type(six.text_type),
              is_in(('national_id', 'passport', 'business_id', 'NIF', 'NIE',
                     'DNI')))
        ],
        fiscal_identification_code=[optional(of_type(six.text_type))],
        street_code=[optional(of_type(six.text_type))],
        alias=[optional(of_type(six.text_type))],
        business_name=[optional(of_type(six.text_type))],
        subaccount=[optional(is_subaccount())],
        municipal_code=[optional(is_subaccount())],
        file=[optional(of_type(six.text_type))])
    def create(self,
               country_iso,
               salutation,
               first_name,
               last_name,
               birth_place,
               birth_date,
               nationality,
               id_nationality,
               id_issue_date,
               id_type,
               id_number,
               address_line1,
               address_line2,
               city,
               region,
               postal_code,
               phone_number_country,
               number_type,
               proof_type,
               alias=None,
               business_name=None,
               fiscal_identification_code=None,
               street_code=None,
               municipal_code=None,
               subaccount=None,
               file=None,
               callback_url=None):
        if country_iso == 'ES' and not fiscal_identification_code:
            raise ValidationError(
              'The parameter fiscal_identification_code is required for Spain numbers'
            )

        if country_iso == 'DK' and not all(street_code, municipal_code):
            raise ValidationError(
                'The parameters street_code and municipal_code are required for Denmark numbers'
            )

        if file:
            file_extension = file.strip().split('.')[-1].lower()
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

            # check file should not max than 5
            file_size_in_mb = os.stat(file).st_size / 1000000.0
            if file_size_in_mb > 5:
                raise ValidationError(
                    'File max size should be less than 5 mb.'
                )

            files = {
                'file': (file.split(os.sep)[-1], open(
                    file, 'rb'), content_types[file_extension])
            }
        else:
            files = {'file': ''}
        data_to_send = to_param_dict(self.create, locals())
        return self.client.request(
            'POST', ('Verification', 'Identity'), data_to_send, files=files)

    @validate_args(
        identity_id=[of_type(six.text_type)],
        country_iso=[optional(of_type(six.text_type))],
        salutation=[optional(of_type(six.text_type), is_in(('Mr', 'Ms')))],
        first_name=[optional(of_type(six.text_type))],
        last_name=[optional(of_type(six.text_type))],
        birth_place=[optional(of_type(six.text_type))],
        birth_date=[optional(of_type(six.text_type))],
        nationality=[optional(of_type(six.text_type))],
        id_nationality=[optional(of_type(six.text_type))],
        id_issue_date=[optional(of_type(six.text_type))],
        id_type=[optional(of_type(six.text_type))],
        id_number=[optional(of_type(six.text_type))],
        alias=[optional(of_type(six.text_type))],
        business_name=[optional(of_type(six.text_type))],
        subaccount=[optional(is_subaccount())],
        file=[optional(of_type(six.text_type))],
        address_line1=[optional(of_type(six.text_type))],
        address_line2=[optional(of_type(six.text_type))],
        city=[optional(of_type(six.text_type))],
        region=[optional(of_type(six.text_type))],
        postal_code=[optional(of_type(six.text_type))],
        phone_number_country=[optional(of_type(six.text_type))],
        number_type=[optional(of_type(six.text_type),
                    is_in(("local", "national", "mobile", "tollfree")))
        ],
        proof_type=[
          optional(
              of_type(six.text_type),
              is_in(('national_id', 'passport', 'business_id', 'NIF', 'NIE',
                     'DNI')))
        ],
        fiscal_identification_code=[optional(of_type(six.text_type))],
        street_code=[optional(of_type(six.text_type))],
        municipal_code=[optional(of_type(six.text_type))],
        callback_url=[optional(of_type(six.text_type))])
    def update(self,
               identity_id,
               country_iso=None,
               salutation=None,
               first_name=None,
               last_name=None,
               birth_place=None,
               birth_date=None,
               nationality=None,
               id_nationality=None,
               id_issue_date=None,
               id_type=None,
               id_number=None,
               address_line1=None,
               address_line2=None,
               city=None,
               region=None,
               postal_code=None,
               alias=None,
               business_name=None,
               fiscal_identification_code=None,
               street_code=None,
               municipal_code=None,
               subaccount=None,
               file=None,
               auto_correct_address=None,
               callback_url=None,
               phone_number_country=None,
               number_type=None,
               proof_type=None):

        if file:
            file_extension = file.strip().split('.')[-1].lower()
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

            # check file should not max than 5
            file_size_in_mb = os.stat(file).st_size / 1000000.0
            if file_size_in_mb > 5:
                raise ValidationError(
                    'File max size should be less than 5 mb.'
                )

            files = {
                'file': (file.split(os.sep)[-1], open(
                    file, 'rb'), content_types[file_extension])
            }
        else:
            files = {'file': ''}

        data_to_send = to_param_dict(self.create, locals())
        return self.client.request(
            'POST', ('Verification', 'Identity', identity_id),
            data_to_send,
            files=files)

    @validate_args(identity_id=[of_type(six.text_type)])
    def get(self, identity_id):
        return self.client.request(
            'GET', ('Verification', 'Identity', identity_id),
            response_type=Identity)

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
             limit=20,
             offset=0):
        return self.client.request(
            'GET', ('Verification', 'Identity', ),
            to_param_dict(self.list, locals()),
            response_type=ListResponseObject,
            objects_type=Identity)

    @validate_args(identity_id=[of_type(six.text_type)])
    def delete(self, identity_id):
        return self.client.request('DELETE', ('Verification', 'Identity',
                                              identity_id))
