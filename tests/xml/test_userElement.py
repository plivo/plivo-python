from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class UserElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        expected_response = '<Response><Dial><User sendDigits="wwww2410" sendOnPreanswer="true" ' \
                            'sipHeaders="head1=val1,head2=val2">This is Test</User></Dial></Response>'

        content = 'This is Test'
        send_digits = 'wwww2410'
        send_on_preanswer = True
        sip_headers = 'head1=val1,head2=val2'

        element = plivoxml.ResponseElement()

        response = element.add(
            plivoxml.DialElement().add(
                plivoxml.UserElement(content).set_send_digits(send_digits).set_send_on_preanswer(
                    send_on_preanswer
                ).set_sip_headers(sip_headers)
            )
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)
