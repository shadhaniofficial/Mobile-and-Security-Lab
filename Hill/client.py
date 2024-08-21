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
    
    def encrypt(self, message):
        messageVector = np.array([[ord(c) % 65] for c in message])
        cipherMatrix = np.dot(self.keyMatrix, messageVector) % 26
        return ''.join(chr(int(c) + 65) for c in cipherMatrix.flatten())

def main():
    key = "GYBNQKURP"  
    hill_cipher = HillCipher(key)
    
    message = "ACT"  
    encrypted_message = hill_cipher.encrypt(message)
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 65432))
    client.sendall(encrypted_message.encode('utf-8'))
    client.close()

if __name__ == "__main__":
    main()

