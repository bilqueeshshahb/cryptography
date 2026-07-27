# write a program of sha-256 (short code)

import hashlib

message = input("enter text:")

h = hashlib.sha256(message.encode()).hexdigest()

print("hash value:" , h)

