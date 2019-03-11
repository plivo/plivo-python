# Change Log

## [4.2.0b1](https://github.com/plivo/plivo-python/tree/v4.2-beta1) (2018-03-11)
- Add PHLO support in Beta branch 

## [4.2.0a4](https://github.com/plivo/plivo-python/tree/v4.2-alpha3) (2018-10-23)
- Fix PHLO run params 

## [4.2.0a3](https://github.com/plivo/plivo-python/tree/v4.2-alpha3) (2018-08-08)
- Support python3.7
- Add PHLO run function

## [4.2.0a2](https://github.com/plivo/plivo-python/tree/v4.2-alpha2) (2018-08-03)
- Fix PHLO Url and component name

## [4.2.0a1](https://github.com/plivo/plivo-python/tree/v4.2-alpha1) (2018-08-03)
- Add PHLO support in alpha release

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
