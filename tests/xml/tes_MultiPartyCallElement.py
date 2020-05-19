from unittest import TestCase
from plivo import plivoxml
from plivo.exceptions import ValidationError


class MultiPartyCallElementTest(TestCase):

    def test_default_xml(self):

        expected_response = '<MultiPartyCall agentHoldMusicMethod="GET" coachMode="true" ' \
                            'customerHoldMusicMethod="GET" endMpcOnExit="false" enterSound="beep:1" ' \
                            'enterSoundMethod="GET" exitSound="beep:2" exitSoundMethod="GET" hold="false" ' \
                            'maxDuration="14400" maxParticipants="10" mute="false" onExitActionMethod="POST" ' \
                            'record="false" recordFileFormat="mp3" recordingCallbackMethod="POST" ' \
                            'relayDTMFInputs="false" role="agent" startMpcOnEnter="true" ' \
                            'statusCallbackEvents="mpc-state-changes,participant-state-changes" ' \
                            'statusCallbackMethod="POST" stayAlone="false" ' \
                            'waitMusicMethod="GET">Nairobi</MultiPartyCall>'

        element = plivoxml.MultiPartyCallElement(content='Nairobi', role='Agent')
        self.assertEqual(element.to_string(False), expected_response)

    def test_setting_optional_fields(self):
        expected_response = '<MultiPartyCall agentHoldMusicMethod="GET" coachMode="true" ' \
                            'customerHoldMusicMethod="GET" endMpcOnExit="false" enterSound="beep:1" ' \
                            'enterSoundMethod="GET" exitSound="beep:1" exitSoundMethod="GET" hold="false" ' \
                            'maxDuration="14400" maxParticipants="10" mute="false" onExitActionMethod="POST" ' \
                            'record="false" recordFileFormat="mp3" recordingCallbackMethod="POST" ' \
                            'relayDTMFInputs="false" role="supervisor" startMpcOnEnter="true" ' \
                            'statusCallbackEvents="mpc-state-changes,participant-state-changes" ' \
                            'statusCallbackMethod="POST" stayAlone="false" ' \
                            'waitMusicMethod="GET">Tokyo</MultiPartyCall>'

        element = plivoxml.MultiPartyCallElement(content='Tokyo', role='supervisor', exit_sound='beep:1')
        self.assertEqual(element.to_string(False), expected_response)

    def test_validation_on_init(self):
        expected_error = '["status_callback_events should be among (\'mpc-state-changes\', ' \
                         '\'participant-state-changes\', \'participant-speak-events\'). ' \
                         'multiple values should be COMMA(,) separated (actual value: hostages-move)"]'

        actual_error = ''
        try:
            plivoxml.MultiPartyCallElement(content='Rio', role='agent', status_callback_events='hostages-move')
        except ValidationError as e:
            actual_error = str(e)
        self.assertEqual(expected_error, actual_error)

    def test_validation_on_set(self):
        expected_error = "['300 < max_duration <= 28800 (actual value: 255)']"

        element = plivoxml.MultiPartyCallElement(content='Denver', role='Customer')
        actual_error = ''
        try:
            element.set_max_duration(255)
        except ValidationError as e:
            actual_error = str(e)
        self.assertEqual(expected_error, actual_error)
