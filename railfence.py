def main():
#asks user for required function until valid response is given
    while True:
        function = input("Do you want to encrypt or decrypt? ").strip().lower()
        if function in ["encrypt", "decrypt"]:
            break
        print("Invalid function, please choose one of the following (encrypt/decrypt).")

    print(railfence(function))


def railfence(function):
    phrase = input("Enter Text: ")
    while True:
        try:
            key = int(input("Key: "))
            if key >= len(phrase):
                raise ValueError
            break
        except ValueError:
            print("Invalid Key, please enter an integer smaller than size of text") #if key is bigger than or equal to the text, the output will just be the regular text

    if function == "encrypt":
        return encrypt(phrase, key)

    elif function == "decrypt":
        return decrypt(phrase, key)
    return


def encrypt(plaintext, key):
    #make 2d array to store characters
    railroad = [["" for x in range(len(plaintext))] for y in range(key)] 
    row = 0
    shiftcycle = False  #flag to know which way to go up or down

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

    #copy resulting array into a string and return it
    encrypted = ""
    for i in range(key):
        for j in range(len(plaintext)):
            encrypted += railroad[i][j]
    return encrypted
    

def decrypt(ciphertext, key):
    #make 2d array to store characters
    railroad = [["" for x in range(len(ciphertext))] for y in range(key)] 
    row = 0
    shiftcycle = False  #flag to know which way to go up or down

    for i in range(len(ciphertext)):
        railroad[row][i] = "*"  #place holder to know where the characters will be

        if shiftcycle:
            row -= 1
        else:
            row += 1

        if row == key - 1:
            shiftcycle = True
        elif row == 0:
            shiftcycle = False

    counter = 0  #to count which character we are in
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((railroad[i][j] == "*") and (counter < len(ciphertext))):
                railroad[i][j] = ciphertext[counter]
                counter += 1

    #now we have a 2d array of the characters, we just have to copy it into a string
    #we have to read in a zigzag
    decrypted = ""
    row = 0
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