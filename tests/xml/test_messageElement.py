from unittest import TestCase

from plivo import plivoxml


class MessageElementTest(TestCase):
    def test_set_methods(self):

        expected_response = '<Response><Message callbackMethod="GET" callbackUrl="http://foo.example.com" ' \
                            'dst="1203443444&lt;1203443445" src="1202322222" type="sms">this is test</Message>' \
                            '</Response>'
        src = '1202322222'
        dst = '1203443444<1203443445'
        type = 'sms'
        callbackUrl = 'http://foo.example.com'
        callbackMethod = 'GET'
        content = 'this is test'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.MessageElement(content).set_src(src).set_dst(dst)
            .set_type(type).set_callback_url(callbackUrl).set_callback_method(
                callbackMethod)).to_string()
        self.assertEqual(response, expected_response + '\n')
