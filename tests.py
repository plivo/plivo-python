import unittest
import os
import random
import string

import plivo

random_letter = lambda: random.choice(string.ascii_letters)
random_name = lambda: ''.join(random_letter() for i in range(8))

try:
    from auth_secrets import AUTH_ID, AUTH_TOKEN
except ImportError:
    AUTH_ID, AUTH_TOKEN = os.getenv("AUTH_ID"), os.getenv("AUTH_TOKEN")
    if not (AUTH_ID and AUTH_TOKEN):
        raise Exception("Create a auth_secrets.py file or set AUTH_ID "
                        "and AUTH_TOKEN as environ values.")


class TestAccounts(unittest.TestCase):
    def setUp(self):
        auth_id = AUTH_ID
        auth_token = AUTH_TOKEN

        self.client = plivo.RestAPI(auth_id, auth_token)

    def test_get_account(self):
        response = self.client.get_account()
        self.assertEqual(200, response[0])
        valid_keys = ["account_type", "address", "auth_id", "auto_recharge",
                      "cash_credits", "city", "created", "enabled"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)

    def test_get_subaccounts(self):
        response = self.client.get_subaccounts()
        self.assertEqual(200, response[0])
        valid_keys = ["meta", "api_id", "objects"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)

    def test_subaccount_crud(self):

        response = self.client.create_subaccount(dict(name=random_name(),
                                                 enabled=True))
        self.assertEqual(201, response[0])
        valid_keys = ["auth_id", "api_id", "auth_token"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)
        auth_id = json_response["auth_id"]
        response = self.client.get_subaccount(dict(subauth_id=auth_id))
        self.assertEqual(200, response[0])
        response = self.client.delete_subaccount(dict(subauth_id=auth_id))
        self.assertEqual(204, response[0])


class TestApplication(unittest.TestCase):
    def setUp(self):
        auth_id = AUTH_ID
        auth_token = AUTH_TOKEN
        self.client = plivo.RestAPI(auth_id, auth_token)

    def test_get_applications(self):
        response = self.client.get_applications()
        self.assertEqual(200, response[0])
        valid_keys = ["objects", "api_id", "meta"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)

    def test_application_crud(self):
        name = random_name()
        params = dict(answer_url="http://plivo.com/",
                      app_name=name)
        response = self.client.create_application(params)
        self.assertEqual(201, response[0])
        app_id = response[1]['app_id']
        response = self.client.get_application({"app_id": app_id})
        self.assertEqual(200, response[0])
        self.assertEqual(name, response[1]["app_name"])
        response = self.client.delete_application(dict(app_id=app_id))
        self.assertEqual(204, response[0])


if __name__ == "__main__":
    unittest.main()
