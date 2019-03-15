from unittest import TestCase

from plivo import plivoxml


class ElementTest(TestCase):
    def test_set_methods(self):
        alphabet = "ipa"
        ph = "t&#x259;mei&#x325;&#x27E;ou&#x325;"
        expected_response = '<Response><Phoneme alphabet="ipa" ph="t&amp;#x259;mei&amp;' \
                            '#x325;&amp;#x27E;ou&amp;#x325;"/></Response>'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.PhonemeElement().set_alphabet(alphabet).set_ph(ph)
        ).to_string()
        self.assertEqual(response, expected_response + '\n')
