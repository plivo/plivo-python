from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class StreamElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        expected_response = '<Response>' \
                            '<Stream bidirectional="true">wss://test.url</Stream>' \
                            '</Response>'

        content = 'wss://test.url'
        bidirectional = True

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.StreamElement(content, bidirectional=bidirectional)
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)