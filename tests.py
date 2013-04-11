import unittest
import plivo

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

    def test_get_subaccount(self):
        response = self.client.get_subaccounts()
        self.assertEqual(200, response[0])
        valid_keys = ["meta", "api_id", "objects"]
        json_response = response[1]
        for key in valid_keys:
            self.assertTrue(key in json_response)

if __name__ == "__main__":
    unittest.main()
