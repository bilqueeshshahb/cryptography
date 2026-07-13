# write a program to find out a messge digest(hash value) from SHA-1 algorithm.

import hashlib

#take user input
text = input ("enter a string to generate a hash:")

#SHA-1 Hash
sha1_result = hashlib.sha1(text.encode())

print("\n--- SHA-1 HASH ---")
print("SHA-1 (hex):",sha1_result.hexdigest())
print("SHA-1 Output size (in bits):",len(sha1_result.digest()) * 8)

#answer = 160

