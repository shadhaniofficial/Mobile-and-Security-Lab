def encode(st):
    encoded_str = ""
    for char in st:
        if char == 'z':
            encoded_str += 'a'
        elif char == 'Z':
            encoded_str += 'A'
        elif 'a' <= char <= 'y':
            encoded_str += chr(ord(char) + 1)
        elif 'A' <= char <= 'Y':
            encoded_str += chr(ord(char) + 1)
        elif char.isdigit():
            encoded_str += chr((ord(char) - ord('0') + 1) % 10 + ord('0'))
        else:
            encoded_str += char
    return encoded_str

def decode(st):
    decoded_str = ""
    for char in st:
        if char == 'a':
            decoded_str += 'z'
        elif char == 'A':
            decoded_str += 'Z'
        elif 'b' <= char <= 'z':
            decoded_str += chr(ord(char) - 1)
        elif 'B' <= char <= 'Z':
            decoded_str += chr(ord(char) - 1)
        elif char.isdigit():
            decoded_str += chr((ord(char) - ord('0') - 1) % 10 + ord('0'))
        else:
            decoded_str += char
    return decoded_str

stri = input("Enter the message: ")
en = encode(stri)
de = decode(en)
print("Encoded: " + en)
print("Decoded: " + de)
