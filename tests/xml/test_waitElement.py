from unittest import TestCase

from plivo import plivoxml


class WaitElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Wait beep="true" length="1" minSilence="1" silence="true"></Wait></Response>'

        length = 1
        silence = True
        min_silence = 1
        beep = True

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.WaitElement().set_length(length).set_silence(
                silence
            ).set_min_silence(min_silence).set_beep(beep)
        ).to_string()
        
        self.assertEqual(response, expected_response + '\n')
