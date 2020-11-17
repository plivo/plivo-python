# Change Log

## [4.14.0](https://github.com/plivo/plivo-python/tree/v4.14.0) (2020-11-05)
- Add Regulatory Compliance API Support.

## [4.13.0](https://github.com/plivo/plivo-python/tree/v4.13.0) (2020-10-23)
- Change lookup API endpoint and response.

## [4.12.0](https://github.com/plivo/plivo-python/tree/v4.12.0) (2020-10-06)
- Add lookup API support.

## [4.11.0](https://github.com/plivo/plivo-python/tree/v4.11.0) (2020-09-24)
- Add "public_uri" optional param support for Application API.

## [4.10.2](https://github.com/plivo/plivo-python/tree/v4.10.2) (2020-09-14)
- Fix GET callback_method for Start Recording API.

## [4.10.1](https://github.com/plivo/plivo-python/tree/v4.10.1) (2020-09-11)
- Fix Play in calls for asynchronous requests.

## [4.10.0](https://github.com/plivo/plivo-python/tree/v4.10.0) (2020-08-24)
- Add Powerpack for MMS.

## [4.9.0](https://github.com/plivo/plivo-python/tree/v4.8.1) (2020-07-21)
- Add retries to other regions for voice requests.

## [4.8.1](https://github.com/plivo/plivo-python/tree/v4.8.1) (2020-06-12)
- Fix SMS Test cases.

## [4.8.0](https://github.com/plivo/plivo-python/tree/v4.8.0) (2020-05-28)
- Add JWT helper functions.

## [4.7.0](https://github.com/plivo/plivo-python/tree/v4.7.0) (2020-04-29)
- Add V3 signature helper functions.

## [4.6.1](https://github.com/plivo/plivo-python/tree/v4.6.1) (2020-03-31)
- Add Nonetype check for API requests.

## [4.6.0](https://github.com/plivo/plivo-python/tree/v4.6.0) (2020-03-31)
- Add application cascade delete support.

## [4.5.0](https://github.com/plivo/plivo-python/tree/v4.5.0) (2020-03-30)
- Add Tollfree support for Powerpack

## [4.4.0](https://github.com/plivo/plivo-python/tree/v4.4.0) (2020-03-27)
- Add post call quality feedback API support.

## [4.3.8](https://github.com/plivo/plivo-python/tree/v4.3.8) (2020-02-25)
- Add Media support

## [4.3.7](https://github.com/plivo/plivo-python/tree/v4.3.7) (2020-02-19)
- Add city and mms filter support for Number Search API

## [4.3.6](https://github.com/plivo/plivo-python/tree/v4.3.6) (2019-12-20)
- Add Powerpack support

## [4.3.5](https://github.com/plivo/plivo-python/tree/v4.3.5) (2019-12-04)
- Add MMS support

## [4.3.4](https://github.com/plivo/plivo-python/tree/v4.3.4) (2019-11-13)
- Add GetInput XML support

## [4.3.3](https://github.com/plivo/plivo-python/tree/v4.3.3) (2019-11-13)
- Fix Bulk call API

## [4.3.2](https://github.com/plivo/plivo-python/tree/v4.3.2) (2019-07-04)
- Add SSML support

## [4.3.1](https://github.com/plivo/plivo-python/tree/v4.3.1) (2019-03-13)
- Fix PHLO import error

## [4.3.0](https://github.com/plivo/plivo-python/tree/v4.3.0) (2019-03-11)
- Add PHLO support
- Add Multi-party call triggers

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
