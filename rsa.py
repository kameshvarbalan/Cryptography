def extended_euclid(p, q):
    if q==0:
        return p, 1, 0
    g, x1, y1 = extended_euclid(q, p%q)
    x = y1
    y = x1 - (p//q)*y1
    return g, x, y

def mul_inverse(e, phi):
    g, x, _ = extended_euclid(e, phi)
    if g!=1:
        return -1
    else:
        return x%phi

def euler_totient(p, q):
    return (p-1)*(q-1)

def generate_key(p, q):
    # Assuming that user gives a valid e less than and relatively prime to phi(n)
    e = int(input('Enter public key (e should be valid): '))
    n = p*q
    phi = euler_totient(p, q)
    d = mul_inverse(e, phi)
    if d==-1:
        print('Invalid e value - Multiplicative inverse of e does not exist')
        exit()
    return (e,n), (d,n)

def encrypt(public_key, plain_text):
    e, n = public_key
    cipher_text = pow(plain_text, e, n)
    return cipher_text

def decrypt(private_key, cipher_text):
    d, n = private_key
    decrypted_text = pow(cipher_text, d, n)
    return decrypted_text

if __name__ == '__main__':
    p, q = map(int, input('\nEnter two prime numbers (p&q): ').split())
    public_key, private_key = generate_key(p, q)
    P = int(input('\nEnter plain text: '))
    C = encrypt(public_key, P)
    print(f'Cipher Text: {C}')
    cipher_text = int(input('\nEnter encrypted text: '))
    M = decrypt(private_key, cipher_text)
    print(f'Decrypted Text: {M}')