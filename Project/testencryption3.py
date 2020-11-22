import binascii


def encfunction(text):
    enclist = [b^11 for b in text]
    return enclist
def decfunction(text):
    declist = [b^11 for b in text]
    return declist


while(True):
    word = input("enter a message: \n")
    action = input("enter 'e' to encrypt, 'd' to decrypt:\n ")
    if action == 'e':
        print("Encrypting...")
        utf8 = binascii.hexlify(word.encode("utf8"))
        print(bytes(encfunction(utf8)))  # הופך רשימה של אינטים חזרה לבייטים

    elif action == 'd':
        word = bytes(word, 'utf-8')
        print("Decrypting...")
        utf8 = decfunction(word)
        print(binascii.unhexlify(utf8).decode("utf8"))
        print(bytes(encfunction(utf8)))
        print(type(word))
    else:
        print("try again")
