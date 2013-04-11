import unittest
import plivo
import random
import string

try:
    import auth_secrets
except ImportError:
    raise Exception("Create a auth_secrets.py file")


class TestAccounts(unittest.TestCase):
    def setUp(self):
        auth_id = auth_secrets.AUTH_ID
        auth_token = auth_secrets.AUTH_TOKEN

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
        random_letter = lambda: random.choice(string.ascii_letters)
        random_name = ''.join(random_letter() for i in range(8))
        response = self.client.create_subaccount(dict(name=random_name,
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
        auth_id = auth_secrets.AUTH_ID
        auth_token = auth_secrets.AUTH_TOKEN
        self.client = plivo.RestAPI(auth_id, auth_token)

    def test_get_applications(self):
        response = self.client.get_applications()
        self.assertEqual(200, response[0])
        valid_keys = ["objects", "api_id", "meta"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)

if __name__ == "__main__":
    unittest.main()
