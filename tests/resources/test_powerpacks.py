from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class PowerpackTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create_powerpack(self):
        response = self.client.powerpacks.create(name='hello_ppk_test', sticky_sender=True)
        self.assertEqual('POST', self.client.current_request.method)
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Powerpack/',
            self.client.current_request.url)

    @with_response(200)
    def test_get_powerpack(self):
        response = self.client.powerpacks.get(uuid='5ec4c8c9-cd74-42b5-9e41-0d7670d6bb46')
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Powerpack/5ec4c8c9-cd74-42b5-9e41-0d7670d6bb46/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_list_powerpack(self):
        powerpacks = self.client.powerpacks.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertGreater(len(list(powerpacks)), 0)
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Powerpack/',
            self.client.current_request.url)
        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_update_powerpack(self):
        params = {}
        params['name'] = 'test'
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        response= powerpack.update(params)
        self.assertEqual(params['name'], response['name'])
    
    @with_response(200)
    def test_delete_powerpack(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        response = powerpack.delete()
        self.assertEqual('DELETE', self.client.current_request.method)

    @with_response(200)
    def test_list_numbers(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        numberpoolnumber = powerpack.list_numbers()
        #response= powerpack.numberpool.numbers.list( )
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(numberpoolnumber)), 3)
        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/NumberPool/d35f2e82-d387-427f-8594-6fa07613c43a/Number/',
            self.client.current_request.url)
        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_count_numbers(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        #count= powerpack.numberpool.numbers.count( )
        count = powerpack.count_numbers()
        self.assertEqual(6, count)

    @with_response(200)
    def test_add_number(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        response = powerpack.add_number(number='15799140336')
        #response= powerpack.numberpool.numbers.add( number='15799140336')
        self.assertEqual('POST', self.client.current_request.method)
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/NumberPool/ca5fd1f2-26c0-43e9-a7e4-0dc426e9dd2f/Number/15799140336/',
            self.client.current_request.url)

    @with_response(200)
    def test_add_tollfree(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        response = powerpack.add_tollfree(tollfree='18772209942')
        #response= powerpack.numberpool.numbers.add( number='18772209942')
        self.assertEqual('POST', self.client.current_request.method)
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/NumberPool/ca5fd1f2-26c0-43e9-a7e4-0dc426e9dd2f/Tollfree/18772209942/',
            self.client.current_request.url)

    @with_response(200)
    def test_remove_number(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        response= powerpack.remove_number( number='15799140336')
        #response= powerpack.numberpool.numbers.remove( number='15799140336')
        self.assertEqual('DELETE', self.client.current_request.method)

    @with_response(200)
    def test_remove_tollfree(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        response= powerpack.remove_tollfree( tollfree='18772209942')
        #response= powerpack.numberpool.tollfree.remove( number='18772209942')
        self.assertEqual('DELETE', self.client.current_request.method)

    @with_response(200)
    def test_remove_shortcode(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        response= powerpack.remove_shortcode( shortcode='333333')
        #response= powerpack.numberpool.shortcode.remove( number='333333')
        self.assertEqual('DELETE', self.client.current_request.method)

    @with_response(200)
    def test_list_shortcode(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        shortcodes = powerpack.list_shortcodes()
       # shortcodes = powerpack.numberpool.shortcodes.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(shortcodes)), 1)

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/NumberPool/ca5fd1f2-26c0-43e9-a7e4-0dc426e9dd2f/Shortcode/?limit=20&offset=0',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_list_tollfree(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        tollfree = powerpack.list_tollfree()
       # shortcodes = powerpack.numberpool.shortcodes.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(tollfree)), 1)

        print(self.client.current_request.url)

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/NumberPool/ca5fd1f2-26c0-43e9-a7e4-0dc426e9dd2f/Tollfree/?limit=20&offset=0',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)
    @with_response(200)
    def test_find_shortcode(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        # response = powerpack.numberpool.shortcodes.find( shortcode='444444')
        response = powerpack.find_shortcode(shortcode='444444')
        self.assertEqual('444444', response['objects'][0]['shortcode'])

    @with_response(200)
    def test_find_tollfree(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        # response = powerpack.numberpool.shortcodes.find( shortcode='444444')
        response = powerpack.find_tollfree(tollfree='18772209942')
        self.assertEqual('18772209942', response['objects'][0]['tollfree'])

    @with_response(200)
    def test_buy_and_number(self):
        powerpack = self.client.powerpacks.get(uuid='d35f2e82-d387-427f-8594-6fa07613c43a')
        # response = powerpack.numberpool.numbers.buy_add_number( number='14845071864')
        response = powerpack.buy_add_number(number='14845071864')
        self.assertEqual('POST', self.client.current_request.method)
        self.assertEqual('14845071864', response['number'])

