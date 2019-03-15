from unittest import TestCase

from plivo import plivoxml


class SElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><S><Break strength="strong" time="250ms">This is Test</Break><Emphasis level="strong">This is Test</Emphasis><Lang xmllang="it">This is Test</Lang><Phoneme alphabet="ipa" ph="t&amp;#x259;mei&amp;#x325;&amp;#x27E;ou&amp;#x325;">This is Test</Phoneme><Prosody pitch="low" rate="x-high" volume="+6dB">This is Test</Prosody><SayAs format="" interpret_as="spell-out">This is Test</SayAs><Sub alias="World Wide Web Consortium">This is Test</Sub><W role="claws:VV0">This is Test</W></S></Response>'

        content_break = 'This is Test'
        strength_break = 'strong'
        time_break = '250ms'

        content_lang = 'This is Test'
        xmllang_lang = "it"

        content_emphasis = 'This is Test'
        level_emphasis = 'strong'

        content_phoneme = 'This is Test'
        alphabet_phoneme = "ipa"
        ph_phoneme = "t&#x259;mei&#x325;&#x27E;ou&#x325;"

        content_prosody = "This is Test"
        volume_prosody = "+6dB"
        rate_prosody = "x-high"
        pitch_prosody = "low"

        content_say_as = 'This is Test'
        interpret_as_say_as = "spell-out"
        # TODO: need to ask the value
        format_say_as = ""

        content_sub = "This is Test"
        alias_sub = "World Wide Web Consortium"

        content_w = "This is Test"
        role_w = "claws:VV0"

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SElement().add_break(
                content_break, strength=strength_break, time=time_break
            ).add_emphasis(
                content_emphasis,
                level=level_emphasis
            ).add_lang(
                content_lang,
                xmllang=xmllang_lang
            ).add_phoneme(
                content_phoneme,
                alphabet=alphabet_phoneme,
                ph=ph_phoneme
            ).add_prosody(
                content_prosody,
                volume=volume_prosody,
                rate=rate_prosody,
                pitch=pitch_prosody
            ).add_say_as(
                content_say_as,
                interpret_as=interpret_as_say_as,
                format=format_say_as
            ).add_sub(
                content_sub,
                alias=alias_sub,
            ).add_w(
                content_w,
                role_w
            )
        ).to_string()
        self.assertEqual(response, expected_response + '\n')
