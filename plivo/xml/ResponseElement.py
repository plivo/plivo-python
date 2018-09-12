from plivo.xml import (ConferenceElement, DialElement, DTMFElement,
                       GetDigitsElement, HangupElement, MessageElement,
                       NumberElement, PlayElement, PlivoXMLElement,
                       PreAnswerElement, RecordElement, RedirectElement,
                       SpeakElement, UserElement, WaitElement)


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
            relay_dtmf=None,
    ):
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
                relay_dtmf=relay_dtmf,
            ))
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
            sip_headers=None,
    ):
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
                sip_headers=sip_headers,
            ))
        return self

    def add_number(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None,
    ):
        self.add(
            NumberElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer,
            ))
        return self

    def add_user(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None,
            sip_headers=None,
    ):
        self.add(
            UserElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer,
                sip_headers=sip_headers,
            ))
        return self

    def add_dtmf(
            self,
            content,
            async_=None,
    ):
        self.add(DTMFElement(
            content=content,
            async_=async_,
        ))
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
            log=None,
    ):
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
                log=log,
            ))
        return self

    def add_hangup(
            self,
            reason=None,
            schedule=None,
    ):
        self.add(HangupElement(
            reason=reason,
            schedule=schedule,
        ))
        return self

    def add_message(
            self,
            content,
            src=None,
            dst=None,
            type=None,
            callback_url=None,
            callback_method=None,
    ):
        self.add(
            MessageElement(
                content=content,
                src=src,
                dst=dst,
                type=type,
                callback_url=callback_url,
                callback_method=callback_method,
            ))
        return self

    def add_play(
            self,
            content,
            loop=None,
    ):
        self.add(PlayElement(
            content=content,
            loop=loop,
        ))
        return self

    def add_pre_answer(self, ):
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
            callback_method=None,
    ):
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
                callback_method=callback_method,
            ))
        return self

    def add_redirect(
            self,
            content,
            method=None,
    ):
        self.add(RedirectElement(
            content=content,
            method=method,
        ))
        return self

    def add_speak(
            self,
            content,
            voice=None,
            language=None,
            loop=None,
    ):
        self.add(
            SpeakElement(
                content=content,
                voice=voice,
                language=language,
                loop=loop,
            ))
        return self

    def add_wait(
            self,
            length=None,
            silence=None,
            min_silence=None,
            beep=None,
    ):
        self.add(
            WaitElement(
                length=length,
                silence=silence,
                min_silence=min_silence,
                beep=beep,
            ))
        return self

    def to_dict(self):
        return {}
