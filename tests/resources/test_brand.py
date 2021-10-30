from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

class BrandTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        response = self.client.brand.create( alt_business_id_type = "GIIN",
                alt_business_id = "111",
                city = "New York",
                company_name = "ABC Inc.",
                country = "US",
                ein = "111111111",
                ein_issuing_country = "US",
                email = "johndoe@abc.com",
                entity_type = "PRIVATE_PROFIT",
                first_name = "John",
                last_name = "Doe",
                phone = "+11234567890",
                postal_code = "10001",
                registration_status = "PENDING",
                state = "NY",
                stock_exchange = "NASDAQ",
                stock_symbol = "ABC",
                street = "123",
                vertical = "RETAIL",
                website = "http://www.abcmobile.com")
        self.assertEqual('POST', self.client.current_request.method)
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/10dlc/Brand/',
            self.client.current_request.url)

    @with_response(200)
    def test_get(self):
        response = self.client.brand.get(brand_id='BRPXS6E')
        self.client.set_expected_response(
            status_code=202, data_to_return=response)
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/10dlc/Brand/BRPXS6E/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_list(self):
        res = self.client.brand.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertGreater(len(list(res.brands)), 0)
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/10dlc/Brand/',
            self.client.current_request.url)
        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)