def caesar_cipher_decrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += char
    
    return result

# Example usage
encrypted_text = "KHOOR"
shift = 3

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print(decrypted_text)   # Output: HELLO
