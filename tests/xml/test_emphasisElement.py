from unittest import TestCase

from plivo import plivoxml


class EmphasisElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Speak><emphasis level="strong"><break strength="strong"/>' \
                            '<lang xml:lang="it">This is Test</lang><emphasis level="strong">' \
                            'This is Test</emphasis><phoneme alphabet="ipa" ph="t&amp;#x259;mei&amp;#x325;' \
                            '&amp;#x27E;ou&amp;#x325;">This is Test</phoneme><prosody pitch="low">' \
                            'This is Test</prosody><say-as format="" interpret-as="spell-out">' \
                            'This is Test</say-as><sub alias="World Wide Web Consortium">This is Test' \
                            '</sub><w role="claws:VV0">This is Test</w></emphasis></Speak></Response>'
        level = "strong"
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
        format_say_as = ""

        content_sub = "This is Test"
        alias_sub = "World Wide Web Consortium"

        content_w = "This is Test"
        role_w = "claws:VV0"

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SpeakElement("").add(
                plivoxml.EmphasisElement().set_level(level).add_break(
                    strength=strength_break
                ).add_lang(
                    content_lang,
                    xmllang=xmllang_lang
                ).add_emphasis(
                    content_emphasis,
                    level=level_emphasis
                ).add_phoneme(
                    content_phoneme,
                    alphabet=alphabet_phoneme,
                    ph=ph_phoneme
                ).add_prosody(
                    content_prosody,
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
            )
        ).to_string(False)
        self.assertEqual(response, expected_response)
