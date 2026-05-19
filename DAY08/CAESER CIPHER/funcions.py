def encrypt(text, shift):
    new_message = ""
    for letter in text:
        ascii_value = ord(letter)
        if ascii_value >= 65 and ascii_value <= 90:
            ascii_value += shift
            if ascii_value > 90:
                ascii_value -= 26
        elif ascii_value >= 97 and ascii_value <= 122:
            ascii_value += shift
            if ascii_value > 122:
                ascii_value -= 26
        new_message += chr(ascii_value)
    return new_message

def decrypt(text, shift):
    new_message = ""
    for letter in text:
        ascii_value = ord(letter)
        if ascii_value >= 65 and ascii_value <= 90:
            ascii_value -= shift
            if ascii_value < 65:
                ascii_value += 26
        elif ascii_value >= 97 and ascii_value <= 122:
            ascii_value -= shift
            if ascii_value < 97:
                ascii_value += 26
        new_message += chr(ascii_value)
    return new_message

def texting():
    ind = True
    new_message = ""
    while ind:
        job = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:")
        if job == "encode":
            text = input("Type your message:")
            shift = int(input("Type the shift number:"))
            new_message = encrypt(text, shift)
            print(f"The encoded text is {new_message}")
        elif job == "decode":
            text = input("Type your message:")
            shift = int(input("Type the shift number:"))
            new_message = decrypt(text, shift)
            print(f"The decoded text is {new_message}")
        option = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.")
        if option == "no":
            ind = False
