from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class HangupElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        schedule = 60
        reason = "rejected"
        expected_response = '<Response><Hangup reason="rejected" schedule="60"/></Response>'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.HangupElement().set_reason(reason).set_schedule(schedule)
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)
