import six


def map_type(val):
    if isinstance(val, bool):
        return six.text_type(val).lower()
    return six.text_type(val)
