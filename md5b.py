def F(B, C, D):
    return (B&C)|(~B&D)

def left_shift(x, s):
    return ((x<<s)&0xFFFFFFFF)|(x>>(32-s))

def modular_add(x, y):
    return (x+y)&0xFFFFFFFF

def operation1(A, B, C, D, M0, K1):
    print('\nRound 1 - Operation 1')
    res = modular_add(A, F(B, C, D))
    res = modular_add(res, M0) 
    res = modular_add(res, K1)
    new_B = modular_add(B, left_shift(res, 7))
    return D, new_B, B, C

def operation2(A, B, C, D, M1, K2):
    print('\nRound 1 - Operation 2')
    res = modular_add(A, F(B, C, D))
    res = modular_add(res, M1) 
    res = modular_add(res, K2)
    new_B = modular_add(B, left_shift(res, 12))
    return D, new_B, B, C

def hex_input(prompt):
    return int(input(prompt), 16)

if __name__ == '__main__':
    A = hex_input('Enter A: ')
    B = hex_input('Enter B: ')
    C = hex_input('Enter C: ')
    D = hex_input('Enter D: ')
    M0 = hex_input('\nEnter M0: ')
    K1 = hex_input('Enter K1: ')
    A, B, C, D = operation1(A, B, C, D, M0, K1)
    print(f'New A: {hex(A)[2:].upper()}')
    print(f'New B: {hex(B)[2:].upper()}')
    print(f'New C: {hex(C)[2:].upper()}')
    print(f'New D: {hex(D)[2:].upper()}')
    M1 = hex_input('\nEnter M1: ')
    K2 = hex_input('Enter K2: ')
    A, B, C, D = operation2(A, B, C, D, M1, K2)
    print(f'New A: {hex(A)[2:].upper()}')
    print(f'New B: {hex(B)[2:].upper()}')
    print(f'New C: {hex(C)[2:].upper()}')
    print(f'New D: {hex(D)[2:].upper()}')