from unittest import TestCase

from plivo import plivoxml


class HangupElementTest(TestCase):
    def test_set_methods(self):
        schedule = 60
        reason = "rejected"
        expected_response = '<Response><Hangup reason="rejected" schedule="60"></Hangup></Response>'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.HangupElement().set_reason(reason).set_schedule(schedule)
        ).to_string()
        self.assertEqual(response, expected_response + '\n')
