# write a program to find out a messge digest(hash value) from SHA-512 algorithm.

import hashlib

#take user input
text = input ("enter a string to generate a hash:")

#SHA-512 Hash
sha512_result = hashlib.sha512(text.encode())

print("\n--- SHA-512 HASH ---")
print("SHA-512 (hex):",sha512_result.hexdigest())
print("SHA-512 Output size (in bits):",len(sha512_result.digest()) * 8)

#answer = 512
