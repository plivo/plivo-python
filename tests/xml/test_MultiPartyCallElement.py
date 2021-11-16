from unittest import TestCase
from plivo import plivoxml
from plivo.exceptions import ValidationError
from tests import PlivoXmlTestCase


class MultiPartyCallElementTest(TestCase, PlivoXmlTestCase):

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
        self.assertXmlEqual(element.to_string(False), expected_response)

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
        self.assertXmlEqual(element.to_string(False), expected_response)

    def test_validation_on_init(self):
        expected_error = '["status_callback_events should be among (\'mpc-state-changes\', ' \
                         '\'participant-state-changes\', \'participant-speak-events\', ' \
                         '\'participant-digit-input-events\', \'add-participant-api-events\'). ' \
                         'multiple values should be COMMA(,) separated (actual value: hostages-move)"]'

        actual_error = ''
        try:
            plivoxml.MultiPartyCallElement(content='Rio', role='agent', status_callback_events='hostages-move')
        except ValidationError as e:
            actual_error = str(e)
        self.assertXmlEqual(expected_error, actual_error)

    def test_validation_on_set(self):
        expected_error = "['300 <= max_duration <= 28800 (actual value: 255)']"

        element = plivoxml.MultiPartyCallElement(content='Denver', role='Customer')
        actual_error = ''
        try:
            element.set_max_duration(255)
        except ValidationError as e:
            actual_error = str(e)
        self.assertXmlEqual(expected_error, actual_error)

    def test_builder_setting(self):

        expected_xml = '<MultiPartyCall agentHoldMusicMethod="GET" coachMode="false" customerHoldMusicMethod="GET" ' \
                       'customerHoldMusicUrl="http://plivo.com/voice.mp3" endMpcOnExit="true" enterSound="beep:1" ' \
                       'enterSoundMethod="GET" exitSound="beep:2" exitSoundMethod="GET" hold="false" ' \
                       'maxDuration="4500" maxParticipants="9" mute="false" onExitActionMethod="GET" ' \
                       'onExitActionUrl="http://plivo.com/api.mp3" record="false" recordFileFormat="mp3" ' \
                       'recordingCallbackMethod="POST" relayDTMFInputs="false" role="customer" ' \
                       'startMpcOnEnter="true" ' \
                       'statusCallbackEvents="mpc-state-changes,participant-state-changes" ' \
                       'statusCallbackMethod="POST" stayAlone="false" ' \
                       'waitMusicMethod="GET">Helsinki</MultiPartyCall> '
        element = plivoxml.MultiPartyCallElement(content='Helsinki', role='customer'). \
            set_max_duration(4500).set_max_participants(9).set_end_mpc_on_exit(True). \
            set_customer_hold_music_url('http://plivo.com/voice.mp3').set_coach_mode(False). \
            set_on_exit_action_url('http://plivo.com/api.mp3').set_on_exit_action_method('GET')

        self.assertXmlEqual(expected_xml, element.to_string(False))
