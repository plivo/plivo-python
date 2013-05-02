Number
------------

This corresponds to the Number endpoint

https://www.plivo.com/docs/api/number/

This class provides the following methods:

1. get
2. get_all
3. search
4. rent

You can call them as::

    number = client.Number.get(...) #Returns details of a sepcific Number
    numbers = client.Number.get_all(...) #Returns a list of currently rented numbers
    number = client.Number.search(...) #Returns a list of number you can rent

You can rent a number found in ``search`` by::

    number.rent()

Alternatively this works too.::

    client.Number.rent(number)

