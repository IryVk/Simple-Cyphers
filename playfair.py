def main():
    #asks user for required function until valid response is given
    while True:
        function = input("Do you want to encrypt or decrypt? ").strip().lower()
        if function in ["encrypt", "decrypt"]:
            break
        print("Invalid function, please choose one of the following (encrypt/decrypt).")

    print(playfair(function))


alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def playfair(function):
    phrase = input("Enter Text: ").lower()
        
    key = input("Key: ").strip().lower().replace(" ","")
    for char in key:
        if not char.isalpha():
            key.replace(char, "")
            
    grid = generatekey(key)

    if function == "encrypt":
        return encrypt(phrase, grid)

    elif function == "decrypt":
        return decrypt(phrase, grid)
    return


#generates 5x5 grid for key
def generatekey(key):
    keyletters = []
    for char in key:
        if char not in keyletters:
            keyletters.append(char)

    for char in alpha:
        if char not in keyletters:
            keyletters.append(char)
    
    #copy list of alphabet into a 2d array
    keygrid = []
    while keyletters != []:
        keygrid.append(keyletters[:5])
        keyletters = keyletters[5:]
 
    return keygrid
    


def encrypt(plaintext, key):
    for char in plaintext:
        if char not in alpha:
            plaintext.replace(char, "")

    #split input into two chars each time
    counter = 0
    i = 0
    splitted = []
    while counter < len(plaintext):
        splitted.append(plaintext[counter])
        counter += 1
        if counter == len(plaintext):
            break

        #if character is repeated, place bogus character
        if plaintext[counter] == splitted[i]:
            splitted[i] += "x"
        else:
            splitted[i] += plaintext[counter]
            counter += 1
        i += 1

    if len(splitted[-1]) < 2:
        splitted[-1] += "x"
    
        
    return


def decrypt(plaintext, key):
    
    return

if __name__ == "__main__":
    main()