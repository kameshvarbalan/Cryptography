def generate_key_square(key):
    key = key.upper().replace('J', 'I')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key_square = ""
    for char in key:
        if char not in key_square and char in alphabet:
            key_square += char
    for char in alphabet:
        if char not in key_square:
            key_square += char
    return [list(key_square[i:i + 5]) for i in range(0, 25, 5)]

def find_position(char, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    key_square = generate_key_square(key)
    print('\nKey Square:')
    for row in key_square:
        print(row)
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    pairs = []
    i = 0
    while i<len(plaintext):
        if i+1<len(plaintext) and plaintext[i]==plaintext[i+1]:
            pairs.append(plaintext[i]+'X')
            i += 1
        elif i+1<len(plaintext):
            pairs.append(plaintext[i]+plaintext[i+1])
            i += 2
        else:
            pairs.append(plaintext[i]+'X')
            i += 1
    ciphertext = ""
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_square)
        row2, col2 = find_position(pair[1], key_square)
        if row1==row2:
            ciphertext += key_square[row1][(col1+1)%5]
            ciphertext += key_square[row2][(col2+1)%5]
        elif col1==col2:
            ciphertext += key_square[(row1+1)%5][col1]
            ciphertext += key_square[(row2+1)%5][col2]
        else: 
            ciphertext += key_square[row1][col2]
            ciphertext += key_square[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    ciphertext = ciphertext.upper().replace(' ', '')
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ''
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_square)
        row2, col2 = find_position(pair[1], key_square)
        if row1==row2:
            plaintext += key_square[row1][(col1-1)%5]
            plaintext += key_square[row2][(col2-1)%5]
        elif col1==col2:
            plaintext += key_square[(row1-1)%5][col1]
            plaintext += key_square[(row2-1)%5][col2]
        else:
            plaintext += key_square[row1][col2]
            plaintext += key_square[row2][col1]
    return plaintext.rstrip('X')

if __name__=='__main__':
    key = input('\nEnter key to generate Playfair Cypher: ')
    plain_text = input('Enter text to encrypt: ')
    cipher_text = playfair_encrypt(plain_text, key)
    print("\nCiphertext:", cipher_text)
    ciphertext = input('\nEnter cypher text to decrypt: ')
    decrypted_text = playfair_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)