from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

class ProfileTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        response = self.client.profile.create( 
                profile_alias="Test Profile",
                customer_type="DIRECT",
                entity_type="PUBLIC",
                company_name="Test Company Inc",
                ein="12-3456789",
                ein_issuing_country="US",
                stock_symbol="TEST",
                stock_exchange="NASDAQ",
                website="https://testcompany.com",
                vertical="TECHNOLOGY",
                alt_business_id="",
                alt_business_id_type="NONE",
                plivo_subaccount="",
                address={
                    "street": "123 Main Street",
                    "city": "San Francisco",
                    "state": "CA",
                    "postal_code": "94105",
                    "country": "US"
                },
                authorized_contact={
                    "first_name": "John",
                    "last_name": "Doe",
                    "phone": "+14155551234",
                    "email": "test@example.com",
                    "title": "CEO",
                    "seniority": "C_LEVEL"
                },
                business_contact_email="employee@company.com"
        )
        self.assertEqual('POST', self.client.current_request.method)
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Profile/',
            self.client.current_request.url)

    @with_response(200)
    def test_get(self):
        response = self.client.profile.get(profile_uuid='201faedc-7df9-4840-9ab1-3997ce3f7cf4')
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Profile/201faedc-7df9-4840-9ab1-3997ce3f7cf4/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)


    @with_response(200)
    def test_list(self):
        response = self.client.profile.list(limit=20, offset=0)
        # Verifying the endpoint hit
        self.assertEqual(len(list(response.profiles)), 10)
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(200)
    def test_delete(self):
        response = self.client.profile.delete(profile_uuid='201faedc-7df9-4840-9ab1-3997ce3f7cf4')
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Profile/201faedc-7df9-4840-9ab1-3997ce3f7cf4/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)

    @with_response(200)
    def test_update(self):
        param = {'company_name': 'google'}
        response = self.client.profile.update(profile_uuid='09322f43-fe16-4525-b8e4-4229c867795d', params=param)
        # Verifying the endpoint hit
        print(self.client.current_request.url)
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Profile/09322f43-fe16-4525-b8e4-4229c867795d/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)