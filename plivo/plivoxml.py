# -*- coding: utf-8 -*-
from lxml import etree
import six
from .exceptions import PlivoXMLError


def map_type(val):
    if isinstance(val, bool):
        return six.text_type(val).lower()
    return six.text_type(val)


class PlivoXMLElement(object):
    def __init__(self):
        self.content = ''
        self.children = []

    def add(self, element):
        if not isinstance(element, PlivoXMLElement):
            raise PlivoXMLError('element must be a PlivoXMLElement')

        if element._name not in self._nestable:
            raise PlivoXMLError(
                '{} is not nestable in {} (allowed: {})'.format(
                    element._name, self._name, self._nestable))

        self.children.append(element)
        return self

    def to_string(self):
        s = etree.tostring(self._to_element(), pretty_print=True)
        return s.decode('utf-8')

    def _to_element(self, parent=None):
        e = etree.SubElement(
            parent, self._name,
            **self.to_dict()) if parent is not None else etree.Element(
                self._name, **self.to_dict())
        e.text = self.content
        for child in self.children:
            child._to_element(parent=e)
        return e


class ResponseElement(PlivoXMLElement):
    _name = 'Response'
    _nestable = [
        'Conference', 'Dial', 'Number', 'User', 'DTMF', 'GetDigits', 'Hangup',
        'Message', 'Play', 'PreAnswer', 'Record', 'Redirect', 'Speak', 'Wait'
    ]

    def add_conference(
            self,
            content,
            muted=None,
            enter_sound=None,
            exit_sound=None,
            start_conference_on_enter=None,
            end_conference_on_exit=None,
            stay_alone=None,
            wait_sound=None,
            max_members=None,
            record=None,
            record_file_format=None,
            time_limit=None,
            hangup_on_star=None,
            action=None,
            method=None,
            callback_url=None,
            callback_method=None,
            digits_match=None,
            floor_event=None,
            redirect=None,
            relay_dtmf=None, ):
        self.add(
            ConferenceElement(
                content=content,
                muted=muted,
                enter_sound=enter_sound,
                exit_sound=exit_sound,
                start_conference_on_enter=start_conference_on_enter,
                end_conference_on_exit=end_conference_on_exit,
                stay_alone=stay_alone,
                wait_sound=wait_sound,
                max_members=max_members,
                record=record,
                record_file_format=record_file_format,
                time_limit=time_limit,
                hangup_on_star=hangup_on_star,
                action=action,
                method=method,
                callback_url=callback_url,
                callback_method=callback_method,
                digits_match=digits_match,
                floor_event=floor_event,
                redirect=redirect,
                relay_dtmf=relay_dtmf, ))
        return self

    def add_dial(
            self,
            action=None,
            method=None,
            hangup_on_star=None,
            time_limit=None,
            timeout=None,
            caller_id=None,
            caller_name=None,
            confirm_sound=None,
            confirm_key=None,
            dial_music=None,
            callback_url=None,
            callback_method=None,
            redirect=None,
            digits_match=None,
            digits_match_b_leg=None,
            sip_headers=None, ):
        self.add(
            DialElement(
                action=action,
                method=method,
                hangup_on_star=hangup_on_star,
                time_limit=time_limit,
                timeout=timeout,
                caller_id=caller_id,
                caller_name=caller_name,
                confirm_sound=confirm_sound,
                confirm_key=confirm_key,
                dial_music=dial_music,
                callback_url=callback_url,
                callback_method=callback_method,
                redirect=redirect,
                digits_match=digits_match,
                digits_match_b_leg=digits_match_b_leg,
                sip_headers=sip_headers, ))
        return self

    def add_number(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None, ):
        self.add(
            NumberElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer, ))
        return self

    def add_user(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None,
            sip_headers=None, ):
        self.add(
            UserElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer,
                sip_headers=sip_headers, ))
        return self

    def add_dtmf(
            self,
            content,
            async=None, ):
        self.add(DTMFElement(
            content=content,
            async=async, ))
        return self

    def add_get_digits(
            self,
            action=None,
            method=None,
            timeout=None,
            digit_timeout=None,
            finish_on_key=None,
            num_digits=None,
            retries=None,
            redirect=None,
            play_beep=None,
            valid_digits=None,
            invalid_digits_sound=None,
            log=None, ):
        self.add(
            GetDigitsElement(
                action=action,
                method=method,
                timeout=timeout,
                digit_timeout=digit_timeout,
                finish_on_key=finish_on_key,
                num_digits=num_digits,
                retries=retries,
                redirect=redirect,
                play_beep=play_beep,
                valid_digits=valid_digits,
                invalid_digits_sound=invalid_digits_sound,
                log=log, ))
        return self

    def add_hangup(
            self,
            reason=None,
            schedule=None, ):
        self.add(HangupElement(
            reason=reason,
            schedule=schedule, ))
        return self

    def add_message(
            self,
            content,
            src=None,
            dst=None,
            type=None,
            callback_url=None,
            callback_method=None, ):
        self.add(
            MessageElement(
                content=content,
                src=src,
                dst=dst,
                type=type,
                callback_url=callback_url,
                callback_method=callback_method, ))
        return self

    def add_play(
            self,
            content,
            loop=None, ):
        self.add(PlayElement(
            content=content,
            loop=loop, ))
        return self

    def add_pre_answer(
            self, ):
        self.add(PreAnswerElement())
        return self

    def add_record(
            self,
            action=None,
            method=None,
            file_format=None,
            redirect=None,
            timeout=None,
            max_length=None,
            play_beep=None,
            finish_on_key=None,
            record_session=None,
            start_on_dial_answer=None,
            transcription_type=None,
            transcription_url=None,
            transcription_method=None,
            callback_url=None,
            callback_method=None, ):
        self.add(
            RecordElement(
                action=action,
                method=method,
                file_format=file_format,
                redirect=redirect,
                timeout=timeout,
                max_length=max_length,
                play_beep=play_beep,
                finish_on_key=finish_on_key,
                record_session=record_session,
                start_on_dial_answer=start_on_dial_answer,
                transcription_type=transcription_type,
                transcription_url=transcription_url,
                transcription_method=transcription_method,
                callback_url=callback_url,
                callback_method=callback_method, ))
        return self

    def add_redirect(
            self,
            content,
            method=None, ):
        self.add(RedirectElement(
            content=content,
            method=method, ))
        return self

    def add_speak(
            self,
            content,
            voice=None,
            language=None,
            loop=None, ):
        self.add(
            SpeakElement(
                content=content,
                voice=voice,
                language=language,
                loop=loop, ))
        return self

    def add_wait(
            self,
            length=None,
            silence=None,
            min_silence=None,
            beep=None, ):
        self.add(
            WaitElement(
                length=length,
                silence=silence,
                min_silence=min_silence,
                beep=beep, ))
        return self

    def to_dict(self):
        return {}


class ConferenceElement(PlivoXMLElement):
    _name = 'Conference'
    _nestable = []

    @property
    def muted(self):
        return self.__muted

    @muted.setter
    def muted(self, value):
        self.__muted = bool(value) if value is not None else None

    def set_muted(self, value):
        self.muted = value
        return self

    @property
    def enter_sound(self):
        return self.__enter_sound

    @enter_sound.setter
    def enter_sound(self, value):
        self.__enter_sound = six.text_type(
            value) if value is not None else None

    def set_enter_sound(self, value):
        self.enter_sound = value
        return self

    @property
    def exit_sound(self):
        return self.__exit_sound

    @exit_sound.setter
    def exit_sound(self, value):
        self.__exit_sound = six.text_type(value) if value is not None else None

    def set_exit_sound(self, value):
        self.exit_sound = value
        return self

    @property
    def start_conference_on_enter(self):
        return self.__start_conference_on_enter

    @start_conference_on_enter.setter
    def start_conference_on_enter(self, value):
        self.__start_conference_on_enter = bool(
            value) if value is not None else None

    def set_start_conference_on_enter(self, value):
        self.start_conference_on_enter = value
        return self

    @property
    def end_conference_on_exit(self):
        return self.__end_conference_on_exit

    @end_conference_on_exit.setter
    def end_conference_on_exit(self, value):
        self.__end_conference_on_exit = bool(
            value) if value is not None else None

    def set_end_conference_on_exit(self, value):
        self.end_conference_on_exit = value
        return self

    @property
    def stay_alone(self):
        return self.__stay_alone

    @stay_alone.setter
    def stay_alone(self, value):
        self.__stay_alone = bool(value) if value is not None else None

    def set_stay_alone(self, value):
        self.stay_alone = value
        return self

    @property
    def wait_sound(self):
        return self.__wait_sound

    @wait_sound.setter
    def wait_sound(self, value):
        self.__wait_sound = six.text_type(value) if value is not None else None

    def set_wait_sound(self, value):
        self.wait_sound = value
        return self

    @property
    def max_members(self):
        return self.__max_members

    @max_members.setter
    def max_members(self, value):
        self.__max_members = int(value) if value is not None else None

    def set_max_members(self, value):
        self.max_members = value
        return self

    @property
    def record(self):
        return self.__record

    @record.setter
    def record(self, value):
        self.__record = bool(value) if value is not None else None

    def set_record(self, value):
        self.record = value
        return self

    @property
    def record_file_format(self):
        return self.__record_file_format

    @record_file_format.setter
    def record_file_format(self, value):
        self.__record_file_format = six.text_type(
            value) if value is not None else None

    def set_record_file_format(self, value):
        self.record_file_format = value
        return self

    @property
    def time_limit(self):
        return self.__time_limit

    @time_limit.setter
    def time_limit(self, value):
        self.__time_limit = int(value) if value is not None else None

    def set_time_limit(self, value):
        self.time_limit = value
        return self

    @property
    def hangup_on_star(self):
        return self.__hangup_on_star

    @hangup_on_star.setter
    def hangup_on_star(self, value):
        self.__hangup_on_star = bool(value) if value is not None else None

    def set_hangup_on_star(self, value):
        self.hangup_on_star = value
        return self

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = six.text_type(value) if value is not None else None

    def set_action(self, value):
        self.action = value
        return self

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = six.text_type(value) if value is not None else None

    def set_method(self, value):
        self.method = value
        return self

    @property
    def callback_url(self):
        return self.__callback_url

    @callback_url.setter
    def callback_url(self, value):
        self.__callback_url = six.text_type(
            value) if value is not None else None

    def set_callback_url(self, value):
        self.callback_url = value
        return self

    @property
    def callback_method(self):
        return self.__callback_method

    @callback_method.setter
    def callback_method(self, value):
        self.__callback_method = six.text_type(
            value) if value is not None else None

    def set_callback_method(self, value):
        self.callback_method = value
        return self

    @property
    def digits_match(self):
        return self.__digits_match

    @digits_match.setter
    def digits_match(self, value):
        self.__digits_match = six.text_type(
            value) if value is not None else None

    def set_digits_match(self, value):
        self.digits_match = value
        return self

    @property
    def floor_event(self):
        return self.__floor_event

    @floor_event.setter
    def floor_event(self, value):
        self.__floor_event = bool(value) if value is not None else None

    def set_floor_event(self, value):
        self.floor_event = value
        return self

    @property
    def redirect(self):
        return self.__redirect

    @redirect.setter
    def redirect(self, value):
        self.__redirect = bool(value) if value is not None else None

    def set_redirect(self, value):
        self.redirect = value
        return self

    @property
    def relay_dtmf(self):
        return self.__relay_dtmf

    @relay_dtmf.setter
    def relay_dtmf(self, value):
        self.__relay_dtmf = bool(value) if value is not None else None

    def set_relay_dtmf(self, value):
        self.relay_dtmf = value
        return self

    def __init__(
            self,
            content,
            muted=None,
            enter_sound=None,
            exit_sound=None,
            start_conference_on_enter=None,
            end_conference_on_exit=None,
            stay_alone=None,
            wait_sound=None,
            max_members=None,
            record=None,
            record_file_format=None,
            time_limit=None,
            hangup_on_star=None,
            action=None,
            method=None,
            callback_url=None,
            callback_method=None,
            digits_match=None,
            floor_event=None,
            redirect=None,
            relay_dtmf=None, ):
        super(ConferenceElement, self).__init__()

        self.content = content
        self.muted = muted
        self.enter_sound = enter_sound
        self.exit_sound = exit_sound
        self.start_conference_on_enter = start_conference_on_enter
        self.end_conference_on_exit = end_conference_on_exit
        self.stay_alone = stay_alone
        self.wait_sound = wait_sound
        self.max_members = max_members
        self.record = record
        self.record_file_format = record_file_format
        self.time_limit = time_limit
        self.hangup_on_star = hangup_on_star
        self.action = action
        self.method = method
        self.callback_url = callback_url
        self.callback_method = callback_method
        self.digits_match = digits_match
        self.floor_event = floor_event
        self.redirect = redirect
        self.relay_dtmf = relay_dtmf

    def to_dict(self):
        d = {
            'muted': self.muted,
            'enterSound': self.enter_sound,
            'exitSound': self.exit_sound,
            'startConferenceOnEnter': self.start_conference_on_enter,
            'endConferenceOnExit': self.end_conference_on_exit,
            'stayAlone': self.stay_alone,
            'waitSound': self.wait_sound,
            'maxMembers': self.max_members,
            'record': self.record,
            'recordFileFormat': self.record_file_format,
            'timeLimit': self.time_limit,
            'hangupOnStar': self.hangup_on_star,
            'action': self.action,
            'method': self.method,
            'callbackUrl': self.callback_url,
            'callbackMethod': self.callback_method,
            'digitsMatch': self.digits_match,
            'floorEvent': self.floor_event,
            'redirect': self.redirect,
            'relayDTMF': self.relay_dtmf,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class DialElement(PlivoXMLElement):
    _name = 'Dial'
    _nestable = ['User', 'Number']

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = six.text_type(value) if value is not None else None

    def set_action(self, value):
        self.action = value
        return self

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = six.text_type(value) if value is not None else None

    def set_method(self, value):
        self.method = value
        return self

    @property
    def hangup_on_star(self):
        return self.__hangup_on_star

    @hangup_on_star.setter
    def hangup_on_star(self, value):
        self.__hangup_on_star = bool(value) if value is not None else None

    def set_hangup_on_star(self, value):
        self.hangup_on_star = value
        return self

    @property
    def time_limit(self):
        return self.__time_limit

    @time_limit.setter
    def time_limit(self, value):
        self.__time_limit = int(value) if value is not None else None

    def set_time_limit(self, value):
        self.time_limit = value
        return self

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        self.__timeout = int(value) if value is not None else None

    def set_timeout(self, value):
        self.timeout = value
        return self

    @property
    def caller_id(self):
        return self.__caller_id

    @caller_id.setter
    def caller_id(self, value):
        self.__caller_id = six.text_type(value) if value is not None else None

    def set_caller_id(self, value):
        self.caller_id = value
        return self

    @property
    def caller_name(self):
        return self.__caller_name

    @caller_name.setter
    def caller_name(self, value):
        self.__caller_name = six.text_type(
            value) if value is not None else None

    def set_caller_name(self, value):
        self.caller_name = value
        return self

    @property
    def confirm_sound(self):
        return self.__confirm_sound

    @confirm_sound.setter
    def confirm_sound(self, value):
        self.__confirm_sound = six.text_type(
            value) if value is not None else None

    def set_confirm_sound(self, value):
        self.confirm_sound = value
        return self

    @property
    def confirm_key(self):
        return self.__confirm_key

    @confirm_key.setter
    def confirm_key(self, value):
        self.__confirm_key = six.text_type(
            value) if value is not None else None

    def set_confirm_key(self, value):
        self.confirm_key = value
        return self

    @property
    def dial_music(self):
        return self.__dial_music

    @dial_music.setter
    def dial_music(self, value):
        self.__dial_music = six.text_type(value) if value is not None else None

    def set_dial_music(self, value):
        self.dial_music = value
        return self

    @property
    def callback_url(self):
        return self.__callback_url

    @callback_url.setter
    def callback_url(self, value):
        self.__callback_url = six.text_type(
            value) if value is not None else None

    def set_callback_url(self, value):
        self.callback_url = value
        return self

    @property
    def callback_method(self):
        return self.__callback_method

    @callback_method.setter
    def callback_method(self, value):
        self.__callback_method = six.text_type(
            value) if value is not None else None

    def set_callback_method(self, value):
        self.callback_method = value
        return self

    @property
    def redirect(self):
        return self.__redirect

    @redirect.setter
    def redirect(self, value):
        self.__redirect = bool(value) if value is not None else None

    def set_redirect(self, value):
        self.redirect = value
        return self

    @property
    def digits_match(self):
        return self.__digits_match

    @digits_match.setter
    def digits_match(self, value):
        self.__digits_match = six.text_type(
            value) if value is not None else None

    def set_digits_match(self, value):
        self.digits_match = value
        return self

    @property
    def digits_match_b_leg(self):
        return self.__digits_match_b_leg

    @digits_match_b_leg.setter
    def digits_match_b_leg(self, value):
        self.__digits_match_b_leg = six.text_type(
            value) if value is not None else None

    def set_digits_match_b_leg(self, value):
        self.digits_match_b_leg = value
        return self

    @property
    def sip_headers(self):
        return self.__sip_headers

    @sip_headers.setter
    def sip_headers(self, value):
        self.__sip_headers = six.text_type(
            value) if value is not None else None

    def set_sip_headers(self, value):
        self.sip_headers = value
        return self

    def __init__(
            self,
            action=None,
            method=None,
            hangup_on_star=None,
            time_limit=None,
            timeout=None,
            caller_id=None,
            caller_name=None,
            confirm_sound=None,
            confirm_key=None,
            dial_music=None,
            callback_url=None,
            callback_method=None,
            redirect=None,
            digits_match=None,
            digits_match_b_leg=None,
            sip_headers=None, ):
        super(DialElement, self).__init__()

        self.action = action
        self.method = method
        self.hangup_on_star = hangup_on_star
        self.time_limit = time_limit
        self.timeout = timeout
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.confirm_sound = confirm_sound
        self.confirm_key = confirm_key
        self.dial_music = dial_music
        self.callback_url = callback_url
        self.callback_method = callback_method
        self.redirect = redirect
        self.digits_match = digits_match
        self.digits_match_b_leg = digits_match_b_leg
        self.sip_headers = sip_headers

    def to_dict(self):
        d = {
            'action': self.action,
            'method': self.method,
            'hangupOnStar': self.hangup_on_star,
            'timeLimit': self.time_limit,
            'timeout': self.timeout,
            'callerID': self.caller_id,
            'callerName': self.caller_name,
            'confirmSound': self.confirm_sound,
            'confirmKey': self.confirm_key,
            'dialMusic': self.dial_music,
            'callbackUrl': self.callback_url,
            'callbackMethod': self.callback_method,
            'redirect': self.redirect,
            'digitsMatch': self.digits_match,
            'digitsMatchBLeg': self.digits_match_b_leg,
            'sipHeaders': self.sip_headers,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_user(
            self,
            content,
            send_digits,
            send_on_preanswer,
            sip_headers, ):
        self.add(
            UserElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer,
                sip_headers=sip_headers, ))
        return self

    def add_number(
            self,
            content,
            send_digits,
            send_on_preanswer, ):
        self.add(
            NumberElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer, ))
        return self


class NumberElement(PlivoXMLElement):
    _name = 'Number'
    _nestable = []

    @property
    def send_digits(self):
        return self.__send_digits

    @send_digits.setter
    def send_digits(self, value):
        self.__send_digits = six.text_type(
            value) if value is not None else None

    def set_send_digits(self, value):
        self.send_digits = value
        return self

    @property
    def send_on_preanswer(self):
        return self.__send_on_preanswer

    @send_on_preanswer.setter
    def send_on_preanswer(self, value):
        self.__send_on_preanswer = bool(value) if value is not None else None

    def set_send_on_preanswer(self, value):
        self.send_on_preanswer = value
        return self

    def __init__(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None, ):
        super(NumberElement, self).__init__()

        self.content = content
        self.send_digits = send_digits
        self.send_on_preanswer = send_on_preanswer

    def to_dict(self):
        d = {
            'sendDigits': self.send_digits,
            'sendOnPreanswer': self.send_on_preanswer,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class UserElement(PlivoXMLElement):
    _name = 'User'
    _nestable = []

    @property
    def send_digits(self):
        return self.__send_digits

    @send_digits.setter
    def send_digits(self, value):
        self.__send_digits = six.text_type(
            value) if value is not None else None

    def set_send_digits(self, value):
        self.send_digits = value
        return self

    @property
    def send_on_preanswer(self):
        return self.__send_on_preanswer

    @send_on_preanswer.setter
    def send_on_preanswer(self, value):
        self.__send_on_preanswer = bool(value) if value is not None else None

    def set_send_on_preanswer(self, value):
        self.send_on_preanswer = value
        return self

    @property
    def sip_headers(self):
        return self.__sip_headers

    @sip_headers.setter
    def sip_headers(self, value):
        self.__sip_headers = six.text_type(
            value) if value is not None else None

    def set_sip_headers(self, value):
        self.sip_headers = value
        return self

    def __init__(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None,
            sip_headers=None, ):
        super(UserElement, self).__init__()

        self.content = content
        self.send_digits = send_digits
        self.send_on_preanswer = send_on_preanswer
        self.sip_headers = sip_headers

    def to_dict(self):
        d = {
            'sendDigits': self.send_digits,
            'sendOnPreanswer': self.send_on_preanswer,
            'sipHeaders': self.sip_headers,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class DTMFElement(PlivoXMLElement):
    _name = 'DTMF'
    _nestable = []

    @property
    def async(self):
        return self.__async

    @async.setter
    def async(self, value):
        self.__async = bool(value) if value is not None else None

    def set_async(self, value):
        self.async = value
        return self

    def __init__(
            self,
            content,
            async=None, ):
        super(DTMFElement, self).__init__()

        self.content = content
        self.async = async

    def to_dict(self):
        d = {
            'async': self.async,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class GetDigitsElement(PlivoXMLElement):
    _name = 'GetDigits'
    _nestable = ['Speak', 'Play']

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = six.text_type(value) if value is not None else None

    def set_action(self, value):
        self.action = value
        return self

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = six.text_type(value) if value is not None else None

    def set_method(self, value):
        self.method = value
        return self

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        self.__timeout = int(value) if value is not None else None

    def set_timeout(self, value):
        self.timeout = value
        return self

    @property
    def digit_timeout(self):
        return self.__digit_timeout

    @digit_timeout.setter
    def digit_timeout(self, value):
        self.__digit_timeout = int(value) if value is not None else None

    def set_digit_timeout(self, value):
        self.digit_timeout = value
        return self

    @property
    def finish_on_key(self):
        return self.__finish_on_key

    @finish_on_key.setter
    def finish_on_key(self, value):
        self.__finish_on_key = six.text_type(
            value) if value is not None else None

    def set_finish_on_key(self, value):
        self.finish_on_key = value
        return self

    @property
    def num_digits(self):
        return self.__num_digits

    @num_digits.setter
    def num_digits(self, value):
        self.__num_digits = int(value) if value is not None else None

    def set_num_digits(self, value):
        self.num_digits = value
        return self

    @property
    def retries(self):
        return self.__retries

    @retries.setter
    def retries(self, value):
        self.__retries = int(value) if value is not None else None

    def set_retries(self, value):
        self.retries = value
        return self

    @property
    def redirect(self):
        return self.__redirect

    @redirect.setter
    def redirect(self, value):
        self.__redirect = bool(value) if value is not None else None

    def set_redirect(self, value):
        self.redirect = value
        return self

    @property
    def play_beep(self):
        return self.__play_beep

    @play_beep.setter
    def play_beep(self, value):
        self.__play_beep = bool(value) if value is not None else None

    def set_play_beep(self, value):
        self.play_beep = value
        return self

    @property
    def valid_digits(self):
        return self.__valid_digits

    @valid_digits.setter
    def valid_digits(self, value):
        self.__valid_digits = six.text_type(
            value) if value is not None else None

    def set_valid_digits(self, value):
        self.valid_digits = value
        return self

    @property
    def invalid_digits_sound(self):
        return self.__invalid_digits_sound

    @invalid_digits_sound.setter
    def invalid_digits_sound(self, value):
        self.__invalid_digits_sound = six.text_type(
            value) if value is not None else None

    def set_invalid_digits_sound(self, value):
        self.invalid_digits_sound = value
        return self

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, value):
        self.__log = bool(value) if value is not None else None

    def set_log(self, value):
        self.log = value
        return self

    def __init__(
            self,
            action=None,
            method=None,
            timeout=None,
            digit_timeout=None,
            finish_on_key=None,
            num_digits=None,
            retries=None,
            redirect=None,
            play_beep=None,
            valid_digits=None,
            invalid_digits_sound=None,
            log=None, ):
        super(GetDigitsElement, self).__init__()

        self.action = action
        self.method = method
        self.timeout = timeout
        self.digit_timeout = digit_timeout
        self.finish_on_key = finish_on_key
        self.num_digits = num_digits
        self.retries = retries
        self.redirect = redirect
        self.play_beep = play_beep
        self.valid_digits = valid_digits
        self.invalid_digits_sound = invalid_digits_sound
        self.log = log

    def to_dict(self):
        d = {
            'action': self.action,
            'method': self.method,
            'timeout': self.timeout,
            'digitTimeout': self.digit_timeout,
            'finishOnKey': self.finish_on_key,
            'numDigits': self.num_digits,
            'retries': self.retries,
            'redirect': self.redirect,
            'playBeep': self.play_beep,
            'validDigits': self.valid_digits,
            'invalidDigitsSound': self.invalid_digits_sound,
            'log': self.log,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_speak(
            self,
            content,
            voice,
            language,
            loop, ):
        self.add(
            SpeakElement(
                content=content,
                voice=voice,
                language=language,
                loop=loop, ))
        return self

    def add_play(
            self,
            content,
            loop, ):
        self.add(PlayElement(
            content=content,
            loop=loop, ))
        return self


class HangupElement(PlivoXMLElement):
    _name = 'Hangup'
    _nestable = []

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = six.text_type(value) if value is not None else None

    def set_reason(self, value):
        self.reason = value
        return self

    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, value):
        self.__schedule = int(value) if value is not None else None

    def set_schedule(self, value):
        self.schedule = value
        return self

    def __init__(
            self,
            reason=None,
            schedule=None, ):
        super(HangupElement, self).__init__()

        self.reason = reason
        self.schedule = schedule

    def to_dict(self):
        d = {
            'reason': self.reason,
            'schedule': self.schedule,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class MessageElement(PlivoXMLElement):
    _name = 'Message'
    _nestable = []

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        self.__src = six.text_type(value) if value is not None else None

    def set_src(self, value):
        self.src = value
        return self

    @property
    def dst(self):
        return self.__dst

    @dst.setter
    def dst(self, value):
        self.__dst = six.text_type(value) if value is not None else None

    def set_dst(self, value):
        self.dst = value
        return self

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = six.text_type(value) if value is not None else None

    def set_type(self, value):
        self.type = value
        return self

    @property
    def callback_url(self):
        return self.__callback_url

    @callback_url.setter
    def callback_url(self, value):
        self.__callback_url = six.text_type(
            value) if value is not None else None

    def set_callback_url(self, value):
        self.callback_url = value
        return self

    @property
    def callback_method(self):
        return self.__callback_method

    @callback_method.setter
    def callback_method(self, value):
        self.__callback_method = six.text_type(
            value) if value is not None else None

    def set_callback_method(self, value):
        self.callback_method = value
        return self

    def __init__(
            self,
            content,
            src=None,
            dst=None,
            type=None,
            callback_url=None,
            callback_method=None, ):
        super(MessageElement, self).__init__()

        self.content = content
        self.src = src
        self.dst = dst
        self.type = type
        self.callback_url = callback_url
        self.callback_method = callback_method

    def to_dict(self):
        d = {
            'src': self.src,
            'dst': self.dst,
            'type': self.type,
            'callbackUrl': self.callback_url,
            'callbackMethod': self.callback_method,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class PlayElement(PlivoXMLElement):
    _name = 'Play'
    _nestable = []

    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, value):
        self.__loop = int(value) if value is not None else None

    def set_loop(self, value):
        self.loop = value
        return self

    def __init__(
            self,
            content,
            loop=None, ):
        super(PlayElement, self).__init__()

        self.content = content
        self.loop = loop

    def to_dict(self):
        d = {
            'loop': self.loop,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class PreAnswerElement(PlivoXMLElement):
    _name = 'PreAnswer'
    _nestable = ['Speak', 'Play', 'Wait']

    def __init__(
            self, ):
        super(PreAnswerElement, self).__init__()

        pass

    def to_dict(self):
        d = {}
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_speak(
            self,
            content,
            voice=None,
            language=None,
            loop=None, ):
        self.add(
            SpeakElement(
                content=content,
                voice=voice,
                language=language,
                loop=loop, ))
        return self

    def add_play(
            self,
            content,
            loop=None, ):
        self.add(PlayElement(
            content=content,
            loop=loop, ))
        return self

    def add_wait(
            self,
            length=None,
            silence=None,
            min_silence=None,
            beep=None, ):
        self.add(
            WaitElement(
                length=length,
                silence=silence,
                min_silence=min_silence,
                beep=beep, ))
        return self


class RecordElement(PlivoXMLElement):
    _name = 'Record'
    _nestable = []

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = six.text_type(value) if value is not None else None

    def set_action(self, value):
        self.action = value
        return self

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = six.text_type(value) if value is not None else None

    def set_method(self, value):
        self.method = value
        return self

    @property
    def file_format(self):
        return self.__file_format

    @file_format.setter
    def file_format(self, value):
        self.__file_format = six.text_type(
            value) if value is not None else None

    def set_file_format(self, value):
        self.file_format = value
        return self

    @property
    def redirect(self):
        return self.__redirect

    @redirect.setter
    def redirect(self, value):
        self.__redirect = bool(value) if value is not None else None

    def set_redirect(self, value):
        self.redirect = value
        return self

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        self.__timeout = int(value) if value is not None else None

    def set_timeout(self, value):
        self.timeout = value
        return self

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, value):
        self.__max_length = int(value) if value is not None else None

    def set_max_length(self, value):
        self.max_length = value
        return self

    @property
    def play_beep(self):
        return self.__play_beep

    @play_beep.setter
    def play_beep(self, value):
        self.__play_beep = bool(value) if value is not None else None

    def set_play_beep(self, value):
        self.play_beep = value
        return self

    @property
    def finish_on_key(self):
        return self.__finish_on_key

    @finish_on_key.setter
    def finish_on_key(self, value):
        self.__finish_on_key = six.text_type(
            value) if value is not None else None

    def set_finish_on_key(self, value):
        self.finish_on_key = value
        return self

    @property
    def record_session(self):
        return self.__record_session

    @record_session.setter
    def record_session(self, value):
        self.__record_session = bool(value) if value is not None else None

    def set_record_session(self, value):
        self.record_session = value
        return self

    @property
    def start_on_dial_answer(self):
        return self.__start_on_dial_answer

    @start_on_dial_answer.setter
    def start_on_dial_answer(self, value):
        self.__start_on_dial_answer = bool(
            value) if value is not None else None

    def set_start_on_dial_answer(self, value):
        self.start_on_dial_answer = value
        return self

    @property
    def transcription_type(self):
        return self.__transcription_type

    @transcription_type.setter
    def transcription_type(self, value):
        self.__transcription_type = six.text_type(
            value) if value is not None else None

    def set_transcription_type(self, value):
        self.transcription_type = value
        return self

    @property
    def transcription_url(self):
        return self.__transcription_url

    @transcription_url.setter
    def transcription_url(self, value):
        self.__transcription_url = six.text_type(
            value) if value is not None else None

    def set_transcription_url(self, value):
        self.transcription_url = value
        return self

    @property
    def transcription_method(self):
        return self.__transcription_method

    @transcription_method.setter
    def transcription_method(self, value):
        self.__transcription_method = six.text_type(
            value) if value is not None else None

    def set_transcription_method(self, value):
        self.transcription_method = value
        return self

    @property
    def callback_url(self):
        return self.__callback_url

    @callback_url.setter
    def callback_url(self, value):
        self.__callback_url = six.text_type(
            value) if value is not None else None

    def set_callback_url(self, value):
        self.callback_url = value
        return self

    @property
    def callback_method(self):
        return self.__callback_method

    @callback_method.setter
    def callback_method(self, value):
        self.__callback_method = six.text_type(
            value) if value is not None else None

    def set_callback_method(self, value):
        self.callback_method = value
        return self

    def __init__(
            self,
            action=None,
            method=None,
            file_format=None,
            redirect=None,
            timeout=None,
            max_length=None,
            play_beep=None,
            finish_on_key=None,
            record_session=None,
            start_on_dial_answer=None,
            transcription_type=None,
            transcription_url=None,
            transcription_method=None,
            callback_url=None,
            callback_method=None, ):
        super(RecordElement, self).__init__()

        self.action = action
        self.method = method
        self.file_format = file_format
        self.redirect = redirect
        self.timeout = timeout
        self.max_length = max_length
        self.play_beep = play_beep
        self.finish_on_key = finish_on_key
        self.record_session = record_session
        self.start_on_dial_answer = start_on_dial_answer
        self.transcription_type = transcription_type
        self.transcription_url = transcription_url
        self.transcription_method = transcription_method
        self.callback_url = callback_url
        self.callback_method = callback_method

    def to_dict(self):
        d = {
            'action': self.action,
            'method': self.method,
            'fileFormat': self.file_format,
            'redirect': self.redirect,
            'timeout': self.timeout,
            'maxLength': self.max_length,
            'playBeep': self.play_beep,
            'finishOnKey': self.finish_on_key,
            'recordSession': self.record_session,
            'startOnDialAnswer': self.start_on_dial_answer,
            'transcriptionType': self.transcription_type,
            'transcriptionUrl': self.transcription_url,
            'transcriptionMethod': self.transcription_method,
            'callbackUrl': self.callback_url,
            'callbackMethod': self.callback_method,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class RedirectElement(PlivoXMLElement):
    _name = 'Redirect'
    _nestable = []

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = six.text_type(value) if value is not None else None

    def set_method(self, value):
        self.method = value
        return self

    def __init__(
            self,
            content,
            method=None, ):
        super(RedirectElement, self).__init__()

        self.content = content
        self.method = method

    def to_dict(self):
        d = {
            'method': self.method,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class SpeakElement(PlivoXMLElement):
    _name = 'Speak'
    _nestable = []

    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, value):
        self.__voice = six.text_type(value) if value is not None else None

    def set_voice(self, value):
        self.voice = value
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = six.text_type(value) if value is not None else None

    def set_language(self, value):
        self.language = value
        return self

    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, value):
        self.__loop = int(value) if value is not None else None

    def set_loop(self, value):
        self.loop = value
        return self

    def __init__(
            self,
            content,
            voice=None,
            language=None,
            loop=None, ):
        super(SpeakElement, self).__init__()

        self.content = content
        self.voice = voice
        self.language = language
        self.loop = loop

    def to_dict(self):
        d = {
            'voice': self.voice,
            'language': self.language,
            'loop': self.loop,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }


class WaitElement(PlivoXMLElement):
    _name = 'Wait'
    _nestable = []

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = int(value) if value is not None else None

    def set_length(self, value):
        self.length = value
        return self

    @property
    def silence(self):
        return self.__silence

    @silence.setter
    def silence(self, value):
        self.__silence = bool(value) if value is not None else None

    def set_silence(self, value):
        self.silence = value
        return self

    @property
    def min_silence(self):
        return self.__min_silence

    @min_silence.setter
    def min_silence(self, value):
        self.__min_silence = int(value) if value is not None else None

    def set_min_silence(self, value):
        self.min_silence = value
        return self

    @property
    def beep(self):
        return self.__beep

    @beep.setter
    def beep(self, value):
        self.__beep = bool(value) if value is not None else None

    def set_beep(self, value):
        self.beep = value
        return self

    def __init__(
            self,
            length=None,
            silence=None,
            min_silence=None,
            beep=None, ):
        super(WaitElement, self).__init__()

        self.length = length
        self.silence = silence
        self.min_silence = min_silence
        self.beep = beep

    def to_dict(self):
        d = {
            'length': self.length,
            'silence': self.silence,
            'minSilence': self.min_silence,
            'beep': self.beep,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
