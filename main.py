# Eric Curtland
# Python 3.11
# CS 427
# Eric; 5 18 9 2; 13 67 29 5

primes_table = [13, 67, 29, 5]


class FeistelNetwork:
    def __init__(self, key, round_function, schedule):
        self.key = key
        self.round_function = round_function
        self.schedule = schedule
        self.total_rounds = 4
        self.counter = 0
        self.nonce = 0

    def encrypt(self, plaintext):
        cypher_text = []
        # breaks the plain text into 4 hex digit blocks
        plain_blocks = [plaintext[i:i+4] for i in range(0, len(plaintext), 4)]
        for block in plain_blocks:
            binary_block = int(block, 16)

            # add zero padding if the last block is less than 4 hex digits
            if len(plain_blocks) > 1 and len(block) < 4:
                binary_block = binary_block << (4 - len(block)) * 4

            # send the counter through the fiestel network
            cypher = self.encrypt_block(self.nonce ^ self.counter)
            self.counter += 1

            # xor the plaintext with the encrypted counter and store the result in cypher text
            cypher_block = hex(binary_block ^ cypher)[2:]

            cypher_block = f'{"0" * (4-len(cypher_block))}{cypher_block}'
            cypher_text.append(cypher_block)

        return ''.join(cypher_text)

    def encrypt_block(self, block):
        for n in range(self.total_rounds):
            upper = (block & 0xFF00) >> 8
            lower = block & 0xFF

            upper ^= self.round_function(self.schedule(self.key, n), lower)

            block = (lower << 8) | upper

        upper = (block & 0xFF00) >> 8
        lower = block & 0xFF
        return (lower << 8) | upper


def xor_round_function(subkey, message):
    return subkey ^ message


def subkey_schedule(key, n):
    for i in range(n * 4):
        key = left_roll(key)
    return (key & 0xFF) ^ (primes_table[n % len(primes_table)] & 0xFF)


# left roll for 16 bit ints
def left_roll(x):
    return ((x << 1) | (x & 0x8000) >> 15) & 0xFFFF


# right roll for 16 bit ints
def right_roll(x):
    return ((x >> 1) | (x & 0x1) << 15) & 0xFFFF


def main():
    args = input("Input string: \n")

    args = args.split(" ")

    network = FeistelNetwork(int(args[1], 16), xor_round_function, subkey_schedule)
    network.nonce = int(args[0], 16)

    cypher = network.encrypt(args[2])
    print("Cypher Text:    ", cypher)
    network.counter = 0
    print("Decrypted Text: ", network.encrypt(cypher))


if __name__ == '__main__':
    main()

