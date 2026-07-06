def caesar_cipher_encrypt(text, shift):
   result = ""
   for char in text:
       if char.isupper(): 
           result += chr((ord(char) + shift - 65) % 26 + 65)
       else:
           result += char 
   return result
# Example usage
text = "HELLO"
shift = 3
encrypted_text = caesar_cipher_encrypt(text, shift)
print(encrypted_text) # Output: KHOOR
