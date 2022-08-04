# Change Log

## [4.25.0](https://github.com/plivo/plivo-python/tree/v4.25.0) (2022-07-29)
**Feature - Token Creation**
- `JWT Token Creation API` added API to create a new JWT token.

## [4.24.1](https://github.com/plivo/plivo-python/tree/v4.24.1) (2022-05-16)
**Bug Fix - Asynchronous Flow Added**
- `callback_url` and `callback_method` added in API's [Asynchronous requests](https://www.plivo.com/docs/voice/api/request#asynchronous-request)

## [4.24.0](https://github.com/plivo/plivo-python/tree/v4.24.0) (2022-05-05)
**Feature - List all recordings and The MultiPartyCall element**
- `from_number` and `to_number` added to filtering param [List all recordings](https://www.plivo.com/docs/voice/api/recording#list-all-recordings)
- `record_min_member_count` param added to [Add a participant to a multiparty call using API](https://www.plivo.com/docs/voice/api/multiparty-call/participants#add-a-participant)

## [4.23.0](https://github.com/plivo/plivo-python/tree/v4.23.0) (2022-03-18)
**Feature - DialElement**
- `confirmTimeout` parameter added to [The Dial element](https://www.plivo.com/docs/voice/xml/dial/) 

## [4.22.3](https://github.com/plivo/plivo-python/tree/v4.22.3) (2022-03-04)
**Bug fix - Application API (create/update)**
- For [create & update application API](https://www.plivo.com/docs/account/api/application#create-an-application) the parameter `answer url` is set to optional. 
- Failing to [update application](https://www.plivo.com/docs/account/api/application#update-an-application) because of `app_id`

## [4.22.2](https://github.com/plivo/plivo-python/tree/v4.22.2) (2022-02-25)
**Feature - conference_recording**
- Add callback_url parameter to [Record Conference API](https://www.plivo.com/docs/voice/api/conference/record-conference#start-recording-a-conference)

## [4.22.1](https://github.com/plivo/plivo-python/tree/v4.22.1) (2022-02-10)
**Feature - EndpointUpdated**
- neglecting endpoint_id in to_param_dict function

## [4.22.0](https://github.com/plivo/plivo-python/tree/v4.22.0) (2022-01-27)
**Feature - MPCStartCallRecording**
- parameter change from statusCallback to recordingCallback

## [4.21.0](https://github.com/plivo/plivo-python/tree/v4.21.0) (2021-12-14)
**Feature - Voice**
- Routing SDK traffic through Akamai endpoints for all the [Voice APIs](https://www.plivo.com/docs/voice/api/overview/)

## [4.20.0](https://github.com/plivo/plivo-python/tree/v4.20.0) (2021-12-02)
**Features - Messaging: 10 DLC API**
- 10 DLC API's for brand and campaign support.

## [4.19.1](https://github.com/plivo/plivo-python/tree/v4.19.1) (2021-11-30)
**Bug fix**
- Library `PyJWT` version mismatch in setup.py compared with requirement.txt.

## [4.19.0](https://github.com/plivo/plivo-python/tree/v4.19.0) (2021-11-25)
**Features - Voice: Multiparty calls**
- The [Add Multiparty Call API](https://www.plivo.com/docs/voice/api/multiparty-call/participants#add-a-participant) allows for greater functionality by accepting options like `start recording audio`, `stop recording audio`, and their HTTP methods.
- [Multiparty Calls](https://www.plivo.com/docs/voice/api/multiparty-call/) now has new APIs to `stop` and `play` audio.

## [4.18.1](https://github.com/plivo/plivo-python/tree/v4.18.1) (2021-07-16)
- Updates to [add a member a multi-party call API](https://www.plivo.com/docs/voice/api/multiparty-call/participants#add-a-participant).
  - Remove validation range for `delay` and `ringtimeout` parameters.
  - Add appropriate error message for multiple `ringtimeout` and `delaydial` values.
  - Fix the agent limit validation bug so that it only checks when multiple `to` param values are supplied.
  - Fix the multiparty call and other voice API UT's.

## [4.18.0](https://github.com/plivo/plivo-python/tree/v4.18.0) (2021-07-13)
- Power pack ID has been included to the response for the [list all messages API](https://www.plivo.com/docs/sms/api/message/list-all-messages/) and the [get message details API](https://www.plivo.com/docs/sms/api/message#retrieve-a-message).
- Support for filtering messages by Power pack ID has been added to the [list all messages API](https://www.plivo.com/docs/sms/api/message#list-all-messages).

## [4.17.0](https://github.com/plivo/plivo-python/tree/v4.17.0) (2021-07-07)
- Add SDK support for MPC enhancements.

## [4.16.2](https://github.com/plivo/plivo-python/tree/v4.16.2) (2021-06-17)
- Fix exception during 400 bad request.

## [4.16.1](https://github.com/plivo/plivo-python/tree/v4.16.1) (2021-05-05)
- Fixing trivis build issue.

## [4.16.0](https://github.com/plivo/plivo-python/tree/v4.16.0) (2021-04-19)
- Added SDK support for Multiparty Call APIs and XML.

## [4.15.3](https://github.com/plivo/plivo-python/tree/v4.15.2) (2021-03-10)
- Add "npanxx" and "local_calling_area" support for Search Phone Number.

## [4.15.2](https://github.com/plivo/plivo-python/tree/v4.15.2) (2020-12-14)
- Fix "Cannot import name 'encodestring' from 'base64'" error for Signature Validation-V2.

## [4.15.1](https://github.com/plivo/plivo-python/tree/v4.15.1) (2020-11-17)
- Fix resource not found exception when making sequential requests.

## [4.15.0](https://github.com/plivo/plivo-python/tree/v4.15.0) (2020-11-17)
- Add number_priority support for Powerpack API.

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
