Usage
-------------

Use the client to send the message.

Get your AUTH_ID and AUTH_TOKEN from the `Plivo Dashboard <https://www.plivo.com/dashboard/>`_.::


    import plivo

    auth_id = 'XXXXXXXXXXXXXXXXXXXX'
    auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

    client = plivo.RestAPI(auth_id, auth_token)

    params = {'src': '121212121212',
    'dst': '1212121212',
    'text': 'Hello World'
    }

    response = client.send_message(params)

``response`` is a two-tuple. The first element is a the HTTP status code from API and second elemnt is the decoded json response.


Alternatively you can also use::

    client = plivo.RestAPI(auth_id, auth_token)

    message = client.Message.send(src='1212121212', dst='123456789', text="Hello")

This returns an object of type ``Call`` which you can use to look up the response.
You can use ``response`` like this.::

    message.status_code #Get the http status. Will be 2XX for success.
    call.api_id #Any anything returned from the API.
    call.json_data #If you want the raw json response.

Similarly for call endpoint we have::

    call = client.Call.get(call_uuid="the_uuid") #Returns a Call object
    list_of_calls = client.Call.get_all() #Returns a list of call objects

Now you can interact with the ``call`` object as such.::

    call.hang()#Will call the RestApi.hangup_call under the hood.
    call.transfer()#Will call transfer_call under the hood.

While you can use the methods directly on the ``RestApi`` using the endpoint specific classes is the simpler and recommended method.

All the endpoints follow this pattern.

``get``, ``create`` and similar singual methods would create an object (of the correct subclass of PlivoResponse)
``get_all``, ``search`` and similar would create a list of objects (of the correct subclass of PlivoResponse)
object specific methods such as ``hang`` can be called directly on the object.

