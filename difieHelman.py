def diffie_hellman(alpha, q, X):
    return pow(alpha, X, q)

if __name__ == '__main__':
    q = int(input('\nEnter large prime number: '))
    alpha = int(input('Enter primitive root: '))
    alpha = alpha%q
    Xa = int(input('Enter private key of A: '))
    Xb = int(input('Enter private key of B: '))
    Ya = diffie_hellman(alpha, q, Xa)
    Yb = diffie_hellman(alpha, q, Xb)
    print(f'\nPublic key of A: {Ya}\nPublic key of B: {Yb}\n')
    mitm = int(input('Enter 1 to perform mitm else 0: '))
    if mitm:
        Xd1, Xd2 = map(int, input('\nEnter attackers private keys with A and B: ').split())
        Yd1, Yd2 = diffie_hellman(alpha, q, Xd1), diffie_hellman(alpha, q, Xd2)
        print(f'\nAttackers public key with A: {Yd1}\nAttackers public key with B: {Yd2}')
        K1, K2 = diffie_hellman(Yd1, q, Xa), diffie_hellman(Yd2, q, Xb)
        print(f'\nAttackers shared secret key with A: {K1}\nAttackers shared secret key with B: {K2}')
        Kd1, Kd2 = diffie_hellman(Ya, q, Xd1), diffie_hellman(Yb, q, Xd2)
        print(f'Secret Session key of A: {Kd1}\nSecret session key of B: {Kd2}')
        print('Diffie-Hellman key exhchange is compromised by Man-in-the-Middle Attack')
    else:
        Ka = diffie_hellman(Yb, q, Xa)
        Kb = diffie_hellman(Ya, q, Xb)
        print(f'\nShared session key of A: {Ka}\nShared session key of B: {Kb}')
        print('Diffie-Hellman key exchange is secure')