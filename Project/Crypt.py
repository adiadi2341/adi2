import binascii

word = input("\n enter a sentence to encrypt or decrypt, the program will understand which one:\n ")

if word.__contains__('a') or word.__contains__('b') or word.__contains__('c') or word.__contains__('d') or word.__contains__('e') or word.__contains__('f'):
    print("\n \n Decrypting...")
    print(binascii.unhexlify(word).decode("utf8"))
elif word == '':
    print('\n \n There is nothing here')
else:
    word = binascii.hexlify(word.encode("utf8"))
    print("\n \n Encrypting...")
print(word)