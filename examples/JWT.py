from plivo.utils import jwt
import time

# using valid_from in epoch and lifetime in seconds
token = jwt.AccessToken('{authId}', '{authToken}', '{endpointUsername}', valid_from=time.time(), lifetime=300, uid='{uid}')
# grants(incoming:bool, outgoing:bool)
token.add_voice_grants(True, True)
print(token.to_jwt())


# using valid_from and valid_till in epoch
token = jwt.AccessToken('{authId}', '{authToken}', '{endpointUsername}', valid_from=time.time(), valid_till=1588751222)
token.add_voice_grants(False, True)
print(token.to_jwt())
