from plivo.base import (PlivoResource, PlivoResourceInterface)


class EndUser(PlivoResource):
    _name = 'EndUser'
    _identifier_string = 'end_user'


class EndUsers(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = EndUser
        super(EndUsers, self).__init__(client)

    def get(self, end_user_id):
        return self.client.request('GET', ('EndUser', end_user_id), response_type=EndUser)

    def list(self, limit=None, offset=None, name=None, last_name=None, end_user_type=None):
        return self.client.request('GET', ('EndUser',), dict(limit=limit, offset=offset,
                                                             name=name, last_name=last_name, end_user_type=end_user_type))

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

    def list(self, limit=None, offset=None):
        return self.client.request('GET', ('ComplianceDocumentType',), dict(limit=limit, offset=offset))


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

    def list(self, limit=None, offset=None, end_user_id=None, document_type_id=None, alias=None):
        return self.client.request('GET', ('ComplianceDocument',), dict(limit=limit, offset=offset,
                                                                        end_user_id=end_user_id,
                                                                        document_type_id=document_type_id, alias=alias))

    def create(self, end_user_id=None, document_type_id=None, alias=None, file=None, **data_fields):
        payload, files = construct_compliance_document_payload(end_user_id, document_type_id, alias, file, data_fields)
        return self.client.request('POST', ('ComplianceDocument',), payload, files=files)

    def update(self, compliance_document_id=None, end_user_id=None, document_type_id=None, alias=None, file=None,
               **data_fields):
        payload, files = construct_compliance_document_payload(end_user_id, document_type_id, alias, file, data_fields)
        return self.client.request('POST', ('ComplianceDocument', compliance_document_id), payload, files=files)

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

    def list(self, status=None, end_user_type=None, number_type=None, country_iso2=None,
             alias=None, limit=None, offset=None, end_user_id=None):
        return self.client.request('GET', ('ComplianceApplication',),
                                   dict(status=status, end_user_type=end_user_type, number_type=number_type,
                                        country_iso2=country_iso2, alias=alias, limit=limit, offset=offset,
                                        end_user_id=end_user_id), )

    def create(self, compliance_requirement_id=None, end_user_id=None, document_ids=None, alias=None,
               end_user_type=None, country_iso2=None, number_type=None):
        return self.client.request('POST', ('ComplianceApplication',),
                                   dict(compliance_requirement_id=compliance_requirement_id, end_user_id=end_user_id,
                                        alias=alias, document_ids=document_ids, end_user_type=end_user_type,
                                        country_iso2=country_iso2, number_type=number_type))

    def update(self, compliance_application_id=None, document_ids=None):
        return self.client.request('POST', ('ComplianceApplication', compliance_application_id),
                                   dict(document_ids=document_ids))

    def delete(self, compliance_application_id=None):
        return self.client.request('DELETE', ('ComplianceApplication', compliance_application_id))

    def submit(self, compliance_application_id=None):
        return self.client.request('POST', ('ComplianceApplication', compliance_application_id, 'Submit'))


# Helper methods
def construct_compliance_document_payload(end_user_id, document_type_id, alias, file, data_fields):
    payload = dict(end_user_id=end_user_id, document_type_id=document_type_id, alias=alias)
    for key, value in data_fields.items():
        payload.update({key: value})
    files = {'file': ''}
    if file:
        files = {'file': open(file, 'rb')}
    return payload, files
