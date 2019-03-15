from unittest import TestCase

from plivo import plivoxml


class RedirectElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Redirect method="POST">This is Test</Redirect></Response>'

        method = "POST"
        content = 'This is Test'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.RedirectElement(content).set_method(method)
        ).to_string()

        self.assertEqual(response, expected_response + '\n')
