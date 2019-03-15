from unittest import TestCase

from plivo import plivoxml


class SayAsElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><SayAs format="application/ssml+xml" interpret_as="spell-out">This is Test</SayAs></Response>'
        interpret_as = "spell-out"
        format = "application/ssml+xml"
        content = 'This is Test'
        
        element = plivoxml.ResponseElement()
        
        response = element.add(
            plivoxml.SayAsElement(content).set_interpret_as(interpret_as).set_format(format)
        ).to_string()
        
        self.assertEqual(response, expected_response + '\n')
