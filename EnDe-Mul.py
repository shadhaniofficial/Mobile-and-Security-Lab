def encode(st):
    encoded_str = ""
    for char in st:
        if 'A' <= char <= 'Z':
            temp = (ord(char) - ord('A') + 2) % 26 + ord('A')
            encoded_str += chr(temp)
        elif 'a' <= char <= 'z':
            temp = (ord(char) - ord('a') + 2) % 26 + ord('a')
            encoded_str += chr(temp)
        elif char.isdigit():
            temp = (ord(char) - ord('0') + 1) % 10 + ord('0')
            encoded_str += chr(temp)
        else:
            encoded_str += char
    
    return encoded_str

def decode(st):
    decoded_str = ""
    for char in st:
        if 'A' <= char <= 'Z':
            temp = (ord(char) - ord('A') - 2) % 26 + ord('A')
            decoded_str += chr(temp)
        elif 'a' <= char <= 'z':
            temp = (ord(char) - ord('a') - 2) % 26 + ord('a')
            decoded_str += chr(temp)
        elif char.isdigit():
            temp = (ord(char) - ord('0') - 1) % 10 + ord('0')
            decoded_str += chr(temp)
        else:
            decoded_str += char
    
    return decoded_str
        
stri = input("Enter the message: ")
en = encode(stri)
de = decode(en)
print("Encoded: " + en)
print("Decoded: " + de)
