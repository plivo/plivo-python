from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class ElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        alphabet = "ipa"
        ph = "t&#x259;mei&#x325;&#x27E;ou&#x325;"
        expected_response = '<Response><Speak><phoneme alphabet="ipa" ph="t&amp;#x259;mei&amp;' \
                            '#x325;&amp;#x27E;ou&amp;#x325;">Well</phoneme></Speak></Response>'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SpeakElement("").add(
                plivoxml.PhonemeElement("Well").set_alphabet(alphabet).set_ph(ph)
            )
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)
