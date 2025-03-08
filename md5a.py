def to_binary(data):
    return ''.join(format(ord(char), '08b') for char in data)
def pad(message):
    bin_text = to_binary(message)
    org_bits = len(bin_text)
    print(f'\nLength of original message (bits): {org_bits}')
    print(f'\nOriginal message in binary:\n{bin_text}')
    padding_bits = (448-org_bits%512)%512
    print(f'\nPadding bits = {padding_bits}')
    padding = '1' + '0'*(padding_bits-1)
    print(f'\nPadding bits in binary:\n{padding}')
    length_bits = format(org_bits, '064b')
    print(f'\nLength of original message in binary: {length_bits}')
    padded_message = bin_text + padding + length_bits
    print(f'\nPadded message in binary:\n{padded_message}')
    blocks = [padded_message[i:i+512] for i in range(0, len(padded_message), 512)]
    for i, item in enumerate(blocks):
        print(f'\nBlock {i+1}:')
        print(item)

if __name__ == '__main__':
    pt = input('Enter message: ')
    pad(pt)