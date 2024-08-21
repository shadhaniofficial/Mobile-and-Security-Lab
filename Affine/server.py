import socket

def affine_decrypt(ciphertext, a, b, m):
    def mod_inverse(a, m):
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError("No modular inverse exists")

    a_inv = mod_inverse(a, m)
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            char = chr(((a_inv * ((ord(char) - offset) - b)) % m) + offset)
        plaintext += char
    return plaintext

def handle_client(client_socket):
    try:
        request = client_socket.recv(1024).decode('utf-8')
        if request:
            parts = request.split('|')
            command = parts[0]
            encrypted_text = parts[1]
            a = int(parts[2])
            b = int(parts[3])
            m = 26  

            if command == 'ENCRYPTED':
                decrypted_text = affine_decrypt(encrypted_text, a, b, m)
                print(f"Received encrypted text: {encrypted_text}")
                print(f"Decrypted text: {decrypted_text}")
                response = decrypted_text
            else:
                response = 'INVALID COMMAND'

            client_socket.send(response.encode('utf-8'))
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print('Server listening...')

    while True:
        client_socket, addr = server.accept()
        print(f'Accepted connection from {addr}')
        handle_client(client_socket)

if __name__ == '__main__':
    main()

