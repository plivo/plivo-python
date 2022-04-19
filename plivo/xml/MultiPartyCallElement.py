from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class MultiPartyCallElement(PlivoXMLElement):
    _name = 'MultiPartyCall'
    _nestable = []

    @property
    def max_duration(self):
        return self.__max_duration

    @max_duration.setter
    @validate_args(
        max_duration=[
            optional(
                of_type_exact(int),
                check(lambda max_duration: 300 <= max_duration <= 28800, '300 <= max_duration <= 28800')
            )]
    )
    def max_duration(self, max_duration):
        self.__max_duration = max_duration

    def set_max_duration(self, max_duration):
        self.max_duration = max_duration
        return self

    @property
    def max_participants(self):
        return self.__max_participants

    @max_participants.setter
    @validate_args(
        max_participants=[
            optional(
                of_type_exact(int),
                check(lambda max_participants: 2 <= max_participants <= 10, '2 <= max_participants <= 10')
            )
        ],
    )
    def max_participants(self, max_participants):
        self.__max_participants = max_participants

    def set_max_participants(self, max_participants):
        self.max_participants = max_participants
        return self

    @property
    def record_min_member_count(self):
        return self.__record_min_member_count

    @record_min_member_count.setter
    @validate_args(
        record_min_member_count=[
            optional(
                of_type_exact(int),
                check(lambda record_min_member_count: 1 <= record_min_member_count <= 2, '1 <= record_min_member_count <= 2')
            )
        ],
    )
    def record_min_member_count(self, record_min_member_count):
        self.__record_min_member_count = record_min_member_count

    def set_record_min_member_count(self, record_min_member_count):
        self.record_min_member_count = record_min_member_count
        return self

    @property
    def wait_music_url(self):
        return self.__wait_music_url

    @wait_music_url.setter
    @validate_args(wait_music_url=[optional(of_type_exact(str), is_url())])
    def wait_music_url(self, wait_music_url):
        self.__wait_music_url = wait_music_url

    def set_wait_music_url(self, wait_music_url):
        self.wait_music_url = wait_music_url
        return self

    @property
    def wait_music_method(self):
        return self.__wait_music_method

    @wait_music_method.setter
    @validate_args(wait_music_method=[optional(of_type_exact(str),
                                               is_in(('GET', 'POST'), case_sensitive=False))])
    def wait_music_method(self, wait_music_method):
        self.__wait_music_method = wait_music_method

    def set_wait_music_method(self, wait_music_method):
        self.wait_music_method = wait_music_method
        return self

    @property
    def agent_hold_music_url(self):
        return self.__agent_hold_music_url

    @agent_hold_music_url.setter
    @validate_args(agent_hold_music_url=[optional(of_type_exact(str), is_url())])
    def agent_hold_music_url(self, agent_hold_music_url):
        self.__agent_hold_music_url = agent_hold_music_url

    def set_agent_hold_music_url(self, agent_hold_music_url):
        self.agent_hold_music_url = agent_hold_music_url
        return self

    @property
    def agent_hold_music_method(self):
        return self.__agent_hold_music_method

    @agent_hold_music_method.setter
    @validate_args(agent_hold_music_method=[optional(of_type_exact(str),
                                                     is_in(('GET', 'POST'), case_sensitive=False))])
    def agent_hold_music_method(self, agent_hold_music_method):
        self.__agent_hold_music_method = agent_hold_music_method

    def set_agent_hold_music_method(self, agent_hold_music_method):
        self.agent_hold_music_method = agent_hold_music_method
        return self

    @property
    def customer_hold_music_url(self):
        return self.__customer_hold_music_url

    @customer_hold_music_url.setter
    @validate_args(customer_hold_music_url=[optional(of_type_exact(str), is_url())])
    def customer_hold_music_url(self, customer_hold_music_url):
        self.__customer_hold_music_url = customer_hold_music_url

    def set_customer_hold_music_url(self, customer_hold_music_url):
        self.customer_hold_music_url = customer_hold_music_url
        return self

    @property
    def customer_hold_music_method(self):
        return self.__customer_hold_music_method

    @customer_hold_music_method.setter
    @validate_args(customer_hold_music_method=[optional(of_type_exact(str),
                                                        is_in(('GET', 'POST'), case_sensitive=False))])
    def customer_hold_music_method(self, customer_hold_music_method):
        self.__customer_hold_music_method = customer_hold_music_method

    def set_customer_hold_music_method(self, customer_hold_music_method):
        self.customer_hold_music_method = customer_hold_music_method
        return self

    @property
    def record(self):
        return self.__record

    @record.setter
    @validate_args(record=[optional(of_type_exact(bool))])
    def record(self, record):
        self.__record = record

    def set_record(self, record):
        self.record = record
        return self

    @property
    def record_file_format(self):
        return self.__record_file_format

    @record_file_format.setter
    @validate_args(
        record_file_format=[
            optional(
                of_type_exact(str),
                is_in(('mp3', 'wav'), case_sensitive=False, case_type='lower')
            )
        ]
    )
    def record_file_format(self, record_file_format):
        self.__record_file_format = record_file_format

    def set_record_file_format(self, record_file_format):
        self.record_file_format = record_file_format
        return self

    @property
    def recording_callback_url(self):
        return self.__recording_callback_url

    @recording_callback_url.setter
    @validate_args(recording_callback_url=[optional(of_type_exact(str), is_url())])
    def recording_callback_url(self, recording_callback_url):
        self.__recording_callback_url = recording_callback_url

    def set_recording_callback_url(self, recording_callback_url):
        self.recording_callback_url = recording_callback_url
        return self

    @property
    def recording_callback_method(self):
        return self.__recording_callback_method

    @recording_callback_method.setter
    @validate_args(recording_callback_method=[optional(of_type_exact(str),
                                                       is_in(('GET', 'POST'), case_sensitive=False))])
    def recording_callback_method(self, recording_callback_method):
        self.__recording_callback_method = recording_callback_method

    def set_recording_callback_method(self, recording_callback_method):
        self.recording_callback_method = recording_callback_method
        return self

    @property
    def status_callback_events(self):
        return self.__status_callback_events

    @status_callback_events.setter
    @validate_args(
        status_callback_events=[
            optional(
                of_type_exact(str),
                multi_is_in(('mpc-state-changes',
                             'participant-state-changes',
                             'participant-speak-events',
                             'participant-digit-input-events',
                             'add-participant-api-events'),
                            case_sensitive=False,
                            make_lower_case=True)
            )
        ]
    )
    def status_callback_events(self, status_callback_events):
        self.__status_callback_events = status_callback_events

    def set_status_callback_events(self, status_callback_events):
        self.status_callback_events = status_callback_events
        return self

    @property
    def status_callback_url(self):
        return self.__status_callback_url

    @status_callback_url.setter
    @validate_args(status_callback_url=[optional(of_type_exact(str), is_url())])
    def status_callback_url(self, status_callback_url):
        self.__status_callback_url = status_callback_url

    def set_status_callback_url(self, status_callback_url):
        self.status_callback_url = status_callback_url
        return self

    @property
    def start_recording_audio(self):
        return self.__start_recording_audio

    @start_recording_audio.setter
    @validate_args(start_recording_audio=[optional(of_type_exact(str), is_url())])
    def start_recording_audio(self, start_recording_audio):
        self.__start_recording_audio = start_recording_audio

    def set_start_recording_audio(self, start_recording_audio):
        self.start_recording_audio = start_recording_audio
        return self

    @property
    def start_recording_audio_method(self):
        return self.__start_recording_audio_method

    @start_recording_audio_method.setter
    @validate_args(
        start_recording_audio_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))])
    def start_recording_audio_method(self, start_recording_audio_method):
        self.__start_recording_audio_method = start_recording_audio_method

    def set_start_recording_audio_method(self, start_recording_audio_method):
        self.start_recording_audio_method = start_recording_audio_method
        return self

    @property
    def stop_recording_audio(self):
        return self.__stop_recording_audio

    @stop_recording_audio.setter
    @validate_args(stop_recording_audio=[optional(of_type_exact(str), is_url())])
    def stop_recording_audio(self, stop_recording_audio):
        self.__stop_recording_audio = stop_recording_audio

    def set_stop_recording_audio(self, stop_recording_audio):
        self.stop_recording_audio = stop_recording_audio
        return self

    @property
    def stop_recording_audio_method(self):
        return self.__stop_recording_audio_method

    @stop_recording_audio_method.setter
    @validate_args(
        stop_recording_audio_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))])
    def stop_recording_audio_method(self, stop_recording_audio_method):
        self.__stop_recording_audio_method = stop_recording_audio_method

    def set_stop_recording_audio_method(self, stop_recording_audio_method):
        self.stop_recording_audio_method = stop_recording_audio_method
        return self

    @property
    def status_callback_method(self):
        return self.__status_callback_method

    @status_callback_method.setter
    @validate_args(status_callback_method=[optional(of_type_exact(str),
                                                    is_in(('GET', 'POST'), case_sensitive=False))])
    def status_callback_method(self, status_callback_method):
        self.__status_callback_method = status_callback_method

    def set_status_callback_method(self, status_callback_method):
        self.status_callback_method = status_callback_method
        return self

    @property
    def stay_alone(self):
        return self.__stay_alone

    @stay_alone.setter
    @validate_args(stay_alone=[optional(of_type_exact(bool))])
    def stay_alone(self, stay_alone):
        self.__stay_alone = stay_alone

    def set_stay_alone(self, stay_alone):
        self.stay_alone = stay_alone
        return self

    @property
    def role(self):
        return self.__role

    @role.setter
    @validate_args(
        role=[
            of_type_exact(str),
            is_in(('agent', 'supervisor', 'customer'), case_sensitive=False, case_type='lower')
        ]
    )
    def role(self, role):
        self.__role = role

    def set_role(self, role):
        self.role = role
        return self

    @property
    def coach_mode(self):
        return self.__coach_mode

    @coach_mode.setter
    @validate_args(coach_mode=[optional(of_type_exact(bool))])
    def coach_mode(self, coach_mode):
        self.__coach_mode = coach_mode

    def set_coach_mode(self, coach_mode):
        self.coach_mode = coach_mode
        return self

    @property
    def mute(self):
        return self.__mute

    @mute.setter
    @validate_args(mute=[optional(of_type_exact(bool))])
    def mute(self, mute):
        self.__mute = mute

    def set_mute(self, mute):
        self.mute = mute
        return self

    @property
    def hold(self):
        return self.__hold

    @hold.setter
    @validate_args(hold=[optional(of_type_exact(bool))])
    def hold(self, hold):
        self.__hold = hold

    def set_hold(self, hold):
        self.hold = hold
        return self

    @property
    def start_mpc_on_enter(self):
        return self.__start_mpc_on_enter

    @start_mpc_on_enter.setter
    @validate_args(start_mpc_on_enter=[optional(of_type_exact(bool))])
    def start_mpc_on_enter(self, start_mpc_on_enter):
        self.__start_mpc_on_enter = start_mpc_on_enter

    def set_start_mpc_on_enter(self, start_mpc_on_enter):
        self.start_mpc_on_enter = start_mpc_on_enter
        return self

    @property
    def end_mpc_on_exit(self):
        return self.__end_mpc_on_exit

    @end_mpc_on_exit.setter
    @validate_args(end_mpc_on_exit=[optional(of_type_exact(bool))])
    def end_mpc_on_exit(self, end_mpc_on_exit):
        self.__end_mpc_on_exit = end_mpc_on_exit

    def set_end_mpc_on_exit(self, end_mpc_on_exit):
        self.end_mpc_on_exit = end_mpc_on_exit
        return self

    @property
    def enter_sound(self):
        return self.__enter_sound

    @enter_sound.setter
    @validate_args(
        enter_sound=[
            optional(
                all_of(
                    of_type_exact(str),
                    one_of(is_url(), is_in(('beep:1', 'beep:2', 'none'), case_sensitive=False, case_type='lower'))
                )
            )
        ]
    )
    def enter_sound(self, enter_sound):
        self.__enter_sound = enter_sound

    def set_enter_sound(self, enter_sound):
        self.enter_sound = enter_sound
        return self

    @property
    def enter_sound_method(self):
        return self.__enter_sound_method

    @enter_sound_method.setter
    @validate_args(enter_sound_method=[optional(of_type_exact(str),
                                                is_in(('GET', 'POST'), case_sensitive=False))])
    def enter_sound_method(self, enter_sound_method):
        self.__enter_sound_method = enter_sound_method

    def set_enter_sound_method(self, enter_sound_method):
        self.enter_sound_method = enter_sound_method
        return self

    @property
    def exit_sound(self):
        return self.__exit_sound

    @exit_sound.setter
    @validate_args(
        exit_sound=[
            optional(
                all_of(
                    of_type_exact(str),
                    one_of(is_url(), is_in(('beep:1', 'beep:2', 'none'), case_sensitive=False, case_type='lower'))
                )
            )
        ]
    )
    def exit_sound(self, exit_sound):
        self.__exit_sound = exit_sound

    def set_exit_sound(self, exit_sound):
        self.exit_sound = exit_sound
        return self

    @property
    def exit_sound_method(self):
        return self.__exit_sound_method

    @exit_sound_method.setter
    @validate_args(exit_sound_method=[optional(of_type_exact(str),
                                               is_in(('GET', 'POST'), case_sensitive=False))])
    def exit_sound_method(self, exit_sound_method):
        self.__exit_sound_method = exit_sound_method

    def set_exit_sound_method(self, exit_sound_method):
        self.exit_sound_method = exit_sound_method
        return self

    @property
    def on_exit_action_url(self):
        return self.__on_exit_action_url

    @on_exit_action_url.setter
    @validate_args(on_exit_action_url=[optional(of_type_exact(str), is_url())])
    def on_exit_action_url(self, on_exit_action_url):
        self.__on_exit_action_url = on_exit_action_url

    def set_on_exit_action_url(self, on_exit_action_url):
        self.on_exit_action_url = on_exit_action_url
        return self

    @property
    def on_exit_action_method(self):
        return self.__on_exit_action_method

    @on_exit_action_method.setter
    @validate_args(on_exit_action_method=[optional(of_type_exact(str),
                                                   is_in(('GET', 'POST'), case_sensitive=False))])
    def on_exit_action_method(self, on_exit_action_method):
        self.__on_exit_action_method = on_exit_action_method

    def set_on_exit_action_method(self, on_exit_action_method):
        self.on_exit_action_method = on_exit_action_method
        return self

    @property
    def relay_dtmf_inputs(self):
        return self.__relay_dtmf_inputs

    @relay_dtmf_inputs.setter
    @validate_args(relay_dtmf_inputs=[optional(of_type_exact(bool))])
    def relay_dtmf_inputs(self, relay_dtmf_inputs):
        self.__relay_dtmf_inputs = relay_dtmf_inputs

    def set_relay_dtmf_inputs(self, relay_dtmf_inputs):
        self.relay_dtmf_inputs = relay_dtmf_inputs
        return self

    def __init__(
            self,
            content,
            role,
            max_duration=14400,
            max_participants=10,
            record_min_member_count=1,
            wait_music_url=None,
            wait_music_method='GET',
            agent_hold_music_url=None,
            agent_hold_music_method='GET',
            customer_hold_music_url=None,
            customer_hold_music_method='GET',
            record=False,
            record_file_format='mp3',
            recording_callback_url=None,
            recording_callback_method='POST',
            status_callback_events='mpc-state-changes,participant-state-changes',
            status_callback_url=None,
            status_callback_method='POST',
            stay_alone=False,
            coach_mode=True,
            mute=False,
            hold=False,
            start_mpc_on_enter=True,
            end_mpc_on_exit=False,
            enter_sound='beep:1',
            enter_sound_method='GET',
            exit_sound='beep:2',
            exit_sound_method='GET',
            on_exit_action_url=None,
            on_exit_action_method='POST',
            relay_dtmf_inputs=False,
            start_recording_audio=None,
            start_recording_audio_method='GET',
            stop_recording_audio=None,
            stop_recording_audio_method='GET'
    ):
        super(MultiPartyCallElement, self).__init__()
        self.stop_recording_audio_method = stop_recording_audio_method
        self.stop_recording_audio = stop_recording_audio
        self.start_recording_audio_method = start_recording_audio_method
        self.start_recording_audio = start_recording_audio
        self.content = content
        self.role = role
        self.max_duration = max_duration
        self.max_participants = max_participants
        self.record_min_member_count = record_min_member_count
        self.wait_music_url = wait_music_url
        self.wait_music_method = wait_music_method
        self.agent_hold_music_url = agent_hold_music_url
        self.agent_hold_music_method = agent_hold_music_method
        self.customer_hold_music_url = customer_hold_music_url
        self.customer_hold_music_method = customer_hold_music_method
        self.record = record
        self.record_file_format = record_file_format
        self.recording_callback_url = recording_callback_url
        self.recording_callback_method = recording_callback_method
        self.status_callback_events = status_callback_events
        self.status_callback_url = status_callback_url
        self.status_callback_method = status_callback_method
        self.stay_alone = stay_alone
        self.coach_mode = coach_mode
        self.mute = mute
        self.hold = hold
        self.start_mpc_on_enter = start_mpc_on_enter
        self.end_mpc_on_exit = end_mpc_on_exit
        self.enter_sound = enter_sound
        self.enter_sound_method = enter_sound_method
        self.exit_sound = exit_sound
        self.exit_sound_method = exit_sound_method
        self.on_exit_action_url = on_exit_action_url
        self.on_exit_action_method = on_exit_action_method
        self.relay_dtmf_inputs = relay_dtmf_inputs

    def to_dict(self):
        d = {
            'role': self.role,
            'maxDuration': self.max_duration,
            'maxParticipants': self.max_participants,
            'recordMinMemberCount': self.record_min_member_count,
            'waitMusicUrl': self.wait_music_url,
            'waitMusicMethod': self.wait_music_method,
            'agentHoldMusicUrl': self.agent_hold_music_url,
            'agentHoldMusicMethod': self.agent_hold_music_method,
            'customerHoldMusicUrl': self.customer_hold_music_url,
            'customerHoldMusicMethod': self.customer_hold_music_method,
            'record': self.record,
            'recordFileFormat': self.record_file_format,
            'recordingCallbackUrl': self.recording_callback_url,
            'recordingCallbackMethod': self.recording_callback_method,
            'statusCallbackEvents': self.status_callback_events,
            'statusCallbackUrl': self.status_callback_url,
            'statusCallbackMethod': self.status_callback_method,
            'stayAlone': self.stay_alone,
            'coachMode': self.coach_mode,
            'mute': self.mute,
            'hold': self.hold,
            'startMpcOnEnter': self.start_mpc_on_enter,
            'endMpcOnExit': self.end_mpc_on_exit,
            'enterSound': self.enter_sound,
            'enterSoundMethod': self.enter_sound_method,
            'exitSound': self.exit_sound,
            'exitSoundMethod': self.exit_sound_method,
            'onExitActionUrl': self.on_exit_action_url,
            'onExitActionMethod': self.on_exit_action_method,
            'relayDTMFInputs': self.relay_dtmf_inputs,
            'startRecordingAudio': self.start_recording_audio,
            'startRecordingAudioMethod': self.start_recording_audio_method,
            'stopRecordingAudio': self.stop_recording_audio,
            'stopRecordingAudioMethod': self.stop_recording_audio_method
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
