def main():
    #asks user for required function until valid response is given
    while True:
        function = input("Do you want to encrypt or decrypt? ").strip().lower()
        if function in ["encrypt", "decrypt"]:
            break
        print("Invalid function, please choose one of the following (encrypt/decrypt).")

    print(caesar(function))


def caesar(function):
    phrase = input("Enter Text: ")
    while True:
        try:
            key = int(input("Key: "))
            if key > 95 or key < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid Key, please enter an integer between 1 & 95") #key can be up to 95 because it's still within constraints of ascii characters we can use

    if function == "encrypt":
        return encrypt(phrase, key)

    elif function == "decrypt":
        return decrypt(phrase, key)


def encrypt(ciphertext, key):
    encrypted = ""
    for char in range(len(ciphertext)):
        x = ord(ciphertext[char])
        #make sure x is in values we can change before we change it
        if 126 >= x >= 32:
            x = ((x + key - 32) % 95) + 32
        encrypted += chr(x)
    
    return encrypted


def decrypt(plaintext, key):
    decrypted = ""
    for char in range(len(plaintext)):
        x = ord(plaintext[char])
        if 126 >= x >= 32:
            x = ((x - key - 32) % 95) + 32
        decrypted += chr(x)
    
    return decrypted


if __name__ == "__main__":
    main()