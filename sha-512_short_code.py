# write a program of sha-512 (short code)

import hashlib

message = input ("enter text:")

h = hashlib.sha512(message.encode()).hexdigest()

print("hash value:" , h)
