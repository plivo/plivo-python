import os
from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface, ResponseObject)
from plivo.exceptions import ValidationError


class EndUser(PlivoResource):
    _name = 'EndUser'
    _identifier_string = 'end_user'


class EndUsers(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = EndUser
        super(EndUsers, self).__init__(client)

    def get(self, end_user_id):
        return self.client.request('GET', ('EndUser', end_user_id), response_type=EndUser)

    def list(self, limit=20, offset=0):
        return self.client.request('GET', ('EndUser',), dict(limit=limit, offset=offset))

    def create(self, name=None, last_name=None, end_user_type=None):
        return self.client.request('POST', ('EndUser',),
                                   dict(name=name, last_name=last_name, end_user_type=end_user_type))

    def update(self, end_user_id=None, last_name=None, name=None, end_user_type=None):
        return self.client.request('POST', ('EndUser', end_user_id),
                                   dict(name=name, last_name=last_name, end_user_type=end_user_type))

    def delete(self, end_user_id=None):
        return self.client.request('DELETE', ('EndUser', end_user_id))


class ComplianceDocumentType(PlivoResource):
    _name = 'ComplianceDocumentType'
    _identifier_string = 'compliance_document_type'


class ComplianceDocumentTypes(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = EndUser
        super(ComplianceDocumentTypes, self).__init__(client)

    def get(self, doc_id):
        return self.client.request('GET', ('ComplianceDocumentType', doc_id), response_type=ComplianceDocumentType)

    def list(self, limit=20, offset=0):
        return self.client.request('GET', ('ComplianceDocumentType',), dict(limit=limit, offset=offset),
                                   objects_type=ComplianceDocumentType,
                                   response_type=ListResponseObject, )


class ComplianceDocument(PlivoResource):
    _name = 'ComplianceDocument'
    _identifier_string = 'compliance_document'


class ComplianceDocuments(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = EndUser
        super(ComplianceDocuments, self).__init__(client)

    def get(self, compliance_document_id):
        return self.client.request('GET', ('ComplianceDocument', compliance_document_id),
                                   response_type=ComplianceDocument)

    def list(self, limit=20, offset=0):
        return self.client.request('GET', ('ComplianceDocument',), dict(limit=limit, offset=offset),
                                   objects_type=ComplianceDocument, response_type=ListResponseObject, )

    def create(self, end_user_id=None, document_type_id=None, alias=None, file_to_upload=None):

        return self.client.request('POST', ('ComplianceDocument',),
                                   dict(end_user_id=end_user_id, document_type_id=document_type_id, alias=alias),
                                   files={})

    def update(self, compliance_document_id=None, end_user_id=None, document_type_id=None, alias=None,
               file_to_upload=None):
        if file_to_upload:
            file_extension = file_to_upload.strip().split('.')[-1].lower()
            files = {
                'file': (file_to_upload.split(os.sep)[-1], open(file_to_upload, 'rb'),)
            }
        else:
            files = {'file': ''}
        return self.client.request('POST', ('ComplianceDocument', compliance_document_id),
                                   dict(end_user_id=end_user_id, document_type_id=document_type_id, alias=alias),
                                   files=files)

    def delete(self, compliance_document_id=None):
        return self.client.request('DELETE', ('ComplianceDocument', compliance_document_id))


class ComplianceRequirement(PlivoResource):
    _name = 'ComplianceRequirement'
    _identifier_string = 'compliance_requirement'


class ComplianceRequirements(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = ComplianceRequirement
        super(ComplianceRequirements, self).__init__(client)

    def get(self, compliance_requirement_id):
        return self.client.request('GET', ('ComplianceRequirement', compliance_requirement_id),
                                   response_type=ComplianceRequirement)

    def list(self, country_iso2=None, number_type=None, end_user_type=None, phone_number=None):
        return self.client.request('GET', ('ComplianceRequirement',),
                                   dict(country_iso2=country_iso2, number_type=number_type,
                                        end_user_type=end_user_type, phone_number=phone_number), )


class ComplianceApplication(PlivoResource):
    _name = 'ComplianceApplication'
    _identifier_string = 'compliance_application'


class ComplianceApplications(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = EndUser
        super(ComplianceApplications, self).__init__(client)

    def get(self, compliance_application_id):
        return self.client.request('GET', ('ComplianceApplication', compliance_application_id),
                                   response_type=ComplianceApplication)

    def list(self, limit=20, offset=0, alias=None):
        return self.client.request('GET', ('ComplianceApplication',), dict(limit=limit, offset=offset, alias=alias),
                                   objects_type=ComplianceApplication, response_type=ListResponseObject, )

    def create(self, compliance_requirement_id=None, end_user_id=None, document_ids=None, alias=None):
        return self.client.request('POST', ('ComplianceDocument',),
                                   dict(compliance_requirement_id=compliance_requirement_id, end_user_id=end_user_id,
                                        alias=alias, document_ids=document_ids))

    def update(self, compliance_application_id=None, compliance_requirement_id=None, end_user_id=None,
               document_ids=None, alias=None):
        return self.client.request('POST', ('ComplianceApplication', compliance_application_id),
                                   dict(compliance_requirement_id=compliance_requirement_id, end_user_id=end_user_id,
                                        alias=alias, document_ids=document_ids))

    def delete(self, compliance_application_id=None):
        return self.client.request('DELETE', ('ComplianceApplication', compliance_application_id))

    def submit(self, compliance_application_id=None):
        return self.client.request('POST', ('ComplianceApplication', compliance_application_id, 'Submit'))
