import string

alphabet = string.ascii_letters + '1234567890' + '+-=*/\_'
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ''

    split_msg = [message[i:i + len(key)]
                 for i in range(0, len(message), len(key))]

    for each_split in split_msg:
        for i, letter in enumerate(each_split):
            num = (letter_to_index[letter] +
                   letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[num]
    return encrypted


def decrypt(cipher, key):
    decrypted = ''

    split_cipher = [cipher[i:i + len(key)]
                    for i in range(0, len(cipher), len(key))]

    for each_split in split_cipher:
        for i, letter in enumerate(each_split):
            num = (letter_to_index[letter] -
                   letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[num]
    return decrypted
