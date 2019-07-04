from unittest import TestCase

from plivo import plivoxml


class NumberElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Dial><Number sendDigits="wwww2410" sendDigitsMode=""' \
                            ' sendOnPreanswer="true">This is Test</Number></Dial></Response>'

        content = 'This is Test'
        send_digits = 'wwww2410'
        send_on_preanswer = True
        send_digits_mode = ""

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.DialElement().add(
                plivoxml.NumberElement(content).set_send_digits(send_digits).set_send_on_preanswer(
                    send_on_preanswer
                ).set_send_digits_mode(
                    send_digits_mode
                )
            )
        ).to_string(False)
        self.assertEqual(response, expected_response)
