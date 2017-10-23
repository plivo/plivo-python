# -*- coding: utf-8 -*-

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class PricingTest(PlivoResourceTestCase):
    def test_pricing_get_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.pricing.get('USA')

    @with_response(200)
    def test_get(self):
        us_pricing = self.client.pricing.get('US')
        self.assertResponseMatches(
            us_pricing, )

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Pricing/?country_iso=US',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying the object type returned
        self.assertEqual(plivo.resources.pricings.Pricing,
                         us_pricing.__class__)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('US', us_pricing.id)
