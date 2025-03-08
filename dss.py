def mod_inverse(a, m):
    a = a%m
    for x in range(1, m):
        if (a*x)%m==1:
            return x
    return None

def sender(p, q, m, x, k, h):
    g = pow(h, (p-1)//q, p)
    y = pow(g, x, p)
    r = pow(g, k, p)%q
    kinv = mod_inverse(k, q)
    s = (kinv*(m+r*x))%q
    print('\nSenders side')
    print(f'g = {g}\nPublic Key = {y}')
    print(f'Digital Signature (r,s) = ({r},{s})')
    return g, y, (r, s)

def receiver(p, q, m, g, y, r, s):
    w = mod_inverse(s, q)
    u1 = (m*w)%q
    u2 =(r*w)%q
    print('\nReceivers side')
    print(f'w = {w}\nu1 = {u1}\nu2 = {u2}')
    v = ((pow(g, u1)*pow(y, u2))%p)%q
    print(f'v = {v}')
    return v==r

if __name__ == '__main__':
    p, q = map(int, input('\nEnter prime numbers p & q: ').split())
    m = int(input('Enter message: '))
    x = int(input('Enter private key: '))
    k = int(input('Enter random integer k: '))
    h = int(input('Enter value of h: '))
    g, y, sign = sender(p, q, m, x, k, h)
    if receiver(p, q, m, g, y, sign[0], sign[1]):
        print('Verification Successful')
    else:
        print('Verification Failed')