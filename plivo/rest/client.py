# -*- coding: utf-8 -*-
"""
Core client, used for all API requests.
"""
from plivo.resources import (Accounts, Addresses, Applications, Calls,
                             Conferences, Endpoints, Identities, Messages,
                             Numbers, Pricings, Recordings, Subaccounts)
from plivo.resources.live_calls import LiveCalls
from plivo.rest.base_client import BaseClient


class Client(BaseClient):
    def __init__(self, auth_id=None, auth_token=None, proxies=None, timeout=5):
        """
        The Plivo API client.

        Deals with all the API requests to be made.
        """
        BaseClient.__init__(self, auth_id, auth_token, proxies, timeout)

        self.account = Accounts(self)
        self.subaccounts = Subaccounts(self)
        self.applications = Applications(self)
        self.calls = Calls(self)
        self.live_calls = LiveCalls(self)
        self.conferences = Conferences(self)
        self.endpoints = Endpoints(self)
        self.messages = Messages(self)
        self.numbers = Numbers(self)
        self.pricing = Pricings(self)
        self.recordings = Recordings(self)
        self.addresses = Addresses(self)
        self.identities = Identities(self)
