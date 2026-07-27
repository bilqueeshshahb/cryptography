# write a program of sha1(short code)

import hashlib

message = input("enter text: ")

h = hashlib.sha1(message.encode()).hexdigest()

print("hash value:" , h)
