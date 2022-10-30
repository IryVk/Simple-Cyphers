import secrets


def main():
    # asks user for required function until valid response is given
    while True:
        function = input("Do you want to encrypt or decrypt? ").strip().lower()
        if function in ["encrypt", "decrypt"]:
            break
        print("Invalid function, please choose one of the following (encrypt/decrypt).")

    print(railfence(function))


def railfence(function):
    # ask if text will be provided in terminal or from file
    while True:
        choice = input("Read from (f)ile or (w)rite text here? (f/w) ").lower().strip()
        if choice not in ["f", "w"]:
            print(
                "Invalid, please write 'f' to read from file or 'w' to write text here."
            )
        else:
            break

    # get file from user
    if choice == "f":
        while True:
            try:
                filename = input("File name? ")
                inptr = open(filename, "r")
                break
            except FileNotFoundError:
                print(
                    """Couldn't find file. Make sure file is inside project folder, otherwise write the path to the file and make sure to write the file extension, ex: ###.txt"""
                )

        phrase = inptr.read()
        inptr.close()

    # get text from user
    elif choice == "w":
        phrase = input("Enter Text: ")

    # ask if user has key or wants an auto key
    while True:
        choice2 = (
            input(
                """If you are decrypting from a file created by this program choose 'r'. Otherwise feel free to choose.\n(P)rovide key or use (r)andom key/
                     (r)ead key from file?(p/r) """
            )
            .lower()
            .strip()
        )
        if choice2 not in ["p", "r"]:
            print(
                "Invalid, please write 'p' to give key or 'r' to randomly generate a key."
            )

        elif choice2 == "r" and function == "decrypt" and choice == "w":
            print(
                "Cannot find key automatically to decrypt text written in terminal, please manually provide key."
            )

        else:
            break

    # using secret library to randomly generate the key
    if choice2 == "r":
        key = secrets.randbelow(10)

    # taking key input from user and ensuring it is valid
    elif choice2 == "p":
        while True:
            try:
                key = int(input("Key: "))
                if key >= len(phrase):
                    raise ValueError
                break
            except ValueError:
                print(
                    "Invalid Key, please enter an integer smaller than size of text"
                )  # if key is bigger than or equal to the text, the output will just be the regular text

    if function == "encrypt":
        encryption = encrypt(phrase, key)
        if choice == "f":
            outptr = open("out_" + filename, "w")
            keyptr = open("key_out_" + filename, "w")
            keyptr.writelines(str(key) + "\n")
            outptr.writelines(encryption)
            outptr.close()
            keyptr.close()

        if choice2 == "r":
            return encryption, key
        return encryption

    elif function == "decrypt":
        # read key from file in case file is generated by program
        if choice2 == "r" and choice == "f":
            while True:
                try:
                    inptr = open("key_" + filename, "r")
                    key = int(inptr.readline())
                    break
                except FileNotFoundError:
                    return "Cannot find file containing the key."
                except ValueError:
                    return "Provided file does not have a Valid Key."
            # phrase = inptr.read()
            inptr.close()

        decryption = decrypt(phrase, key)
        if choice == "f":
            outptr = open("out_" + filename, "w")
            outptr.writelines(decryption)
            outptr.close()
        return decryption


def encrypt(plaintext, key):
    # make 2d array to store characters
    railroad = [["" for x in range(len(plaintext))] for y in range(key)]
    row = 0
    shiftcycle = False  # flag to know which way to go up or down

    for i in range(len(plaintext)):
        railroad[row][i] = plaintext[i]

        if shiftcycle:
            row -= 1
        else:
            row += 1

        if row == key - 1:
            shiftcycle = True
        elif row == 0:
            shiftcycle = False

    # copy resulting array into a string and return it
    encrypted = ""
    for i in range(key):
        for j in range(len(plaintext)):
            encrypted += railroad[i][j]
    return encrypted


def decrypt(ciphertext, key):
    # make 2d array to store characters
    railroad = [["" for x in range(len(ciphertext))] for y in range(key)]
    row = 0
    shiftcycle = False  # flag to know which way to go up or down

    for i in range(len(ciphertext)):
        railroad[row][i] = "*"  # place holder to know where the characters will be

        if shiftcycle:
            row -= 1
        else:
            row += 1

        if row == key - 1:
            shiftcycle = True
        elif row == 0:
            shiftcycle = False

    counter = 0  # to count which character we are in
    for i in range(key):
        for j in range(len(ciphertext)):
            if (railroad[i][j] == "*") and (counter < len(ciphertext)):
                railroad[i][j] = ciphertext[counter]
                counter += 1

    # now we have a 2d array of the characters, we just have to copy it into a string
    # we have to read in a zigzag
    decrypted = ""
    row = 0
    shiftcycle = False  # flag to know which way to go up or down
    for i in range(len(ciphertext)):
        decrypted += railroad[row][i]

        if shiftcycle:
            row -= 1
        else:
            row += 1

        if row == key - 1:
            shiftcycle = True
        elif row == 0:
            shiftcycle = False

    return decrypted


if __name__ == "__main__":
    main()
