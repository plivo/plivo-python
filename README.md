===========
Plivo Python Helper
===========


Example code to make a call
---------------------------

    #!/usr/bin/env python

    import plivo

    auth_id = 'XXXXXXXXXXXXXXXXXXXX'
    auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

    p = plivo.RestAPI(auth_id, auth_token)

    params = {'to': '121212121212',
    'from': '1212121212',
    'ring_url': 'http://example.com/ring_url',
    'answer_url': 'http://example.com/answer_url',
    'hangup_url': 'http://example.com/hangup_url'
    }

    response = p.make_call(params)


Running Tests
-----------------------

Create a file named auth_secrets.py and give it your `AUTH_ID` and `AUTH_TOKEN`.
Run `python tests.py`

Installation
-------------------

    pip install plivo


Building docs
-----------------------

    cd docs
    make html

(You should have sphinx installed.)
