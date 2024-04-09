import random
import string

alphabet_kv_pairs = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}


def get_key_in_alphabet_kv_pairs(value):
    for k, v in alphabet_kv_pairs.items():
        if v == value:
            return k
    return None


def encrypt_message(message_string, key):
    encrypt_string: [str] = ""
    for char in message_string:
        if char == " ":
            encrypt_string += random.choice(string.digits + string.punctuation)
        else:
            char_index: [int] = alphabet_kv_pairs[char]
            encrypt_char_index: [int] = (char_index + key) % 26
            encrypt_string += get_key_in_alphabet_kv_pairs(encrypt_char_index)

    return encrypt_string


def decrypt_message(message_string, key):
    decrypt_string: [str] = ""
    for char in message_string:
        if char in (string.digits + string.punctuation):
            decrypt_string += " "
        else:
            char_index: [int] = alphabet_kv_pairs[char]
            decrypt_char_index: [int] = (char_index - key) % 26
            decrypt_string += get_key_in_alphabet_kv_pairs(decrypt_char_index)

    return decrypt_string


end_program = False
while not end_program:
    user_choice: [str] = ""
    while user_choice != "encode" and user_choice != "decode":
        user_choice = input("Type 'encode' to encrypt, or type 'decode' to decrypt: ").lower()
    user_message: [str] = input("Enter your message: ")
    shift_key: [int] = int(input("Enter your shift_key: "))

    if user_choice == "encode":
        encoded_message = encrypt_message(user_message, shift_key)
        print(f"Here is your encrypted message: {encoded_message}")
    else:
        decoded_message = decrypt_message(user_message, shift_key)
        print(f"Here is your decrypted message: {decoded_message}")

    go_again = input("Type 'yes' if you want to go again, or type 'no': ").lower()
    if go_again == "no":
        end_program = True
