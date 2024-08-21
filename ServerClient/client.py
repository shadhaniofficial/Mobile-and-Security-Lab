import socket

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

def start_client():
    host = '127.0.0.1'
    port = 65432
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    plaintext = input("Enter a string: ")
    shift = int(input("Enter the shift value: "))

    encrypted = encrypt_caesar_cipher(plaintext, shift)
    print(f"Encrypted: {encrypted}")

    message = f"{encrypted}|{shift}"
    client_socket.sendall(message.encode())
    
    decrypted = client_socket.recv(1024).decode()
    print(f"Decrypted from server: {decrypted}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

