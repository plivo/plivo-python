# plivo-python
The Plivo Python SDK makes it simpler to integrate communications into your Python applications using the Plivo REST API. Using the SDK, you will be able to make voice calls, send SMS and generate Plivo XML to control your call flows.

A new version `4.0b1` is released as a public beta and is now available on PyPI. Visit the [4.0 release branch](https://github.com/plivo/plivo-python/tree/4.0) to know more.

## Installation
Install the SDK using [pip](http://www.pip-installer.org/en/latest/)

    pip install plivo

Alternatively, you can download the source code from this repo and run

    python setup.py install

We recommend that you use [virtualenv](https://virtualenv.pypa.io/en/stable/) to manage and segregate your Python environments, instead of using `sudo` with your commands and overwriting dependencies.

If you are looking for the `4.0b1` version, you can install it using

    pip install --pre plivo

## Running Tests
Create a file named auth_secrets.py and give it your `AUTH_ID` and `AUTH_TOKEN`, and run

    python tests.py

## Examples

### Example code to make a call

```python
#!/usr/bin/env python

import plivo

auth_id = 'XXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

p = plivo.RestAPI(auth_id, auth_token)

params = {'to': '121212121212',
          'from': '1212121212',
          'ring_url': 'http://example.com/ring_url'
          'answer_url': 'http://example.com/answer_url',
          'hangup_url': 'http://example.com/hangup_url'
          }

response = p.make_call(params)

```

## Building docs
Run the following command to build docs (you should have sphinx installed.).

    cd docs
    make html
