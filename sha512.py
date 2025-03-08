def sha_512(message_size):
    padding = (896-message_size%1024)%1024
    total_length = message_size+padding+128
    blocks = total_length//1024
    return padding, blocks

if __name__ == '__main__':
    message_size = int(input('Enter message size in bits: '))
    padding, blocks = sha_512(message_size)
    print(f'\nPadding Bits: {padding}\nNo. of Blocks: {blocks}')