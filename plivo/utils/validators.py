# -*- coding: utf-8 -*-
import functools
import importlib
import inspect
import re

import decorator
import six

from plivo.exceptions import ValidationError


def regex(regex):
    rexp = re.compile(regex)

    def f(name, value):
        if not rexp.match(value):
            return None, [
                '{} should match format {} (actual value: {})'.format(
                    name, regex, value)
            ]

        return value, []

    return f


def all_of(*validators):
    def f(name, value):
        for validator in validators:
            value, errs = validator(name, value)
            if errs:
                return None, errs
        return value, []

    return f


def one_of(*validators):
    def f(name, value):
        for validator in validators:
            new_val, errs = validator(name, value)
            if errs:
                continue
            else:
                return new_val, []
        return None, '{} did not satisfy any of the required types'.format(
            name)

    return f


def check(checker, message=None):
    def f(name, value):
        inr = checker(value)
        msg = message or '{} should be in range'.format(name)
        if inr:
            return value, []
        else:
            return None, ['{} (actual value: {})'.format(msg, value)]

    return f


def is_in(iterable, message=None, case_sensitive=True, case_type='upper'):
    def f(name, value):
        actual_value = value
        if not case_sensitive:
            if case_type == 'upper':
                value = str(value).upper()
            elif case_type == 'lower':
                value = str(value).lower()
            elif case_type == 'title':
                value = str(value).title()

        msg = message or '{} should be in {}'.format(name, iterable)
        if value in iterable:
            return value, []
        else:
            return None, ['{} (actual value: {})'.format(msg, actual_value)]
    return f


def multi_is_in(iterable, message=None, case_sensitive=True, make_lower_case=False, separator=','):
    def f(name, value):
        actual_value = value
        if not case_sensitive:
            if make_lower_case:
                value = str(value).lower()
            else:
                value = str(value).upper()
        msg = message or '{} should be among {}. multiple values should be COMMA(,) separated'.format(name, iterable)
        for val in value.split(separator):
            if val not in iterable:
                return None, ['{} (actual value: {})'.format(msg, actual_value)]
        return value, []

    return f


def optional(*validators):
    def f(name, value):
        if value is None:
            return None, []
        return all_of(*validators)(name, value)

    return f


def required(validate):
    def f(name, value):
        if not value:
            return None, '{} is required (current value: None)'.format(name)
        return validate(name, value)

    return f


def of_type(*args):
    def f(name, value):
        if value is None:
            return None, ['{name} cannot be None'.format(name=name)]
        for typ in args:
            if isinstance(typ, str):
                parts = typ.split('.')
                typ = getattr(
                    importlib.import_module('.'.join(parts[:-1])), parts[-1])
            try:
                value = typ(value)
                return value, []
            except ValueError:
                pass
        return None, [
            '{name} should be of type: {types}'.format(
                name=name, types=[arg.__name__ for arg in args])
        ]

    return f


def of_type_exact(*args):
    def f(name, value):
        for typ in args:
            if isinstance(typ, str):
                parts = typ.split('.')
                typ = getattr(
                    importlib.import_module('.'.join(parts[:-1])), parts[-1])
            if not isinstance(value, typ):
                continue
            return value, []
        return None, [
            '{name} should be of type: {types}'.format(
                name=name,
                types=[getattr(arg, '__name__', str(arg)) for arg in args])
        ]

    return f


def is_iterable(validator, sep=None):
    def f(name, value):
        try:
            l = []
            v, e = validator(name, value)
            if v and not e:
                raise TypeError()  # hack
            for i, item in enumerate(iter(value)):
                val, errs = validator('{}[{}]'.format(name, i), item)
                if errs:
                    return None, errs
                l.append(val)
            ret = (l, []) if not sep else (sep.join(l), [])
            return ret
        except TypeError:
            val, errs = validator(name, value)
            if errs:
                return None, errs
            return ([val], []) if not sep else (val, [])

    return required(f)


def multiple_valid_integers(lowerbound, upperbound):
    def f(name, value):
        if isinstance(value, int):
            if value >= lowerbound and value <= upperbound:
                return value, []
            else:
                return None, {name + ' value must be in range ' + str(lowerbound) + ' to ' + str(upperbound)}
        else:
            values = value.split('<')
            for i in values:
                is_int = True
                try:
                    int(i)
                except ValueError:
                    is_int = False
                if is_int:
                    if int(i) > upperbound or int(i) < lowerbound:
                        return None, [name + ' destination value must be in range ' + str(lowerbound) + ' to ' + str(upperbound)]
                else:
                    return None, ['{} destination value must be integer'.format(name)]
            return value, []
    return f


def validate_args(**to_validate):
    def outer(wrapped):
        @functools.wraps(wrapped)
        def wrapper(self, *args, **kwargs):
            params = inspect.getcallargs(wrapped, *args, **kwargs)
            for arg_name, validators in to_validate.items():
                for validator in validators:
                    params[arg_name], errs = validator(arg_name,
                                                       params.get(
                                                           arg_name, None))
                    if errs:
                        raise ValidationError(errs)
            return wrapped(**params)

        return decorator.decorate(wrapped, wrapper)

    return outer


is_valid_date = functools.partial(of_type, six.text_type)
is_phonenumber = functools.partial(of_type, six.text_type)
is_subaccount_id = functools.partial(all_of, of_type(six.text_type),
                                     regex(r'^SA[A-Z0-9]{18}$'))
is_mainaccount_id = functools.partial(all_of, of_type(six.text_type),
                                      regex(r'^MA[A-Z0-9]{18}$'))
is_account_id = functools.partial(all_of, of_type(six.text_type),
                                      regex(r'^(M|S)A[A-Z0-9]{18}$'))
is_subaccount = functools.partial(
    one_of, of_type_exact('plivo.resources.accounts.Subaccount'),
    is_subaccount_id())
is_url = functools.partial(
    all_of, of_type(six.text_type),
    regex(
        r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|None)'
    ))
is_proper_date_format = functools.partial(all_of, of_type_exact(str),
                                          regex(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}(:\d{2}(\.\d{1,6})?)?$'))
