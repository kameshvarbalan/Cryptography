IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def permute(input_bits, table):
    return ''.join(input_bits[pos-1] for pos in table)

if __name__=='__main__':
    input_data = input('\nEnter input data (hexadecimal): ')
    if len(input_data)!=16 or not all(nibble in '0123456789ABCDEF' for nibble in input_data):
        raise ValueError('Input must be a 64-bit hexadecimal string')
    input_data = bin(int(input_data, 16))[2:].zfill(64)
    print(f'Input data in binary: {input_data}')
    ip_data = permute(input_data, IP_TABLE)
    print('\nOutput from Initial Permutation Table:')
    print(f'Binary: {ip_data}\nHexaDecimal: {hex(int(ip_data, 2))[2:].zfill(16).upper()}')
    fp_data = permute(ip_data, FP_TABLE)
    print('\nOutput from Final Permutation Table:')
    print(f'Binary: {fp_data}\nHexaDecimal: {hex(int(fp_data, 2))[2:].zfill(16).upper()}')