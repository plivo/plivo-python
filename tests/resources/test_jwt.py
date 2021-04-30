# # -*- coding: utf-8 -*-

# import plivo
# import time
# from tests.base import PlivoResourceTestCase
# from plivo.utils import jwt
# import sys


# class AccessTokenTest(PlivoResourceTestCase):
#     def test_jwt_constructor(self):
#         if int(sys.version[0]) == 3:
#             self.assertRaisesRegex(TypeError, "", jwt.AccessToken.__init__,
#                                jwt.AccessToken, 'ADADADADADADADADADA',
#                                'qwerty')
#         else:
#             self.assertRaisesRegexp(TypeError, "", jwt.AccessToken.__init__,
#                                    jwt.AccessToken, 'ADADADADADADADADADA',
#                                    'qwerty')

#     def test_jwt_constructor_auth_id(self):
#         if int(sys.version[0]) == 3:
#             self.assertRaisesRegex(plivo.exceptions.ValidationError,
#                                "auth_id should match format .*",
#                                jwt.AccessToken.__init__, jwt.AccessToken,
#                                'ADADADADADADADADADA', 'qwerty', 'username')
#         else:
#             self.assertRaisesRegexp(plivo.exceptions.ValidationError,
#                                    "auth_id should match format .*",
#                                    jwt.AccessToken.__init__, jwt.AccessToken, 'ADADADADADADADADADA', 'qwerty', 'username')

#     def test_jwt_constructor_auth_id(self):
#         if int(sys.version[0]) == 3:
#             self.assertRaisesRegex(plivo.exceptions.ValidationError,
#                                "auth_id should match format .*",
#                                jwt.AccessToken.__init__, jwt.AccessToken,
#                                'ADADADADADADADADADA', 'qwerty', 'username')
#         else:
#             self.assertRaisesRegexp(plivo.exceptions.ValidationError,
#                                    "auth_id should match format .*",
#                                    jwt.AccessToken.__init__, jwt.AccessToken,
#                                    'ADADADADADADADADADA', 'qwerty', 'username')

#     def test_jwt_constructor_lifetime(self):
#         if int(sys.version[0]) == 3:
#             self.assertRaisesRegex(plivo.exceptions.ValidationError,
#                                ".* lifetime .*",
#                                jwt.AccessToken.__init__,
#                                jwt.AccessToken,
#                                'MADADADADADADADADADA',
#                                'qwerty',
#                                'username',
#                                valid_from=int(time.time()),
#                                lifetime=123)
#         else:
#             self.assertRaisesRegexp(plivo.exceptions.ValidationError,
#                                    ".* lifetime .*",
#                                    jwt.AccessToken.__init__,
#                                    jwt.AccessToken,
#                                    'MADADADADADADADADADA',
#                                    'qwerty',
#                                    'username',
#                                    valid_from=int(time.time()),
#                                    lifetime=123)

#     def test_jwt_constructor_validity(self):
#         self.assertRaisesRegex(plivo.exceptions.ValidationError,
#                                "use either lifetime or valid_till",
#                                jwt.AccessToken.__init__,
#                                jwt.AccessToken,
#                                'MADADADADADADADADADA',
#                                'qwerty',
#                                'username',
#                                valid_from=int(time.time()),
#                                valid_till=int(time.time()) - 100,
#                                lifetime=1200)
#         self.assertRaisesRegex(plivo.exceptions.ValidationError,
#                                "validity expires .* seconds before it starts",
#                                jwt.AccessToken.__init__,
#                                jwt.AccessToken,
#                                'MADADADADADADADADADA',
#                                'qwerty',
#                                'username',
#                                valid_from=int(time.time()),
#                                valid_till=int(time.time()) - 100)

#     def test_jwt(self):
#         token = jwt.AccessToken('MADADADADADADADADADA', 'qwerty', 'username', valid_from=12121212, lifetime=300, uid='username-12345')
#         token.add_voice_grants(True, True)
#         self.assertEqual(True, token.grants['voice']['incoming_allow'])
#         self.assertNotEqual(False, token.grants['voice']['outgoing_allow'])
#         self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImN0eSI6InBsaXZvO3Y9MSJ9.eyJqdGkiOiJ1c2VybmFtZS0xMjM0NSIsImlzcyI6Ik1BREFEQURBREFEQURBREFEQURBIiwic3ViIjoidXNlcm5hbWUiLCJuYmYiOjEyMTIxMjEyLCJleHAiOjEyMTIxNTEyLCJncmFudHMiOnsidm9pY2UiOnsiaW5jb21pbmdfYWxsb3ciOnRydWUsIm91dGdvaW5nX2FsbG93Ijp0cnVlfX19.khM99-sYP2AylLo9y6bwNnJbVPjjtOMAimiFvNo7FGA', token.to_jwt())
