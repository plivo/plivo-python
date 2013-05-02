Carrier
------------

This corresponds to the application endpoint

https://www.plivo.com/docs/api/carrier/incoming/

Provides these calls::

    carrier = client.Carrier.create(..)
    carrier = client.Carrier.get(..)
    carriers = client.Carrier.get_all()#Gets the list of all carriers
    carrier.delete()
    carrier.modify(...)