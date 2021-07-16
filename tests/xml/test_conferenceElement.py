from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class ConferenceElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        expected_response = '<Response><Conference action="http://foo.com/get_recording/" callbackMethod="GET"' \
                            ' callbackUrl="http://foo.com/sms_status/" digitsMatch="#0,99,000"' \
                            ' endConferenceOnExit="true" enterSound="" exitSound="beep:1" floorEvent="true"' \
                            ' hangupOnStar="true" maxMembers="100" method="GET" muted="false" record="true"' \
                            ' recordFileFormat="mp3" recordWhenAlone="" redirect="true" relayDTMF="true"' \
                            ' sendDigits="wwww2410" startConferenceOnEnter="true" stayAlone="true" timeLimit="600"' \
                            ' transcriptionMethod="POST" transcriptionType="auto"' \
                            ' transcriptionUrl="http://www.foo.com/waitmusic/"' \
                            ' waitSound="http://www.foo.com/waitmusic/"/></Response>'
        muted = False
        enter_sound = ""
        exit_sound = "beep:1"
        start_conference_on_enter = True
        end_conference_on_exit = True
        stay_alone = True
        wait_sound = "http://www.foo.com/waitmusic/"
        max_members = 100
        record = True
        record_file_format = "mp3"
        time_limit = 600
        hangup_on_star = True
        action = "http://foo.com/get_recording/"
        method = "GET"
        callback_url = "http://foo.com/sms_status/"
        callback_method = "GET"
        digits_match = "#0,99,000"
        floor_event = True
        redirect = True
        relay_dtmf = True
        send_digits = "wwww2410"
        record_when_alone = ""
        transcription_type = "auto"
        transcription_url = "http://www.foo.com/waitmusic/"
        transcription_method = "POST"

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.ConferenceElement().set_muted(
                muted
            ).set_enter_sound(
                enter_sound
            ).set_exit_sound(
                exit_sound
            ).set_start_conference_on_enter(
                start_conference_on_enter
            ).set_end_conference_on_exit(
                end_conference_on_exit
            ).set_stay_alone(
                stay_alone
            ).set_wait_sound(
                wait_sound
            ).set_max_members(
                max_members
            ).set_record(
                record
            ).set_record_file_format(
                record_file_format
            ).set_time_limit(
                time_limit
            ).set_hangup_on_star(
                hangup_on_star
            ).set_action(
                action
            ).set_method(
                method
            ).set_callback_url(
                callback_url
            ).set_callback_method(
                callback_method
            ).set_digits_match(
                digits_match
            ).set_floor_event(
                floor_event
            ).set_redirect(
                redirect
            ).set_relay_dtmf(
                relay_dtmf
            ).set_send_digits(
                send_digits
            ).set_record_when_alone(
                record_when_alone
            ).set_transcription_type(
                transcription_type
            ).set_transcription_url(
                transcription_url
            ).set_transcription_method(
                transcription_method
            )
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)
