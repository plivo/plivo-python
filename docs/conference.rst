Conference
------------

This corresponds to the conference endpoint

https://www.plivo.com/docs/api/conference/

Provides these calls::

    #TODO: The should return list, currently return conference object.
    conferences = client.Conference.get_all(...)
    conferences = client.Conference.hang_all(...)
    conference = client.Conference.get(..)

    conference.hang()
    conference.record()
    conference.stop_record()




