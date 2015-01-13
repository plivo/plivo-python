import xml.etree.ElementTree as etree

class PlivoError(Exception):
    pass


class Element(object):
    nestables = ()
    valid_attributes = ()

    def __init__(self, body='', **attributes):
        self.attributes = {}
        self.name = self.__class__.__name__
        self.body = unicode(body).encode('ascii', 'xmlcharrefreplace')
        self.node = None
        for k, v in attributes.iteritems():
            if not k in self.valid_attributes:
                raise PlivoError('invalid attribute %s for %s' % (k, self.name))
            self.attributes[k] = self._convert_value(v)
        self.node = etree.Element(self.name, attrib=self.attributes)
        if self.body:
            self.node.text = self.body

    @staticmethod
    def _convert_value(v):
        if v is True:
            return u'true'
        elif v is False:
            return u'false'
        elif v is None:
            return u'none'
        elif v == 'get':
            return u'GET'
        elif v == 'post':
            return u'POST'
        return unicode(v)

    def add(self, element):
        if element.name in self.nestables:
            self.node.append(element.node)
            return element
        raise PlivoError('%s not nestable in %s' % (element.name, self.name))

    def to_xml(self):
        return etree.tostring(self.node, encoding="utf-8")

    def __str__(self):
        return self.to_xml()

    def __repr__(self):
        return self.to_xml()

    def addSpeak(self, body, **kwargs):
        return self.add(Speak(body, **kwargs))

    def addPlay(self, body, **kwargs):
        return self.add(Play(body, **kwargs))

    def addGetDigits(self, **kwargs):
        return self.add(GetDigits(**kwargs))

    def addRecord(self, **kwargs):
        return self.add(Record(**kwargs))

    def addDial(self, **kwargs):
        return self.add(Dial(**kwargs))

    def addNumber(self, body, **kwargs):
        return self.add(Number(body, **kwargs))

    def addUser(self, body, **kwargs):
        return self.add(User(body, **kwargs))

    def addRedirect(self, body, **kwargs):
        return self.add(Redirect(body, **kwargs))

    def addWait(self, **kwargs):
        return self.add(Wait(**kwargs))

    def addHangup(self, **kwargs):
        return self.add(Hangup(**kwargs))

    def addPreAnswer(self, **kwargs):
        return self.add(PreAnswer(**kwargs))

    def addConference(self, body, **kwargs):
        return self.add(Conference(body, **kwargs))

    def addMessage(self, body, **kwargs):
        return self.add(Message(body, **kwargs))

    def addDTMF(self, body, **kwargs):
        return self.add(DTMF(body, **kwargs))

class Response(Element):
    nestables = ('Speak', 'Play', 'GetDigits', 'Record', 'Dial', 'Message',
                 'Redirect', 'Wait', 'Hangup', 'PreAnswer', 'Conference', 'DTMF')
    valid_attributes = ()

    def __init__(self):
        Element.__init__(self, body='')


class Speak(Element):
    nestables = ()
    valid_attributes = ('voice', 'language', 'loop')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No text set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Play(Element):
    nestables = ()
    valid_attributes = ('loop')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No url set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Wait(Element):
    nestables = ()
    valid_attributes = ('length', 'silence', 'min_silence', 'minSilence', 'beep')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Redirect(Element):
    nestables = ()
    valid_attributes = ('method')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No url set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Hangup(Element):
    nestables = ()
    valid_attributes = ('schedule', 'reason')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class GetDigits(Element):
    nestables = ('Speak', 'Play', 'Wait')
    valid_attributes = ('action', 'method', 'timeout', 'digitTimeout', 'finishOnKey',
                        'numDigits', 'retries', 'invalidDigitsSound', 'validDigits',
                        'playBeep', 'redirect', 'digitTimeout', 'log')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Number(Element):
    nestables = ()
    valid_attributes = ('sendDigits', 'sendOnPreanswer', 'sendDigitsMode')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No number set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class User(Element):
    nestables = ()
    valid_attributes = ('sendDigits', 'sendOnPreanswer', 'sipHeaders',
                        'webrtc')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No user set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Dial(Element):
    nestables = ('Number', 'User')
    valid_attributes = ('action','method','timeout','hangupOnStar',
                        'timeLimit','callerId', 'callerName', 'confirmSound',
                        'dialMusic', 'confirmKey', 'redirect',
                        'callbackUrl', 'callbackMethod', 'digitsMatch',
                        'sipHeaders')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Conference(Element):
    nestables = ()
    valid_attributes = ('muted','beep','startConferenceOnEnter',
                        'endConferenceOnExit','waitSound','enterSound', 'exitSound',
                        'timeLimit', 'hangupOnStar', 'maxMembers',
                        'record', 'recordFileFormat','recordWhenAlone', 'action', 'method', 'redirect',
                        'digitsMatch', 'callbackUrl', 'callbackMethod', 'relayDTMF',
                        'stayAlone', 'floorEvent', 'transcriptionType', 'transcriptionUrl',
                        'transcriptionMethod')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No conference name set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Record(Element):
    nestables = ()
    valid_attributes = ('action', 'method', 'timeout','finishOnKey',
                        'maxLength', 'playBeep', 'recordSession',
                        'startOnDialAnswer', 'redirect', 'fileFormat',
                        'callbackUrl', 'callbackMethod', 'transcriptionType',
                        'transcriptionUrl', 'transcriptionMethod')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class PreAnswer(Element):
    nestables = ('Play', 'Speak', 'GetDigits', 'Wait', 'Redirect', 'Message', 'DTMF')
    valid_attributes = ()

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Message(Element):
    nestables = ()
    valid_attributes = ('src', 'dst', 'type', 'callbackUrl', 'callbackMethod')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No text set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class DTMF(Element):
    nestables = ()
    valid_attributes = ('async',)

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No digits set for %s' % self.name)
        Element.__init__(self, body, **attributes)
