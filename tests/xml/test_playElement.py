from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class PlayElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        expected_response = '<Response><Play loop="1">This is test</Play></Response>'

        loop = 1
        content = 'This is test'
        element = plivoxml.ResponseElement()

        response = element.add(
            plivoxml.PlayElement(content).set_loop(loop)
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)
