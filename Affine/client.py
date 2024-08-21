import socket

def affine_encrypt(plaintext, a, b, m):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            char = chr(((a * (ord(char) - offset) + b) % m) + offset)
        ciphertext += char
    return ciphertext

def send_request(text, a, b):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    
    
    m = 26  # size of the alphabet
    encrypted_text = affine_encrypt(text, a, b, m)
    
    request = f"ENCRYPTED|{encrypted_text}|{a}|{b}"
    client.send(request.encode('utf-8'))

    response = client.recv(4096).decode('utf-8')
    print(f"Server response (Decrypted): {response}")
    
    client.close()

def main():
    text = input("Enter text to encrypt: ")
    a = int(input("Enter key a: "))
    b = int(input("Enter key b: "))
    
    send_request(text, a, b)

if __name__ == '__main__':
    main()

