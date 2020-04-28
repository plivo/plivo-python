import plivo.utils.AccessToken as jwt
import time

# using valid_from in epoch and lifetime in seconds
token = jwt.AccessToken('MADADADADADADADADADA', 'qwerty', 'username', valid_from=time.time(), lifetime=300, uid='username-12345')
token.add_voice_grants(True, True)
print(token.to_jwt())
