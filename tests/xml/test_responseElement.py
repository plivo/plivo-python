# -*- coding: utf-8 -*-

from unittest import TestCase

from plivo import plivoxml


class ResponseElementTest(TestCase):
    def test_create_response(self):
        self.assertEqual(plivoxml.ResponseElement().to_string(False),
                         '<Response/>')

    def test_add_conference(self):
        content = 'test'
        elem = plivoxml.ResponseElement().add_conference(
            content=content).to_string(False)
        self.assertEqual(
            elem, '<Response><Conference>test</Conference></Response>')

    def test_add_dial(self):
        time = 2
        elem = plivoxml.ResponseElement().add_dial(time_limit=time).to_string(False)
        self.assertEqual(elem,
                         '<Response><Dial timeLimit="2"/></Response>')

    def test_add_dtmf(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_dtmf(content=content).to_string(False)
        self.assertEqual(elem, '<Response><DTMF>dummy</DTMF></Response>')

    def test_add_get_digits(self):
        content = 2
        elem = plivoxml.ResponseElement().add_get_digits(
            timeout=content).to_string(False)
        self.assertEqual(
            elem, '<Response><GetDigits timeout="2"/></Response>')

    def test_add_get_input(self):
        content = 2
        elem = plivoxml.ResponseElement().add_get_input(
            execution_timeout=content).to_string(False)
        self.assertEqual(
            elem, '<Response><GetInput executionTimeout="2"/></Response>')

    def test_add_hangup(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_hangup(
            reason=content).to_string(False)
        self.assertEqual(
            elem, '<Response><Hangup reason="dummy"/></Response>')

    def test_add_message(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_message(
            content=content).to_string(False)
        self.assertEqual(elem,
                         '<Response><Message>dummy</Message></Response>')

    def test_add_play(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_play(content=content).to_string(False)
        self.assertEqual(elem, '<Response><Play>dummy</Play></Response>')

    def test_add_pre_answer(self):
        elem = plivoxml.ResponseElement().add_pre_answer().to_string(False)
        self.assertEqual(elem,
                         '<Response><PreAnswer/></Response>')

    def test_add_record(self):
        action = 'https://foo.example.com'
        elem = plivoxml.ResponseElement().add_record(action=action).to_string(False)
        expected_response = '<Response><Record action="https://foo.example.com"/></Response>'
        self.assertEqual(elem, expected_response)

    def test_add_redirect(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_redirect(
            content=content).to_string(False)
        self.assertEqual(elem,
                         '<Response><Redirect>dummy</Redirect></Response>')

    def test_add_speak(self):
        response = plivoxml.ResponseElement()
        response.add(
            plivoxml.SpeakElement(
                'Please leave a message after the beep. Press the star key when done.'
            ))
        response.add(
            plivoxml.RecordElement(
                action='http://foo.com/get_recording/',
                max_length=30,
                finish_on_key='*'))
        response.add(plivoxml.SpeakElement('Recording not received.'))
        elem = response.to_string(False)
        self.assertEqual(
            elem,
            '<Response><Speak>Please leave a message after the beep. Press the star key when done.</Speak><Record action="http://foo.com/get_recording/" finishOnKey="*" maxLength="30"/><Speak>Recording not received.</Speak></Response>'
        )

    def test_add_wait(self):
        content = 2
        elem = plivoxml.ResponseElement().add_wait(length=content).to_string(False)
        self.assertEqual(elem,
                         '<Response><Wait length="2"/></Response>')

    def test_add_mpc(self):

        expected_xml = '<Response><MultiPartyCall agentHoldMusicMethod="GET" coachMode="true" ' \
                       'customerHoldMusicMethod="GET" endMpcOnExit="false" enterSound="beep:2" ' \
                       'enterSoundMethod="GET" exitSound="beep:1" exitSoundMethod="GET" hold="true" ' \
                       'maxDuration="20000" maxParticipants="7" mute="true" onExitActionMethod="POST" ' \
                       'onExitActionUrl="https://plivo.com/exitAction" record="true" recordFileFormat="wav" ' \
                       'recordingCallbackMethod="GET" relayDTMFInputs="false" role="customer" ' \
                       'startMpcOnEnter="true" statusCallbackEvents="mpc-state-changes,participant-state-changes" ' \
                       'statusCallbackMethod="GET" stayAlone="false" waitMusicMethod="POST" ' \
                       'waitMusicUrl="https://plivo.com/plivoTone.mp3">multi party conference</MultiPartyCall>' \
                       '</Response>'

        elem = plivoxml.ResponseElement().add_multi_party_call(content='multi party conference', role='customer',
                                                               max_duration=20000, max_participants=7,
                                                               wait_music_url='https://plivo.com/plivoTone.mp3',
                                                               wait_music_method='POST', start_mpc_on_enter=True,
                                                               record=True, record_file_format='wav', mute=True,
                                                               enter_sound='beep:2', exit_sound='beep:1', hold=True,
                                                               on_exit_action_url='https://plivo.com/exitAction')
        self.assertEqual(expected_xml, elem.to_string(False))
