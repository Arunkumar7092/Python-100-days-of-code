from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
conti = True
while conti == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    def encrypt(paramater_text,parameter_shift):
        encrypted_text=""
        for letters in paramater_text:
            if letters in alphabet:
                position = alphabet.index(letters)
                new_position = position + parameter_shift
                encrypted_text+= alphabet[new_position]
            else:
                encrypted_text += letters
        print(f"your encrypted text is {encrypted_text}")
        print("If you wish to decrypt the same above encrypted message continue with caesar cipher")

    def decrypt(paramater_text,parameter_shift):
        decrypted_text=""
        for letters in paramater_text:
            if letters in alphabet:
                position = alphabet.index(letters)
                new_position = position - parameter_shift
                decrypted_text+= alphabet[new_position]
            else:
                decrypted_text+= letters
        print(f"your encrypted text is {decrypted_text}")
        print("If you wish to encrypt the same above decrypted message continue with caesar cipher")



    if direction == "encode":
        encrypt(paramater_text = text ,parameter_shift = shift)
    else:
        decrypt(paramater_text = text ,parameter_shift = shift)

    loop = input("Type 'yes' to continue encoding and decrypting and no to stop encoding and decrypting : ").lower()

    if loop == "no":
        conti = False
