def main():
    #asks user for required function until valid response is given
    while True:
        function = input("Do you want to encrypt or decrypt? ").strip().lower()
        if function in ["encrypt", "decrypt"]:
            break
        print("Invalid function, please choose one of the following (encrypt/decrypt).")

    print(vigenere(function))


def vigenere(function):
    phrase = input("Enter Text: ")
    while True:
        try:
            key = input("Key: ")
            for i in range(len(key)):
                if ord(key[i]) < 32 or ord(key[i]) > 126:
                    raise ValueError
            break
        except ValueError:
            print("Invalid Key") #key can only contain chars within 32-126 in ascii code

    if function == "encrypt":
        return encrypt(phrase, key)

    elif function == "decrypt":
        return decrypt(phrase, key)


def encrypt(plaintext, key):
    encrypted = ""
    counter = 0   #counter to help us repeat key until all text is encrypted
    for i in range(len(plaintext)):
        x = ord(plaintext[i])
        #make sure x is in values we can change before we change it
        if 126 >= x >= 32:
            x = ((x + ord(key[counter]) - 32) % 95) + 32
        encrypted += chr(x)
        counter += 1
        if counter == len(key): # when counter reaches end of key, reset counter
            counter = 0
    
    return encrypted


def decrypt(ciphertext, key):
    decrypted = ""
    counter = 0   #counter to help us repeat key until all text is encrypted
    for i in range(len(ciphertext)):
        x = ord(ciphertext[i])
        #make sure x is in values we can change before we change it
        if 126 >= x >= 32:
            x = ((x - ord(key[counter]) - 32 + 95) % 95) + 32
        decrypted += chr(x)
        counter += 1
        if counter == len(key): # when counter reaches end of key, reset counter
            counter = 0
    
    return decrypted


if __name__ == "__main__":
    main()
