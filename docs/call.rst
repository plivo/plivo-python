Call
------------

This corresponds to the call endpoint

https://www.plivo.com/docs/api/call/

Provides these methods

    1. get
    2. get_all
    3. send
    4. hang
    5. transfer

``.get`` returns object of type ``Call``.
``.get_all`` returns a list of ``Call`` objects.

You can use ``hang`` and ``transfer`` on a Call object.::


    call = client.Call.get(..)
    call.hang()

Alternatively this is valid too::

    client.Call.hang(call.call_uuid)


