alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(start_text, shift_amount, cipher_direction):
    cipher_text = ""
    if direction == 'encode':
        for letter in start_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")
    elif direction == 'decode':
        for letter in start_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The decoded text is {cipher_text}")

ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)


'''def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")'''



'''def decrypt(dec_text, dec_shift):
    cipher_decrypt = ""
    for letter in dec_text:
        position = alphabet.index(letter)
        new_position = position - dec_shift
        new_letter = alphabet[new_position]
        cipher_decrypt += new_letter
    print(f"The decoded text is {cipher_decrypt}")'''




