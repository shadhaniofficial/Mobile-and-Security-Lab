import socket
import numpy as np

class HillCipher:
    def __init__(self, key):
        self.keyMatrix = np.zeros((3, 3), dtype=int)
        self.getKeyMatrix(key)
    
    def getKeyMatrix(self, key):
        k = 0
        for i in range(3):
            for j in range(3):
                self.keyMatrix[i][j] = ord(key[k]) % 65
                k += 1
    
    def decrypt(self, cipherText):
        cipherMatrix = np.array([[ord(c) % 65] for c in cipherText])
        invKeyMatrix = np.linalg.inv(self.keyMatrix)  # Compute the inverse of the key matrix
        invKeyMatrix = np.round(invKeyMatrix).astype(int) % 26
        messageMatrix = np.dot(invKeyMatrix, cipherMatrix) % 26
        return ''.join(chr(int(m) + 65) for m in messageMatrix.flatten())

def handle_client(client_socket, hill_cipher):
    while True:
        encrypted_message = client_socket.recv(1024).decode('utf-8')
        if not encrypted_message:
            break
        decrypted_message = hill_cipher.decrypt(encrypted_message)
        print(f"Decrypted Message: {decrypted_message}")
    client_socket.close()

def main():
    key = "GYBNQKURP" 
    hill_cipher = HillCipher(key)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 65432))
    server.listen(5)
    print("Server listening on port 65432...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr} has been established!")
        handle_client(client_socket, hill_cipher)

if __name__ == "__main__":
    main()

