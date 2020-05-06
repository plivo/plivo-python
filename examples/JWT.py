from plivo.utils import jwt
import time

# using valid_from in epoch and lifetime in seconds
token = jwt.AccessToken('MADADADADADADADADADA', 'qwerty', 'username', valid_from=time.time(), lifetime=300, uid='username-12345')
token.add_voice_grants(True, True)
print(token.to_jwt())


# using valid_from and valid_till in epoch
token = jwt.AccessToken('MADADADADADADADADADA', 'qwerty', 'username', valid_from=time.time(), valid_till=1588751222)
token.add_voice_grants(True, True)
print(token.to_jwt())
print(time.time())
