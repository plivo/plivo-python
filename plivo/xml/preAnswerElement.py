import six

from plivo.xml import (PlayElement, PlivoXMLElement, SpeakElement, WaitElement,
                       map_type)


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
