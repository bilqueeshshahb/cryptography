# dephihellman key exchange implementation

# 1.input parameters    
p = int(input("enter the value of p:"))
g = int(input("enter the value of generator:"))

# 2.private parameters
alice_private = int(input("enter the value of alice private key:"))
bob_private = int(input("enter the value of bob private key:"))
print(f"alice's secret private key:{alice_private}")
print(f"bob's secret private key:{bob_private}\n")

# 3.public key calculation(g^secret mod p)
alice_public = pow (g, alice_private, p)
bob_public = pow(g, bob_private, p)
print(f"alice's public key sent to bob: {alice_public}")
print(f"bob's public key sent to alice: {bob_public}\n")

# 4.shared secret key derivation (received_public^my_private mod p)
alice_shared_secret = pow(bob_public, alice_private, p)
bob_shared_secret = pow(alice_public, bob_private, p)
print(f"alice calculated shared secret: {alice_shared_secret}")
print(f"bob calculated shared secret: {bob_shared_secret}")

#5.verification
if(alice_shared_secret == bob_shared_secret):
    print("\nsuccess! both parties have established the same shared secret key")
          
                    


