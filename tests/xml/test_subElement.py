from unittest import TestCase

from plivo import plivoxml


class SubElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Speak><Sub alias="World Wide Web Consortium"/></Speak></Response>'
        alias="World Wide Web Consortium"

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SpeakElement("").add(
                plivoxml.SubElement().set_alias(alias)
            )
        ).to_string()
        self.assertEqual(response, expected_response + '\n')
