def prepare_key_matrix(key, n):
    key = key.upper()
    key_values = [ord(char)-ord('A') for char in key]
    if len(key_values) != n*n:
        raise ValueError('Key length must be equal to n^2')
    key_matrix = []
    for i in range(n):
        key_matrix.append(key_values[i*n:(i+1)*n])
    return key_matrix

def determinant(matrix):
    if len(matrix)==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    det = 0
    for col in range(len(matrix)):
        minor = [[matrix[row][c] for c in range(len(matrix)) if c != col] for row in range(1, len(matrix))]
        cofactor = ((-1)**col) * matrix[0][col] * determinant(minor)
        det += cofactor
    return det

def mod_inverse(a, m):
    a = a%m
    for x in range(1, m):
        if (a*x)%m==1:
            return x
    return None

def inverse_matrix(matrix, modulus):
    n = len(matrix)
    if n==2:
        det = determinant(matrix) % modulus
        det_inv = mod_inverse(det, modulus)
        if det == 0 or det_inv is None:
            raise ValueError("Matrix is not invertible modulo {}".format(modulus))
        return [[(matrix[1][1] * det_inv) % modulus, (-matrix[0][1] * det_inv) % modulus],
            [(-matrix[1][0] * det_inv) % modulus, (matrix[0][0] * det_inv) % modulus]]
    det = determinant(matrix)%modulus
    det_inv = mod_inverse(det, modulus)
    if det==0 or det_inv is None:
        raise ValueError('Matrix is not invertible modulo {}'.format(modulus))
    cofactor_matrix = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            minor = [[matrix[r][c] for c in range(n) if c != col] for r in range(n) if r != row]
            cofactor_matrix[row][col] = ((-1)**(row+col)) * determinant(minor)
    inverse = [[(cofactor_matrix[col][row]*det_inv)%modulus for col in range(n)] for row in range(n)]
    return inverse

def multiply_matrices(matrix1, matrix2, modulus):
    result = [[0]*len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= modulus
    return result

def hill_encrypt(plaintext, key, n):
    key_matrix = prepare_key_matrix(key, n)
    print('\nKey Matrix:')
    for row in key_matrix:
        print(row)
    plaintext = plaintext.upper()
    plaintext_values = [ord(char)-ord('A') for char in plaintext]
    while len(plaintext_values)%n != 0:
        plaintext_values.append(ord('X')-ord('A'))
    plaintext_blocks = [plaintext_values[i:i+n] for i in range(0, len(plaintext_values), n)]
    ciphertext = ''
    for block in plaintext_blocks:
        block_matrix = [block]
        encrypted_matrix = multiply_matrices(block_matrix, key_matrix, 26)
        ciphertext += ''.join(chr(num+ord('A')) for num in encrypted_matrix[0])
    return ciphertext

def hill_decrypt(ciphertext, key, n):
    key_matrix = prepare_key_matrix(key, n)
    key_inverse = inverse_matrix(key_matrix, 26)
    print('\nKey Inverse Matrix:')
    for row in key_inverse:
        print(row)
    ciphertext_values = [ord(char)-ord('A') for char in ciphertext]
    ciphertext_blocks = [ciphertext_values[i:i+n] for i in range(0, len(ciphertext_values), n)]
    plaintext = ''
    for block in ciphertext_blocks:
        block_matrix = [block]
        decrypted_matrix = multiply_matrices(block_matrix, key_inverse, 26)
        plaintext += ''.join(chr(num+ord('A')) for num in decrypted_matrix[0])
    return plaintext.rstrip('X')

if __name__=='__main__':
    key = input('\nEnter key (length should be square number): ')
    n = int(len(key)**0.5)
    plain_text = input('Enter text to encrypt: ')
    cipher_text = hill_encrypt(plain_text, key, n)
    print("\nCiphertext:", cipher_text)
    ciphertext = input('\nEnter cypher text to decrypt: ')
    decrypted_text = hill_decrypt(ciphertext, key, n)
    print("\nDecrypted Text:", decrypted_text)