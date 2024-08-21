import socket

def decrypt_caesar_cipher(ciphertext, shift):
    return encrypt_caesar_cipher(ciphertext, -shift)

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

def start_server():
    host = '127.0.0.1'
    port = 65432
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        
        encrypted_text, shift = data.split('|')
        shift = int(shift)
        decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
        print(f"decrypted text: {decrypted_text}")
       #conn.sendall(decrypted_text.encode())
	
    conn.close()

if __name__ == "__main__":
    start_server()

