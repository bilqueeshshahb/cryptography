# write a program of MD-5(short code)

import hashlib

message = input ("enter text:")

h = hashlib.md5(message.encode()).hexdigest()

print("hash value:" ,h)
