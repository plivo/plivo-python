from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.utils import to_param_dict


class VerifyCallerid(PlivoResource):
    _name = 'VerifyCallerid'

    def initiate_verify(self):
        return self.client.calls.initiate_verify(self.id,
                                                 **to_param_dict(self.initiate_verify(), locals()))

    def verify_caller_id(self):
        return self.client.calls.verify_caller_id(self.id,
                                                  **to_param_dict(self.verify_caller_id(), locals()))

    def delete_verified_caller_id(self):
        return self.client.calls.delete_verified_caller_id(self.id,
                                                           **to_param_dict(self.delete_verified_caller_id(), locals()))

    def get_verified_caller_id(self):
        return self.client.calls.get_verified_caller_id(self.id,
                                                        **to_param_dict(self.get_verified_caller_id(), locals()))

    def update_verified_caller_id(self):
        return self.client.calls.update_verified_caller_id(self.id,
                                                           **to_param_dict(self.update_verified_caller_id(), locals()))

    def list_verified_caller_id(self):
        return self.client.calls.list_verified_caller_id(self.id,
                                                         **to_param_dict(self.list_verified_caller_id(), locals()))


class VerifyCallerids(PlivoResourceInterface):
    _resource_type = VerifyCallerid

    def initiate_verify(self,
                        phone_number=None,
                        alias=None,
                        channel=None,
                        country=None,
                        subaccount=None,
                        account_id=None,
                        auth_id=None,
                        auth_token=None
                        ):
        return self.client.request('POST', ('VerifiedCallerId',),
                                   to_param_dict(self.initiate_verify, locals()), is_voice_request=True)

    def verify_caller_id(self,
                         verification_uuid,
                         otp=None,
                         ):
        return self.client.request('POST', ('VerifiedCallerId', 'Verification', verification_uuid),
                                   to_param_dict(self.verify_caller_id, locals()), is_voice_request=True)

    def delete_verified_caller_id(self,
                                  phone_number
                                  ):
        return self.client.request('DELETE', ('VerifiedCallerId', phone_number),
                                   to_param_dict(self.delete_verified_caller_id, locals()), is_voice_request=True)

    def get_verified_caller_id(self,
                               phone_number
                               ):
        return self.client.request('GET', ('VerifiedCallerId', phone_number), is_voice_request=True)

    def update_verified_caller_id(self,
                                  phone_number,
                                  alias=None,
                                  subaccount=None
                                  ):
        return self.client.request('POST', ('VerifiedCallerId', phone_number),
                                   to_param_dict(self.update_verified_caller_id, locals()), is_voice_request=True)

    def list_verified_caller_id(self,
                                country=None,
                                subaccount=None,
                                alias=None,
                                limit=None,
                                offset=None
                                ):
        return self.client.request('GET', ('VerifiedCallerId',), to_param_dict(self.list_verified_caller_id, locals()),
                                   is_voice_request=True)
