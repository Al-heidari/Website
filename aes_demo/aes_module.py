class AES:
    SBOX = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]
    INV_SBOX = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
    ]
    RCON = [
        0x00000000, 0x01000000, 0x02000000, 0x04000000,
        0x08000000, 0x10000000, 0x20000000, 0x40000000,
        0x80000000, 0x1b000000, 0x36000000, 0x6c000000,
        0xd8000000, 0xab000000, 0x4d000000, 0x9a000000
    ]

    def __init__(self, key):
        if len(key) not in [16, 24, 32]:
            raise ValueError("Key must be 16, 24, or 32 bytes long (128, 192, or 256 bits).")
        self.key = key
        self.Nk = len(key) // 4
        self.Nb = 4
        self.Nr = self.Nk + 6
        self.round_keys = self.key_expansion()

    def galois_mult(self, a, b):
        product = 0
        for _ in range(8):
            if b & 1:
                product ^= a
            hi_bit_set = a & 0x80
            a = (a << 1) & 0xFF
            if hi_bit_set:
                a ^= 0x1B
            b >>= 1
        return product

    def RotWord(self, word):
        return ((word << 8) & 0xffffffff) | (word >> 24)

    def SubWord(self, word):
        return (self.SBOX[word >> 24] << 24) | (self.SBOX[(word >> 16) & 0xff] << 16) | (self.SBOX[(word >> 8) & 0xff] << 8) | self.SBOX[word & 0xff]

    def key_expansion(self):
        w = [0] * (self.Nb * (self.Nr + 1))
        for i in range(self.Nk):
            w[i] = int.from_bytes(self.key[4 * i: 4 * (i + 1)], byteorder='big')
        for i in range(self.Nk, self.Nb * (self.Nr + 1)):
            temp = w[i - 1]
            if i % self.Nk == 0:
                temp = self.SubWord(self.RotWord(temp)) ^ self.RCON[i // self.Nk]
            elif self.Nk > 6 and i % self.Nk == 4:
                temp = self.SubWord(temp)
            w[i] = w[i - self.Nk] ^ temp
        return w

    def add_round_key(self, state, round_key):
        round_key_bytes = []
        for word in round_key:
            round_key_bytes.extend(word.to_bytes(4, byteorder='big'))
        return [state[i] ^ round_key_bytes[i] for i in range(len(state))]


class Encryption_AES(AES):
    def sub_bytes(self, state):
        return [self.SBOX[b] for b in state]

    def shift_rows(self, state):
        num_rows = 4
        for i in range(1, num_rows):
            state[i::num_rows] = state[i::num_rows][i:] + state[i::num_rows][:i]
        return state

    def mix_columns(self, state):
        for i in range(4):
            a = state[i*4:(i+1)*4]
            state[i*4+0] = self.galois_mult(a[0], 2) ^ self.galois_mult(a[1], 3) ^ self.galois_mult(a[2], 1) ^ self.galois_mult(a[3], 1)
            state[i*4+1] = self.galois_mult(a[0], 1) ^ self.galois_mult(a[1], 2) ^ self.galois_mult(a[2], 3) ^ self.galois_mult(a[3], 1)
            state[i*4+2] = self.galois_mult(a[0], 1) ^ self.galois_mult(a[1], 1) ^ self.galois_mult(a[2], 2) ^ self.galois_mult(a[3], 3)
            state[i*4+3] = self.galois_mult(a[0], 3) ^ self.galois_mult(a[1], 1) ^ self.galois_mult(a[2], 1) ^ self.galois_mult(a[3], 2)
        return state

    def cipher(self, input_bytes):
        state = input_bytes
        round_keys = self.key_expansion()
        state = self.add_round_key(state, round_keys[0:self.Nb])
        for round in range(1, self.Nr):
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, round_keys[round * self.Nb: (round + 1) * self.Nb])
        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, round_keys[self.Nr * self.Nb: (self.Nr + 1) * self.Nb])
        return state


class Decryption_AES(AES):
    def invsub_bytes(self, state):
        return [self.INV_SBOX[b] for b in state]

    def invshift_rows(self, state):
        num_rows = 4
        for i in range(1, num_rows):
            state[i::num_rows] = state[i::num_rows][-i:] + state[i::num_rows][:-i]
        return state

    def invmix_columns(self, state):
        for i in range(4):
            a = state[i*4:(i+1)*4]
            state[i*4+0] = self.galois_mult(a[0], 0x0e) ^ self.galois_mult(a[1], 0x0b) ^ self.galois_mult(a[2], 0x0d) ^ self.galois_mult(a[3], 0x09)
            state[i*4+1] = self.galois_mult(a[0], 0x09) ^ self.galois_mult(a[1], 0x0e) ^ self.galois_mult(a[2], 0x0b) ^ self.galois_mult(a[3], 0x0d)
            state[i*4+2] = self.galois_mult(a[0], 0x0d) ^ self.galois_mult(a[1], 0x09) ^ self.galois_mult(a[2], 0x0e) ^ self.galois_mult(a[3], 0x0b)
            state[i*4+3] = self.galois_mult(a[0], 0x0b) ^ self.galois_mult(a[1], 0x0d) ^ self.galois_mult(a[2], 0x09) ^ self.galois_mult(a[3], 0x0e)
        return state

    def eq_inv_cipher(self, ciphertext):
        state = ciphertext
        round_keys = self.key_expansion()
        state = self.add_round_key(state, round_keys[self.Nr * self.Nb: (self.Nr + 1) * self.Nb])
        for round in range(self.Nr - 1, 0, -1):
            state = self.invshift_rows(state)
            state = self.invsub_bytes(state)
            state = self.add_round_key(state, round_keys[round * self.Nb: (round + 1) * self.Nb])
            state = self.invmix_columns(state)
        state = self.invshift_rows(state)
        state = self.invsub_bytes(state)
        state = self.add_round_key(state, round_keys[0:self.Nb])
        return state