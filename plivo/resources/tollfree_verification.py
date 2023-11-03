from ..utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface, ListTollfreeVerificationResponseObject
from ..exceptions import *
from ..utils import *


class TollfreeVerification(PlivoResource):
    _name = 'TollfreeVerification'
    _identifier_string = 'uuid'

    def delete(self):
        return self.client.tollfree_verification.delete(tollfree_verification_uuid=self.uuid)

    def update(self,
               profile_uuid=None,
               usecase=None,
               usecase_summary=None,
               message_sample=None,
               optin_image_url=None,
               volume=None,
               additional_information=None,
               extra_data=None,
               optin_type=None,
               callback_url=None,
               callback_method=None):
        return self.client.tollfree_verification.update(self.uuid, profile_uuid=profile_uuid, usecase=usecase,
                                                        usecase_summary=usecase_summary, message_sample=message_sample,
                                                        optin_image_url=optin_image_url, volume=volume,
                                                        additional_information=additional_information,
                                                        extra_data=extra_data, optin_type=optin_type,
                                                        callback_url=callback_url, callback_method=callback_method)

class TollfreeVerifications(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = TollfreeVerification
        super(TollfreeVerifications, self).__init__(client)

    def create(self,
               profile_uuid=None,
               usecase=None,
               usecase_summary=None,
               message_sample=None,
               optin_image_url=None,
               volume=None,
               number=None,
               additional_information=None,
               extra_data=None,
               optin_type=None,
               callback_url=None,
               callback_method=None):
        return self.client.request(
            'POST', ('TollfreeVerification',), to_param_dict(self.create, locals()))

    def get(self, tollfree_verification_uuid=None):
        return self.client.request(
            'GET', ('TollfreeVerification', tollfree_verification_uuid), response_type=TollfreeVerification)

    def list(self,
             number=None,
             status=None,
             profile_uuid=None,
             created__gt=None,
             created__gte=None,
             created__lt=None,
             created__lte=None,
             usecase=None,
             limit=20,
             offset=0):
        return self.client.request(
            'GET', ('TollfreeVerification',), to_param_dict(self.list, locals()),
            objects_type=TollfreeVerification, response_type=ListTollfreeVerificationResponseObject, )

    def update(self, tollfree_verification_uuid=None,
               profile_uuid=None,
               usecase=None,
               usecase_summary=None,
               message_sample=None,
               optin_image_url=None,
               volume=None,
               additional_information=None,
               extra_data=None,
               optin_type=None,
               callback_url=None,
               callback_method=None):
        return self.client.request(
            'POST', ('TollfreeVerification', tollfree_verification_uuid), to_param_dict(self.update, locals()))

    def delete(self, tollfree_verification_uuid=None):
        return self.client.request('DELETE', ('TollfreeVerification', tollfree_verification_uuid))
