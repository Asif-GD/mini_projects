# caesar cipher using lists

"""
Algorithm
step 1 - get the message
step 2 - get the shift
step 3 - encrypt
step 4 - display encrypt message
step 5 - decrypt
step 6 - display decrypt message
"""
alphabet_list: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
encrypt function:
1. get the index of the char from the message by looking up from the alphabets_list
2. add the shift to this index
3. get the new char from the alphabets_list based on the new index
4. build the encrypted message
"""


def encrypt_message(message, shift) -> str:
    new_message: str = ""
    for char in message:
        if char == " ":
            new_message += " "
        else:
            char_index = alphabet_list.index(char)
            new_index = char_index + shift
            if new_index >= 26:
                new_index %= 26
            new_char = alphabet_list[new_index]
            new_message += new_char

    return new_message


"""
decrypt function:
1. get the index of the char from the message by looking up from the alphabets_list
2. add the shift to this index
3. get the new char from the alphabets_list based on the new index
4. build the encrypted message
"""


def decrypt_message(message, shift) -> str:
    new_message: str = ""
    for char in message:
        if char == " ":
            new_message += " "
        else:
            char_index = alphabet_list.index(char)
            new_index = char_index - shift
            if new_index < 1:
                new_index %= 26
            new_char = alphabet_list[new_index]
            new_message += new_char

    return new_message


use_script: [str] = "yes"

while use_script == "yes":

    user_choice: [str] = ""

    while user_choice != "encode" and user_choice != "decode":
        user_choice = input("Type 'encode' to encrypt message or 'decode' to decrypt message: ").lower()
        if user_choice != "encode" and user_choice != "decode":
            print("Invalid choice. Please choose one of the options given.")

    user_message = input("Enter your message: ").lower()
    key = int(input("Enter the shift number: "))

    if user_choice == "encode":
        cryptic_message = encrypt_message(user_message, key)
        print(f"Here's the encoded result: {cryptic_message}")
    else:
        cryptic_message = decrypt_message(user_message, key)
        print(f"Here's the decoded result: {cryptic_message}")

    use_script = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
