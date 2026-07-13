# write a program to find out message digest(hash value ) from MD-5 algorithm.
import hashlib  #provides hashing algorithms like MD-5, SHA-1
import sys    #use here to get the size of an object ib byte

str = input("enter the value:")  # ask the user to enter a string.
str = bytes(str, 'utf-8') #convert the strings to bytes required ex."abc->b'abc'

result = hashlib.md5(str); # computes the MD5 hash of the byte string.
            
print("the byte eqvivalent of hash is: " , end="")
print(result.digest())  # result.digest() returns the raw bytes.
            
print("\r")
print("the size of the output:", end="")
print(sys.getsizeof(result.digest())) # print the size in bytes

#answer = 49

            

