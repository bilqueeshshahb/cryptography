#write a program to encrypt and decrypt message using rail fence cipher.

from pycipher import Railfence

plaintext = input("enter plaintext:")
rail = int(input("enter number of rail:"))

cipher = Railfence(rail)
ciphertext = cipher.encipher(plaintext)

print("Encrypted:" , ciphertext)

plaintext = cipher.decipher(ciphertext)

print("Decrypted:" ,plaintext)

