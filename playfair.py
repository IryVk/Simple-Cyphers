import string
import secrets


def main():
    # asks user for required function until valid response is given
    while True:
        function = input("Do you want to encrypt or decrypt? ").strip().lower()
        if function in ["encrypt", "decrypt"]:
            break
        print("Invalid function, please choose one of the following (encrypt/decrypt).")

    print(playfair(function))


alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def playfair(function):
    # ask if text will be provided in terminal or from file
    while True:
        choice = input("Read from (f)ile or (w)rite text here?(f/w) ").lower().strip()
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

        phrase = "".join(inptr.readlines()).lower().replace("j", "i")
        inptr.close()

    # get text from user
    elif choice == "w":
        phrase = input("Enter Text: ").lower().replace("j", "i")

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

    # using secret library to randomly generate a 4 letter key
    if choice2 == "r":
        alphabet = string.ascii_lowercase
        key = "".join(secrets.choice(alphabet) for i in range(4)).replace("j", "i")

    elif choice2 == "p":
        # remove invalid chars from key
        key = input("Key: ").lower().replace("j", "i")
        for char in key:
            if char not in alpha:
                key = key.replace(char, "")

    # remove non alphabet letters
    for char in phrase:
        if char not in alpha:
            phrase = phrase.replace(char, "")

    # split input into two chars each time
    counter = 0
    i = 0
    splitted = []
    while counter < len(phrase):
        splitted.append(phrase[counter])
        counter += 1
        if counter == len(phrase):
            break

        # if character is repeated, place bogus character
        if phrase[counter] == splitted[i]:
            splitted[i] += "x"
        else:
            splitted[i] += phrase[counter]
            counter += 1
        i += 1

    # if last charcater is single add bogus character
    if len(splitted[-1]) < 2:
        splitted[-1] += "x"

    if function == "encrypt":
        grid = generatekey(key)
        encryption = encrypt(splitted, grid)

        if choice == "f":
            outptr = open("out_" + filename, "w")
            keyptr = open("key_out_" + filename, "w")
            keyptr.writelines(str(key) + "\n")
            outptr.writelines(encryption)
            outptr.close()
            keyptr.close()
        # out puts key if it is randomly generated
        if choice2 == "r":
            return encryption, key
        return encryption

    elif function == "decrypt":
        # read key from file in case file is generated by program
        if choice2 == "r" and choice == "f":
            while True:
                try:
                    inptr = open("key_" + filename, "r")
                    key = inptr.readline().replace("j", "i")  # clean up key
                    for char in key:
                        if char not in alpha:
                            key = key.replace(char, "")
                    break
                except FileNotFoundError:
                    return "Cannot find file containing the key."

            inptr.close()

        grid = generatekey(key)
        decryption = decrypt(splitted, grid)

        return decryption


# generates 5x5 grid for key
def generatekey(key):
    keyletters = []
    for char in key:
        if char not in keyletters:
            keyletters.append(char)

    for char in alpha:
        if char not in keyletters:
            keyletters.append(char)

    # copy list of alphabet into a 2d array
    keygrid = []
    while keyletters != []:
        keygrid.append(keyletters[:5])
        keyletters = keyletters[5:]

    return keygrid


# find char location in key
def find(char, key):
    for i in range(5):
        for j in range(5):
            if char == key[i][j]:
                return i, j


def encrypt(splitted, key):
    # loop over splitted and do as required
    for i in range(len(splitted)):
        x1, y1 = find(splitted[i][0], key)
        x2, y2 = find(splitted[i][1], key)
        # if in same row
        if x1 == x2:
            y1 += 1
            y2 += 1
            # loop back to start if reaches edge
            if y1 == 5:
                y1 = 0
            if y2 == 5:
                y2 = 0
        # if in same column
        elif y1 == y2:
            x1 += 1
            x2 += 1
            # loop back to start if reaches edge
            if x1 == 5:
                x1 = 0
            if x2 == 5:
                x2 = 0
        # if neither, form rectangle and switch horizontally
        else:
            tempy = y1
            y1 = y2
            y2 = tempy
        # now return values to splitted
        splitted[i] = key[x1][y1] + key[x2][y2]

    encrypted = "".join(splitted)
    return encrypted


def decrypt(splitted, key):
    # loop over splitted and do as required
    for i in range(len(splitted)):
        x1, y1 = find(splitted[i][0], key)
        x2, y2 = find(splitted[i][1], key)
        # if in same row
        if x1 == x2:
            y1 -= 1
            y2 -= 1
            # loop back to start if reaches edge
            if y1 == -1:
                y1 = 4
            if y2 == -1:
                y2 = 4
        # if in same column
        elif y1 == y2:
            x1 -= 1
            x2 -= 1
            # loop back to start if reaches edge
            if x1 == -1:
                x1 = 4
            if x2 == -1:
                x2 = 4
        # if neither, form rectangle and switch horizontally
        else:
            tempy = y1
            y1 = y2
            y2 = tempy
        # now return values to splitted
        splitted[i] = key[x1][y1] + key[x2][y2]

    encrypted = "".join(splitted)
    return encrypted


if __name__ == "__main__":
    main()
