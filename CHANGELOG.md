# Change Log

## [4.1.5](https://github.com/plivo/plivo-python/tree/v4.1.5) (2018-11-21)
- Add hangup party details to CDR. CDR filtering allowed by hangup_source and hangup_cause_code.
- Add sub-account cascade delete support.

## [4.1.4](https://github.com/plivo/plivo-python/tree/v4.1.4) (2018-10-31)
- Add live calls filtering by to, from numbers and call direction. 

## [4.1.3](https://github.com/plivo/plivo-python/tree/v4.1.3) (2018-09-18)
- Add python3.7 support
- Add support to get queued calls
- Add powerpack support
- Add support for filter of parent call UUID
- Add log_incoming_messages support

## [4.1.1](https://github.com/plivo/plivo-python/tree/v4.1.1) (2018-06-29)
- Added limit & offset parameters to endpoint list api

## [4.1.0](https://github.com/plivo/plivo-python/tree/v4.1.0) (2018-02-26)
- Add Address and Identity resources
- Change a few functions in numbers.py to support the verification flows

## [4.0.0](https://github.com/plivo/plivo-python/tree/v4.0.0) (2018-01-18)
- Supports specifying timeouts and proxies while client initialization
- A few bug fixes (#35, #36, #39 & #40)

## [4.0.0b1](https://github.com/plivo/plivo-python/tree/v4.0-beta1) (2017-10-23)
- The new SDK works with both Python 2 & 3
- JSON serialization and deserialization is now handled by the SDK
- The API interfaces are consistent and guessable
- Handles pagination automatically when listing all objects of a resource

## [0.11.3](https://github.com/plivo/plivo-python/tree/0.11.3) (2016-11-02)
- Reverts back method `validate_request_signature(uri, signature, auth_token, params=None)` to `validate_signature(uri, post_params, signature, auth_token)`
- Has a fix for `validate_signature` when POST params contain unicode strings.

## [0.11.2](https://github.com/plivo/plivo-python/tree/v0.11.2) (2016-10-28)
- This release changes method `validate_signature(uri, post_params, signature, auth_token)` to `validate_request_signature(uri, signature, auth_token, params=None)`

## [0.11.1](https://github.com/plivo/plivo-python/tree/v0.11.1) (2016-06-02)
- Merge pull request #19 from plivo/add_param_dial_xml
- Added `digitsMatchBLeg` parameter to Dial XML

## [0.11.0](https://github.com/plivo/plivo-python/tree/v11.0) (2015-10-27)
- Compatible with python3. Typo with the tag. This is v0.11.0 and NOT v11.0

## [0.10.3](https://github.com/plivo/plivo-python/tree/v0.10.3) (2015-10-08)
- `stop_speak_member` function added

## Other changes
- 2014-01-14: Adds support for PhoneNumber API & Adds beep parameter for Wait element
- 2013-09-25: Missing minSilence for <Wait>
- 2013-09-25: Added relayDTMF to <Conference> and async to <DTMF>
- 2013-02-23: pricing API added
