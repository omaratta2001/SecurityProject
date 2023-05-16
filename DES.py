s_box = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
INITIAL_PERMUTATION_TABLE = [58, 50, 42, 34, 26, 18, 10, 2,
                            60, 52, 44, 36, 28, 20, 12, 4,
                            62, 54, 46, 38, 30, 22, 14, 6,
                            64, 56, 48, 40, 32, 24, 16, 8,
                            57, 49, 41, 33, 25, 17, 9, 1,
                            59, 51, 43, 35, 27, 19, 11, 3,
                            61, 53, 45, 37, 29, 21, 13, 5,
                            63, 55, 47, 39, 31, 23, 15, 7]
E_table = [32, 1, 2, 3, 4, 5, 4, 5,
           6, 7, 8, 9, 8, 9, 10, 11,
           12, 13, 12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21, 20, 21,
           22, 23, 24, 25, 24, 25, 26, 27,
           28, 29, 28, 29, 30, 31, 32, 1]
p_box = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]


pc1_table = [57, 49, 41, 33, 25, 17, 9,
             1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27,
             19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 28, 20, 12, 4]


PC2_TABLE = [14, 17, 11, 24, 1, 5,
             3, 28, 15, 6, 21, 10,
             23, 19, 12, 4, 26, 8,
             16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32]
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


FINAL_PERMUTATION_TABLE = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]


def encrypt_DES(plaintext, keys):
    # Initial Permutation
    plaintext = initial_permutation(plaintext)

    # Divide the 64-bit input into two 32-bit halves, left and right
    left, right = divide_into_halves(plaintext)

    # Perform 16 rounds of encryption
    for i in range(16):
        # Expand the 32-bit right half to 48 bits using the E-bit selection table
        expanded_right = expand_right_half(right)

        # XOR the 48-bit result with the corresponding 48-bit round key
        round_key = keys[i]
        xored = xor_with_round_key(expanded_right, round_key)

        # Divide the resulting 48 bits into eight 6-bit blocks, each of which is passed through a corresponding S-box to obtain a 4-bit output
        s_box_output = s_box_substitution(xored)

        # Combine the eight 4-bit outputs to obtain a 32-bit output using the P-box permutation
        p_box_output = p_box_permutation(s_box_output)

        # XOR the 32-bit output with the left half of the input
        xored_output = xor_output_left_half(left, p_box_output)

        # Swap the left and right halves
        left = right
        right = xored_output

    # Combine the right and left halves
    ciphertext = right + left

    # Final Permutation
    ciphertext = final_permutation(ciphertext)

    return ciphertext

def decrypt_DES(ciphertext, keys):
    # Initial Permutation
    ciphertext = initial_permutation(ciphertext)

    # Divide the 64-bit input into two 32-bit halves, left and right
    left, right = divide_into_halves(ciphertext)

    # Perform 16 rounds of decryption in reverse order
    for i in reversed(range(16)):
        # Expand the 32-bit right half to 48 bits using the E-bit selection table
        expanded_right = expand_right_half(right)

        # XOR the 48-bit result with the corresponding 48-bit round key
        round_key = keys[i]
        xored = xor_with_round_key(expanded_right, round_key)

        # Divide the resulting 48 bits into eight 6-bit blocks, each of which is passed through a corresponding S-box to obtain a 4-bit output
        s_box_output = s_box_substitution(xored)

        # Combine the eight 4-bit outputs to obtain a 32-bit output using the P-box permutation
        p_box_output = p_box_permutation(s_box_output)

        # XOR the 32-bit output with the left half of the input
        xored_output = xor_output_left_half(left, p_box_output)

        # Swap the left and right halves
        left = right
        right = xored_output

    # Combine the right and left halves
    plaintext = right + left

    # Final Permutation
    plaintext = final_permutation(plaintext)

    return plaintext





def xor_output_left_half(output_bits, left_half_bits):
    # Convert the output bits string to a list of integers
    output_list = [int(bit) for bit in output_bits]

    # Convert the left half bits string to a list of integers
    left_half_list = [int(bit) for bit in left_half_bits]

    # Perform the XOR operation between the output bits and the left half bits
    xored_bits = [output_list[i] ^ left_half_list[i] for i in range(len(output_list))]

    # Convert the resulting bits to a string and return it
    return ''.join([str(bit) for bit in xored_bits])


def divide_into_halves(input_bits):
    # Divide the input into left and right halves
    left_half = input_bits[:32]
    right_half = input_bits[32:]

    return left_half, right_half


def p_box_permutation(output_bits):
    # Define the P-box permutation (omitted for brevity)


    # Convert the output bits string to a list of integers
    output_list = [int(bit) for bit in output_bits]

    # Apply the P-box permutation to the output bits
    permuted_bits = [output_list[i - 1] for i in p_box]

    # Convert the permuted bits to a string and return it
    return ''.join([str(bit) for bit in permuted_bits])


def s_box_substitution(xored_bits):
    # Define the S-boxes (omitted for brevity)

    # Divide the 48-bit input into eight 6-bit blocks
    blocks = [xored_bits[i:i + 6] for i in range(0, 48, 6)]

    # Perform S-box substitution on each block
    output_bits = []
    for i in range(8):
        # Extract the current block and corresponding S-box
        current_block = blocks[i]
        current_s_box = s_box[i]

        # Convert the block to row and column indices
        row_index = int(current_block[0] + current_block[5], 2)
        col_index = int(current_block[1:5], 2)

        # Perform S-box substitution on the row and column indices
        s_box_output = current_s_box[row_index][col_index]

        # Convert the resulting output to binary and append it to the output bits list
        output_bits += [int(bit) for bit in bin(s_box_output)[2:].zfill(4)]

    # Convert the output bits list to a string and return it
    return ''.join([str(bit) for bit in output_bits])


def xor_with_round_key(expanded_right_half, round_key):
    # Convert the expanded right half and the round key to binary lists
    expanded_right_half_list = [int(bit) for bit in expanded_right_half]
    round_key_list = [int(bit) for bit in round_key]

    # XOR the expanded right half with the round key
    xored_bits = [expanded_right_half_list[i] ^ round_key_list[i] for i in range(48)]

    # Convert the resulting binary list back to a string
    xored_string = ''.join([str(bit) for bit in xored_bits])

    return xored_string


def expand_right_half(right_half):
    # Apply the E-bit selection table to the right half
    expanded_right_half = [right_half[E_table[i] - 1] for i in range(48)]

    return ''.join(expanded_right_half)

def circular_left_shift(bits, shift):
    """Performs a circular left shift on the given bit string by the specified number of positions."""
    return bits[shift:] + bits[:shift]
def pc1_permutation(key):
    # PC-1 permutation table
    permuted_key = ''
    for i in pc1_table:
        permuted_key += key[i-1]
    return permuted_key

def combine_halves(left, right):
    combined_key = left + right
    return combined_key



def pc2_permutation(combined_key):
    round_key = ''
    for index in PC2_TABLE:
        round_key += combined_key[index - 1]
    return round_key



def generate_round_keys(master_key):
    # PC1 Permutation

    permuted_key = pc1_permutation(master_key)

    # Split the permuted key into two 28-bit halves
    left, right = divide_into_halves(permuted_key)

    round_keys = []

    # Perform 16 rounds of key generation
    for i in range(16):
        # Perform circular left shift on the two 28-bit halves
        left = circular_left_shift(left, SHIFT_SCHEDULE[i])
        right = circular_left_shift(right, SHIFT_SCHEDULE[i])

        # Combine the two 28-bit halves
        combined_key = combine_halves(left, right)

        # PC2 Permutation
        round_key = pc2_permutation(combined_key)

        # Add the round key to the list of round keys
        round_keys.append(round_key)

    return round_keys


def initial_permutation(plaintext):
    # Apply the initial permutation to the plaintext
    permuted = [0] * 64
    for i in range(64):
        permuted[i] = plaintext[INITIAL_PERMUTATION_TABLE[i] - 1]
    return permuted



def final_permutation(ciphertext):
    output = ''
    for i in range(64):
        output += ciphertext[FINAL_PERMUTATION_TABLE[i]-1]
    return output



def bin_to_str(binary):
    # Pad the binary string with zeros if its length is not divisible by 8
    if len(binary) % 8 != 0:
        binary = binary.zfill((len(binary) // 8 + 1) * 8)

    # Convert the binary string to a byte array
    byte_array = bytearray(int(binary[i:i + 8], 2) for i in range(0, len(binary), 8))

    # Convert the byte array to a string
    return ''.join(chr(b) for b in byte_array)


def text_to_binary(text):
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    return binary


if __name__ == '__main__':

    key = input("Enter the master key: ")

    # Convert the key to binary
    key_binary = text_to_binary(key)
    # Generate the round keys from the master key
    round_keys = generate_round_keys(key_binary)

    # Get the plaintext from the user
    plaintext = input("Enter the plaintext: ")

    # Split the plaintext into 8 characters in a list
    plaintext_list = [plaintext[i:i + 8] for i in range(0, len(plaintext), 8)]
    if len(plaintext_list[-1]) < 8:
        plaintext_list[-1] += ' ' * (8 - len(plaintext_list[-1]))

    print(plaintext_list)
    # Encrypt each block of plaintext
    ciphertext_list = []
    for block in plaintext_list:
        # Convert the block to binary
        block_binary = text_to_binary(block)
        print(block_binary)
        # Encrypt the block using the round keys
        ciphertext_binary = encrypt_DES(block_binary, round_keys)

        # Convert the ciphertext back to a string and add it to the list
        ciphertext_list.append(bin_to_str(ciphertext_binary))
    print("Ciphertext: " + "".join(ciphertext_list))

    plaintext_list1=[]
    for block in ciphertext_list:
        # Convert the block to binary
        block_binary = text_to_binary(block)
        print(block_binary)

        # Encrypt the block using the round keys
        ciphertext_binary = decrypt_DES(block_binary, round_keys)

        # Convert the ciphertext back to a string and add it to the list
        plaintext_list1.append(bin_to_str(ciphertext_binary))

    # Print the ciphertext
    print("PlainText: " + "".join(plaintext_list1))

