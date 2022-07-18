from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

class ProfileTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        response = self.client.profile.create(originator="xxxxx", 
                profile_alias="yyyyy",
               customer_type="DIRECT",
               entity_type="PRIVATE",
               company_name="plivo",
               ein="ghdwgdjwbdkjdw",
               ein_issuing_country="US",
               stock_symbol="jgasjdgja",
               stock_exchange="AMEX",
               website="www.example.com",
               vertical="REAL_ESTATE",
               alt_business_id="uyqgugdqw",
               alt_business_id_type="jhjadada",
               plivo_subaccount="123433566",
               address={
                "street": "jhjhja",
                "city": "New York",
                "state": "Califernia",
                "postal_code": "6575",
                "country": "US"
               },
               authorized_contact={
                "first_name": "john",
                "last_name": "con",
                "phone": "1876865565",
                "email": "xyz@plivo.com",
                "title": "ugigwc",
                "seniority": "jsgfjs"
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
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Profile/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_delete(self):
        response = self.client.profile.delete(profile_uuid='201faedc-7df9-4840-9ab1-3997ce3f7cf4')
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Profile/201faedc-7df9-4840-9ab1-3997ce3f7cf4/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)