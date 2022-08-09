from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

class ProfileTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        response = self.client.profile.create( 
                profile_alias="profile name sample",
                customer_type="DIRECT",
                entity_type="PRIVATE",
                company_name="ABC Inc.",
                ein="123456789",
                ein_issuing_country="US",
                stock_symbol="ABC",
                stock_exchange="NSE",
                website="www.example.com",
                vertical="REAL_ESTATE",
                alt_business_id="",
                alt_business_id_type="NONE",
                plivo_subaccount="123433566",
                address={
                    "street": "123",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10001",
                    "country": "US"
                },
                authorized_contact={
                    "first_name": "john",
                    "last_name": "con",
                    "phone": "1876865565",
                    "email": "xyz@plivo.com",
                    "title": "con",
                    "seniority": "admin"
                }
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
        response = self.client.profile.list()
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