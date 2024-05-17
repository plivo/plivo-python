# plivo-python

[![UnitTests](https://github.com/plivo/plivo-python/actions/workflows/unitTests.yml/badge.svg?branch=master)](https://github.com/plivo/plivo-python/actions/workflows/unitTests.yml)
[![PyPI](https://img.shields.io/pypi/v/plivo.svg)](https://pypi.python.org/pypi/plivo)
[![PyPI](https://img.shields.io/pypi/pyversions/plivo.svg)](https://pypi.python.org/pypi/plivo)
[![codecov](https://codecov.io/gh/plivo/plivo-python/branch/master/graph/badge.svg)](https://codecov.io/gh/plivo/plivo-python)
[![PyPI](https://img.shields.io/pypi/l/plivo.svg)](https://pypi.python.org/pypi/plivo)


The Plivo Python SDK makes it simpler to integrate communications into your Python applications using the Plivo REST API. Using the SDK, you will be able to make voice calls, send SMS and generate Plivo XML to control your call flows.

## Installation
Install the SDK using [pip](http://www.pip-installer.org/en/latest/)

    pip install plivo

If you have the `0.11.3` version (a.k.a legacy) already installed, you will have to first uninstall it before installing the new version. `pip install --upgrade plivo` might not work depending on your system status.

Alternatively, you can download the source code from this repo(master branch) and run

    python setup.py install

For features in beta, use the beta branch:

    pip install plivo==4.2.0b1
    
Alternatively, you can download the source code from this repo(beta branch) and run

    python setup.py install

We recommend that you use [virtualenv](https://virtualenv.pypa.io/en/stable/) to manage and segregate your Python environments, instead of using `sudo` with your commands and overwriting dependencies.

## Getting started

### Authentication
To make the API requests, you need to create a `RestClient` and provide it with authentication credentials (which can be found at [https://manage.plivo.com/dashboard/](https://manage.plivo.com/dashboard/)).

We recommend that you store your credentials in the `PLIVO_AUTH_ID` and the `PLIVO_AUTH_TOKEN` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialise the client with no arguments and it will automatically fetch them from the environment variables:

```python
import plivo

client = plivo.RestClient()
```
Alternatively, you can specifiy the authentication credentials while initializing the `RestClient`.

```python
import plivo

client = plivo.RestClient(auth_id='your_auth_id', auth_token='your_auth_token')
```

If you expect to make a large number of API requests, re-use the same client instance, but if you expect to create a client on an on-demand basis, you can use a context manager to automatically frees all resources used by the client

```python
import plivo

with plivo.RestClient() as client:
  pass # Do something with the client
```

### The basics
The SDK uses consistent interfaces to create, retrieve, update, delete and list resources. The pattern followed is as follows:

```python
client.resources.create(*args, **kwargs) # Create
client.resources.get(id=resource_identifier) # Get
client.resources.update(id=resource_identifier, *args, **kwargs) # Update
client.resources.delete(id=resource_identifier) # Delete
client.resources.list() # List all resources, max 20 at a time
```

You can also use the `resource` directly to update and delete it. For example,

```python
resource = client.resources.get(id=resource_identifier)
resource.update(*args, **kwargs) # update the resource
resource.delete() # Delete the resource
```

Also, using `client.resources.list()` would list the first 20 resources by default (which is the first page, with `limit` as 20, and `offset` as 0). To get more, you will have to use `limit` and `offset` to get the second page of resources.

To list all resources, you can simply use the following pattern that will handle the pagination for you automatically, so you won't have to worry about passing the right `limit` and `offset` values.

```python
for resource in client.resources:
    print(resource.id)
```

## Examples

### Send a message

```python
import plivo

client = plivo.RestClient()
message_created = client.messages.create(
    src='the_source_number',
    dst='the_destination_number',
    text='Hello, world!'
)

```

### Make a call

```python
import plivo

client = plivo.RestClient()
call_made = client.calls.create(
    from_='the_from_number',
    to_='the_to_number',
    answer_url='https://answer.url'
)

```

### Lookup a number

```python
import plivo

client = plivo.RestClient(auth_id='', auth_token='')
resp = client.lookup.get("<insert-number-here>")
print(resp)
```

### Generate Plivo XML

```python
from plivo import plivoxml

xml_response = plivoxml.ResponseElement()
xml_response.add_speak('Hello, world!') # or add(plivoxml.SpeakElement(text))

print(xml_response.to_string())
```

This generates the following XML:

```xml
<Response>
  <Speak>Hello, world!</Speak>
</Response>
```

### Run a PHLO

```python
import plivo

auth_id = '<auth_id>'
auth_token = '<auth_token>'
phlo_id = '<phlo_id' # https://console.plivo.com/phlo/list/
phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
phlo = phlo_client.phlo.get(phlo_id)
response = phlo.run()
print(response)
```

## WhatsApp Messaging
Plivo's WhatsApp API allows you to send different types of messages over WhatsApp, including templated messages, free form messages and interactive messages. Below are some examples on how to use the Plivo Go SDK to send these types of messages.

### Templated Messages
Templated messages are a crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversation with their customers using templated messages.

WhatsApp templates support 4 components:  `header` ,  `body`,  `footer`  and `button`. At the point of sending messages, the template object you see in the code acts as a way to pass the dynamic values within these components.  `header`  can accomodate `text` or `media` (images, video, documents) content.  `body`  can accomodate text content.  `button`  can support dynamic values in a `url` button or to specify a developer-defined payload which will be returned when the WhatsApp user clicks on the `quick_reply` button. `footer`  cannot have any dynamic variables.

Example:
```python
import plivo
from plivo.utils.template import Template

client = plivo.RestClient('<auth_id>','<auth_token>')

template=Template(**{ 
            "name": "template_name",
            "language": "en_US",
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "media",
                            "media": "https://xyz.com/s3/img.jpg"
                        }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": "WA-Text"
                        }
                    ]
                }
            ]
          }
       )
response = client.messages.create(   
        src="the_from_number",
        dst="the_to_number",
        type_="whatsapp",
        template=template,
        url="https://foo.com/wa_status/"
    )
print(response)
```

### Free Form Messages
Non-templated or Free Form WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

#### Free Form Text Message
Example:
```python
import plivo
client = plivo.RestClient('<auth_id>','<auth_token>')
response = client.messages.create(
         src="the_from_number",
         dst="the_to_number",
         type_="whatsapp",
         text="Hello, from Python!"
       )
print(response)
```

#### Free Form Media Message
Example:
```python
import plivo
client = plivo.RestClient('<auth_id>','<auth_token>')
response = client.messages.create(
         src="the_from_number",
         dst="the_to_number",
         type_="whatsapp",
         text="whatsapp_video",
         media_urls=["https://sample-videos.com/img/Sample-png-image-1mb.png"]
        )
print(response)
```

### Interactive Messages
This guide shows how to send non-templated interactive messages to recipients using Plivo’s APIs.

#### Quick Reply Buttons
Quick reply buttons allow customers to quickly respond to your message with predefined options.

Example:
```python
import plivo
from plivo.utils.interactive import Interactive

client = plivo.RestClient('<auth_id>','<auth_token>')

interactive=Interactive(**{
        "type": "button",
        "header": {
            "type": "media",
            "media": "https://xyz.com/s3/img.jpg"
        },
        "body": {
            "text": "Make your selection"
        },
        "action": {
            "buttons": [
                {
                    "title": "Click here",
                    "id": "bt1"
                },
                {
                    "title": "Know More",
                    "id": "bt2"
                },
                {
                    "title": "Request Callback",
                    "id": "bt3"
                }
            ]
        }
    })

response= client.messages.create(
    src="the_from_number",
    dst="the_to_number",
    type_="whatsapp",
    interactive=interactive
)
print(response)
```

#### Interactive Lists
Interactive lists allow you to present customers with a list of options.

Example:
```python
import plivo
from plivo.utils.interactive import Interactive

client = plivo.RestClient('<auth_id>','<auth_token>')

interactive=Interactive(**{
        "type": "list",
        "header": {
            "type": "text",
            "text": "Welcome to Plivo"
        },
        "body": {
            "text": "You can review the list of rewards we offer"
        },
        "footer": {
            "text": "Yours Truly"
        },
        "action": {
            "buttons": [{
                "title": "Click here"
            }],
            "sections": [
                {
                    "title": "SECTION_1_TITLE",
                    "rows": [
                        {
                            "id": "SECTION_1_ROW_1_ID",
                            "title": "SECTION_1_ROW_1_TITLE",
                            "description": "SECTION_1_ROW_1_DESCRIPTION"
                        },
                        {
                            "id": "SECTION_1_ROW_2_ID",
                            "title": "SECTION_1_ROW_2_TITLE",
                            "description": "SECTION_1_ROW_2_DESCRIPTION"
                        }
                    ]
                },
                {
                    "title": "SECTION_2_TITLE",
                    "rows": [
                        {
                            "id": "SECTION_2_ROW_1_ID",
                            "title": "SECTION_2_ROW_1_TITLE",
                            "description": "SECTION_2_ROW_1_DESCRIPTION"
                        },
                        {
                            "id": "SECTION_2_ROW_2_ID",
                            "title": "SECTION_2_ROW_2_TITLE",
                            "description": "SECTION_2_ROW_2_DESCRIPTION"
                        }
                    ]
                }
            ]
        }
    })

response= client.messages.create(
    src="the_from_number",
    dst="the_to_number",
    type_="whatsapp",
    interactive=interactive
)
print(response)
```

#### Interactive CTA URLs
CTA URL messages allow you to send links and call-to-action buttons.

Example:
```python
import plivo
from plivo.utils.interactive import Interactive

client = plivo.RestClient('<auth_id>','<auth_token>')

interactive=Interactive(**{
        "type": "cta_url",
        "header": {
            "type": "media",
            "media": "https://xyz.com/s3/img.jpg"
        },
        "body": {
            "text": "Know More"
        },
        "footer": {
            "text": "Plivo"
        },
        "action": {
            "buttons": [
                {
                    "title": "Click here",
                    "cta_url": "https:plivo.com"
                }
            ]
        }
    })

response= client.messages.create(
    src="the_from_number",
    dst="the_to_number",
    type_="whatsapp",
    interactive=interactive
)
print(response)
```

### Location Messages
This guide shows how to send templated and non-templated location messages to recipients using Plivo’s APIs.

#### Templated Location Messages
Example:
```python
import plivo
from plivo.utils.template import Template

client = plivo.RestClient('<auth_id>','<auth_token>')

template=Template(**{
        "name": "plivo_order_pickup",
        "language": "en_US",
        "components": [
            {
                "type": "header",
                "parameters": [
                    {
                        "type": "location",
                        "location": {
                            "longitude": "122.148981",
                            "latitude": "37.483307",
                            "name": "Pablo Morales",
                            "address": "1 Hacker Way, Menlo Park, CA 94025"
                        }
                    }
                ]
            }
        ]
    })

response= client.messages.create(
    src="the_from_number",
    dst="the_to_number",
    type_="whatsapp",
    template=template
)
print(response)
```

#### Non-Templated Location Messages
Example:
```python
import plivo
from plivo.utils.location import Location

client = plivo.RestClient('<auth_id>','<auth_token>')

location=Location(**{
        "longitude": "122.148981",
        "latitude": "37.483307",
        "name": "Pablo Morales",
        "address": "1 Hacker Way, Menlo Park, CA 94025"
    })

response= client.messages.create(
    src="the_from_number",
    dst="the_to_number",
    type_="whatsapp",
    location=location
)
print(response)
```

### More examples
Refer to the [Plivo API Reference](https://api-reference.plivo.com/latest/python/introduction/overview) for more examples. Also refer to the [guide to setting up dev environment](https://developers.plivo.com/getting-started/setting-up-dev-environment/) on [Plivo Developers Portal](https://developers.plivo.com) to setup a Flask server & use it to test out your integration in under 5 minutes. to get started with Plivo.

## Reporting issues
Report any feedback or problems with this version by [opening an issue on Github](https://github.com/plivo/plivo-python/issues).
