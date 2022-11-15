from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

class BrandTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        response = self.client.brand.create( 
                brand_alias = "brand name sample",
                brand_type="STARTER",
                profile_uuid="201faedc-7df9-4840-9ab1-3997ce3f7cf4",
                secondary_vetting=False,
                url="http://example.come/test",
                method="POST")
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
        res = self.client.brand.list(limit=2, offset=0)
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertGreater(len(list(res.brands)), 0)
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/10dlc/Brand/?limit=2&offset=0',
            self.client.current_request.url)
        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_get_usecases(self):
        response = self.client.brand.get_usecases(brand_id='BRPXS6E')
        self.client.set_expected_response(
            status_code=202, data_to_return=response)
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/10dlc/Brand/BRPXS6E/usecases/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_delete(self):
        response = self.client.brand.get(brand_id='BRPXS6E')
        self.client.set_expected_response(
            status_code=202, data_to_return=response)
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/10dlc/Brand/BRPXS6E/',
            self.client.current_request.url)
        
        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)
