# -*- coding: utf-8 -*-
from unittest import TestCase


class ClientTest(TestCase):
    def test_subaccount(self):
        from plivo.utils import is_valid_subaccount
        self.assertTrue(is_valid_subaccount('SA' + 'X' * 18))
