import rsa

#generate keys
public_key, private_key = rsa.newkeys(2048)

message = input ("enter the message:")

#encrypt
ciphertext = rsa.encrypt(message.encode(), public_key)
print("encrypted:", ciphertext)

#decrypt
plaintext = rsa.decrypt(ciphertext, private_key)
print("decrypted:", plaintext.decode())

