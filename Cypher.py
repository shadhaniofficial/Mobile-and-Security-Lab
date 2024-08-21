def encrypt_caesar_cipher(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        elif char.isdigit():
            
            shift_amount = shift % 10
            start = ord('0')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 10)
            encrypted_text += encrypted_char
        else:
            
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(ciphertext, shift):
    return encrypt_caesar_cipher(ciphertext, -shift)


plaintext = input("Enter a String: ")
shift = int(input("Enter the shift value: "))

encrypted = encrypt_caesar_cipher(plaintext, shift)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_caesar_cipher(encrypted, shift)
print(f"Decrypted: {decrypted}")

