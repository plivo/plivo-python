from unittest import TestCase

from plivo import plivoxml


class SayAsElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Speak><say-as format="application/ssml+xml" interpret-as="spell-out">' \
                            'This is Test</say-as></Speak></Response>'
        interpret_as = "spell-out"
        format = "application/ssml+xml"
        content = 'This is Test'

        element = plivoxml.ResponseElement()

        response = element.add(
            plivoxml.SpeakElement("").add(
                plivoxml.SayAsElement(content).set_interpret_as(interpret_as).set_format(format)
            )
        ).to_string(False)

        self.assertEqual(response, expected_response)
