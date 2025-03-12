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

alphabet = "abcdefghijklmnopqrstuvwxyz"
square = vigenere_sq(alphabet)

key = "bluesmurf"
plaintext = "One small step for man, one giant leap for mankind."
cipher = encrypt_vigenere_v2(key.lower(),plaintext.lower(),alphabet)
print(cipher)
print("-")
print(decrypt(key,cipher,alphabet))