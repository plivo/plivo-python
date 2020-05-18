from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement


class MultiPartyCallElement(PlivoXMLElement):
    _name = 'MultiPartyCall'
    _nestable = []

    @property
    def max_duration(self):
        return self.__max_duration

    @max_duration.setter
    def max_duration(self, value):
        self.__max_duration = int(value) if value is not None else None

    @validate_args(
        value=[
            of_type_exact(int),
            in_range(min_value=300, max_value=28800)
        ],
    )
    def set_max_duration(self, value):
        self.__max_duration = value
        return self

    @property
    def max_participants(self):
        return self.__max_participants

    @max_participants.setter
    def max_participants(self, value):
        self.__max_participants = int(value) if value is not None else None

    @validate_args(
        value=[
            of_type_exact(int),
            in_range(min_value=2, max_value=10)
        ],
    )
    def set_max_participants(self, value):
        self.__max_participants = value
        return self

    @property
    def wait_music_url(self):
        return self.__wait_music_url

    @wait_music_url.setter
    def wait_music_url(self, value):
        self.__wait_music_url = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_url
        ],
    )
    def set_wait_music_url(self, value):
        self.__wait_music_url = value
        return self

    @property
    def wait_music_method(self):
        return self.__wait_music_method

    @wait_music_method.setter
    def wait_music_method(self, value):
        self.__wait_music_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_wait_music_method(self, value):
        self.__wait_music_method = value
        return self

    @property
    def agent_hold_music_url(self):
        return self.__agent_hold_music_url

    @agent_hold_music_url.setter
    def agent_hold_music_url(self, value):
        self.__agent_hold_music_url = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_url
        ],
    )
    def set_agent_hold_music_url(self, value):
        self.__agent_hold_music_url = value
        return self

    @property
    def agent_hold_music_method(self):
        return self.__agent_hold_music_method

    @agent_hold_music_method.setter
    def agent_hold_music_method(self, value):
        self.__agent_hold_music_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_agent_hold_music_method(self, value):
        self.__agent_hold_music_method = value
        return self

    @property
    def customer_hold_music_url(self):
        return self.__customer_hold_music_url

    @customer_hold_music_url.setter
    def customer_hold_music_url(self, value):
        self.__customer_hold_music_url = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_url
        ],
    )
    def set_customer_hold_music_url(self, value):
        self.__customer_hold_music_url = value
        return self

    @property
    def customer_hold_music_method(self):
        return self.__customer_hold_music_method

    @customer_hold_music_method.setter
    def customer_hold_music_method(self, value):
        self.__customer_hold_music_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_customer_hold_music_method(self, value):
        self.__customer_hold_music_method = value
        return self

    @property
    def recording_callback_url(self):
        return self.__recording_callback_url

    @recording_callback_url.setter
    def recording_callback_url(self, value):
        self.__recording_callback_url = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_url
        ],
    )
    def set_recording_callback_url(self, value):
        self.__recording_callback_url = value
        return self

    @property
    def recording_callback_method(self):
        return self.__recording_callback_method

    @recording_callback_method.setter
    def recording_callback_method(self, value):
        self.__recording_callback_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_recording_callback_method(self, value):
        self.__recording_callback_method = value
        return self

    @property
    def status_callback_url(self):
        return self.__status_callback_url

    @status_callback_url.setter
    def status_callback_url(self, value):
        self.__status_callback_url = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_url
        ],
    )
    def set_status_callback_url(self, value):
        self.__status_callback_url = value
        return self

    @property
    def status_callback_method(self):
        return self.__status_callback_method

    @status_callback_method.setter
    def status_callback_method(self, value):
        self.__status_callback_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_status_callback_method(self, value):
        self.__status_callback_method = value
        return self

    @property
    def on_exit_action_url(self):
        return self.__on_exit_action_url

    @on_exit_action_url.setter
    def on_exit_action_url(self, value):
        self.__on_exit_action_url = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_url
        ],
    )
    def set_on_exit_action_url(self, value):
        self.__on_exit_action_url = value
        return self

    @property
    def on_exit_action_method(self):
        return self.__on_exit_action_method

    @on_exit_action_method.setter
    def on_exit_action_method(self, value):
        self.__on_exit_action_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_on_exit_action_method(self, value):
        self.__on_exit_action_method = value
        return self

    @property
    def record(self):
        return self.__record

    @record.setter
    def record(self, value):
        self.__record = bool(value) if not None else None

    @validate_args(
        value=[of_type_exact(bool)]
    )
    def set_record(self, value):
        self.__record = value
        return self

    @property
    def record_file_format(self):
        return self.__record_file_format

    @record_file_format.setter
    def record_file_format(self, value):
        self.__record_file_format = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('mp3', 'wav'), case_sensitive=False, case_type='lower')
        ]
    )
    def set_record_file_format(self, value):
        self.__record_file_format = value
        return self

    @property
    def status_callback_events(self):
        return self.__status_callback_events

    @status_callback_events.setter
    def status_callback_events(self, value):
        self.__status_callback_events = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            multi_is_in(('mpc-state-changes',
                         'participant-state-changes',
                         'participant-speak-events'),
                        case_sensitive=False,
                        make_lower_case=True)
        ]
    )
    def set_status_callback_events(self, value):
        self.__status_callback_events = value
        return self

    @property
    def stay_alone(self):
        return self.__stay_alone

    @stay_alone.setter
    def stay_alone(self, value):
        self.__stay_alone = bool(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(bool)
        ]
    )
    def set_stay_alone(self, value):
        self.__stay_alone = value
        return self

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('agent', 'supervisor', 'customer'), case_sensitive=False, case_type='lower')
        ]
    )
    def set_role(self, value):
        self.__role = value
        return self

    @property
    def coach_mode(self):
        return self.__coach_mode

    @coach_mode.setter
    def coach_mode(self, value):
        self.__coach_mode = bool(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(bool)
        ]
    )
    def set_coach_mode(self, value):
        self.__coach_mode = value
        return self

    @property
    def mute(self):
        return self.__mute

    @mute.setter
    def mute(self, value):
        self.__mute = bool(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(bool)
        ]
    )
    def set_mute(self, value):
        self.__mute = value
        return self

    @property
    def hold(self):
        return self.__hold

    @hold.setter
    def hold(self, value):
        self.__hold = bool(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(bool)
        ]
    )
    def set_hold(self, value):
        self.__hold = value
        return self

    @property
    def start_mpc_on_enter(self):
        return self.__start_mpc_on_enter

    @start_mpc_on_enter.setter
    def start_mpc_on_enter(self, value):
        self.__start_mpc_on_enter = bool(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(bool)
        ]
    )
    def set_start_mpc_on_enter(self, value):
        self.__start_mpc_on_enter = value
        return self

    @property
    def end_mpc_on_exit(self):
        return self.__end_mpc_on_exit

    @end_mpc_on_exit.setter
    def end_mpc_on_exit(self, value):
        self.__end_mpc_on_exit = bool(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(bool)
        ]
    )
    def set_end_mpc_on_exit(self, value):
        self.__end_mpc_on_exit = value
        return self

    @property
    def relay_dtmf_inputs(self):
        return self.__relay_dtmf_inputs

    @relay_dtmf_inputs.setter
    def relay_dtmf_inputs(self, value):
        self.__relay_dtmf_inputs = bool(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(bool)
        ]
    )
    def set_relay_dtmf_inputs(self, value):
        self.__relay_dtmf_inputs = value
        return self

    @property
    def enter_sound(self):
        return self.__enter_sound

    @enter_sound.setter
    def enter_sound(self, value):
        self.__enter_sound = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_plivo_sound
        ]
    )
    def set_enter_sound(self, value):
        self.__enter_sound = value
        return self

    @property
    def enter_sound_method(self):
        return self.__enter_sound_method

    @enter_sound_method.setter
    def enter_sound_method(self, value):
        self.__enter_sound_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_enter_sound_method(self, value):
        self.__enter_sound_method = value
        return self

    @property
    def exit_sound(self):
        return self.__exit_sound

    @exit_sound.setter
    def exit_sound(self, value):
        self.__exit_sound = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_plivo_sound
        ]
    )
    def set_exit_sound(self, value):
        self.__exit_sound = value
        return self

    @property
    def exit_sound_method(self):
        return self.__exit_sound_method

    @exit_sound_method.setter
    def exit_sound_method(self, value):
        self.__exit_sound_method = str(value) if not None else None

    @validate_args(
        value=[
            of_type_exact(six.text_type),
            is_in(('GET', 'POST'), case_sensitive=False)
        ]
    )
    def set_exit_sound_method(self, value):
        self.__exit_sound_method = value
        return self

    def __init__(
            self,
            content=None,
            max_duration=14400,
            max_participants=10,
            wait_music_url=None,
            wait_music_method='GET',
            agent_hold_music_url=None,
            agent_hold_music_method='GET',
            customer_hold_music_url=None,
            customer_hold_music_method='GET',
            recording_callback_url=None,
            recording_callback_method='GET',
            status_callback_url=None,
            status_callback_method='GET',
            on_exit_action_url=None,
            on_exit_action_method='POST',
            record=False,
            record_file_format='mp3',
            status_callback_events='mpc-state-changes,participant-state-changes',
            stay_alone=False,
            role=None,
            coach_mode=True,
            mute=False,
            hold=False,
            start_mpc_on_enter=True,
            end_mpc_on_exit=False,
            relay_dtmf_inputs=False,
            enter_sound='beep:1',
            enter_sound_method='GET',
            exit_sound='beep:2',
            exit_sound_method='GET'
    ):
        super(MultiPartyCallElement, self).__init__()
        self.content = content
        self.max_duration = max_duration
        self.max_participants = max_participants
        self.wait_music_url = wait_music_url
        self.wait_music_method = wait_music_method
        self.agent_hold_music_url = agent_hold_music_url
        self.agent_hold_music_method = agent_hold_music_method
        self.customer_hold_music_url = customer_hold_music_url
        self.customer_hold_music_method = customer_hold_music_method
        self.recording_callback_url = recording_callback_url
        self.recording_callback_method = recording_callback_method
        self.status_callback_url = status_callback_url
        self.status_callback_method = status_callback_method
        self.on_exit_action_url = on_exit_action_url
        self.on_exit_action_method = on_exit_action_method
        self.record = record
        self.record_file_format = record_file_format
        self.status_callback_events = status_callback_events
        self.stay_alone = stay_alone
        self.role = role
        self.coach_mode = coach_mode
        self.mute = mute
        self.hold = hold
        self.start_mpc_on_enter = start_mpc_on_enter
        self.end_mpc_on_exit = end_mpc_on_exit
        self.relay_dtmf_inputs = relay_dtmf_inputs
        self.enter_sound = enter_sound
        self.enter_sound_method = enter_sound_method
        self.exit_sound = exit_sound
        self.exit_sound_method = exit_sound_method
