# -*- coding: utf-8 -*-
import functools
import io
import json
import os


def with_response(status_code, method_name=None):
    def wrapper(func):
        @functools.wraps(func)
        def decorator(self, *args, **kwargs):
            name = method_name or func.__name__.replace('test_', '')
            name = self.__class__.__name__.replace('Test', '') + name.replace(
                '_', ' ').title().replace(' ', '')
            name = name[0].lower() + name[1:] + 'Response'

            path = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), 'resources', 'fixtures', name +
                    '.json'))
            try:
                with io.open(path) as f:
                    self.expected_response = json.load(f)
                    self.client.set_expected_response(
                        status_code=status_code,
                        data_to_return=self.expected_response)
            except IOError:
                if 'delete' in func.__name__:
                    self.client.set_expected_response(
                        data_to_return=None, status_code=status_code)

            func(self, *args, **kwargs)

        return decorator

    return wrapper
