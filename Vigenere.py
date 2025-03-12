from sys import exit

def vigenere_head(alphabet:str):
    return list(" ") + list(alphabet)

def vigenere_sq(alphabet:str):
    alphabet = list(alphabet)
    sq_list = [vigenere_head(alphabet)]
    alpha_len = len(alphabet)
    for i in range(alpha_len):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere_sq_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f"| {" | ".join(row)} |")
        if i == 0:
            print(f"{"|---" * len(row)}" + "|")


def letter_to_index_v2(letter:str,alphabet:str):
    return alphabet.upper().find(letter.upper())

def index_to_letter_v1(index,alphabet:str):
    alpha_len = len(alphabet)
    if 0 <= index < alpha_len:
        return alphabet[index]

def vigenere_index_v2(key_letter, plaintext_letter, alphabet):
    result = index_to_letter_v1(
        (letter_to_index_v2(plaintext_letter,alphabet) +
        letter_to_index_v2(key_letter,alphabet)) % len(alphabet),
        alphabet
    )
    if result is None:
        print(len(alphabet))
        print(key_letter, plaintext_letter)
        print(letter_to_index_v2(plaintext_letter,alphabet))
        print(letter_to_index_v2(key_letter,alphabet))
    return result

def encrypt_vigenere_v2(key,plaintext,alphabet):
    cipher_text = []
    counter = 0
    for i, c in enumerate(plaintext):
        if c == " ":
            cipher_text.append(" ")
        elif c in alphabet:
            cipher_text.append(vigenere_index_v2(key[counter % len(key)],c,alphabet))
            counter += 1
    #print(cipher_text)
    return "".join(cipher_text)

def non_vigenere_index_v2(key_letter, cipher_text, alphabet):
    #print(len(alphabet)) :3
    return index_to_letter_v1(
        (letter_to_index_v2(cipher_text,alphabet) -
        letter_to_index_v2(key_letter,alphabet) + len(alphabet)) % len(alphabet),
        alphabet
    )

def decrypt(key,cipher_text,alphabet):
    cipher_text = cipher_text.lower()
    plaintext = []
    counter = 0
    for c in cipher_text:
        if c == " ":
            plaintext.append(" ")
        elif c in alphabet:
            plaintext.append(non_vigenere_index_v2(key[counter % len(key)], c , alphabet))
            counter += 1
    #print(plaintext)
    return "".join(plaintext)

def enc_menu(key,alphabet,encrypt_list):
    plaintext = input("Enter text to encrypt: ")
    encrypt_list.append(encrypt_vigenere_v2(key,plaintext,alphabet))

def dec_menu(key,alphabet,encrypt_list):
    results = []
    for cipher_text in encrypt_list:
        results.append(decrypt(key,cipher_text,alphabet))
    return results

def dec_dump(encrypt_list):
    return encrypt_list

def main():
    encrypt_list = []
    key = "bluesmurf"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = "one small step for man, one giant leap for mankind"
    menu = [
        ["1) Encrypt", enc_menu, [key, alphabet,encrypt_list]], # LIST IN A LIST !!!!!!!!!!!!!!!
        ["2) Decrypt", dec_menu, [key,alphabet,encrypt_list]],
        ["3) Dump Decrypt", dec_dump, [encrypt_list]],
        ["4) Quit", exit, [0]]
    ]
    while True:
        for menu_item in menu:
            print(menu_item[0])

        try:
            choice = int(input("Make your choice"))
            if not (0 < choice <= len(menu)):
                print("Must be between 0 and 5")
            else:
                result = menu[choice-1][1](*menu[choice-1][2])
                if result: print(result)
        except ValueError as ignored:
            print("must be int")

if __name__ == "__main__":
    main()