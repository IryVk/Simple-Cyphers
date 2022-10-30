def main():
    # asks user for required function until valid response is given
    while True:
        function = input("Do you want to encrypt or decrypt? ").strip().lower()
        if function in ["encrypt", "decrypt"]:
            break
        print("Invalid function, please choose one of the following (encrypt/decrypt).")

    print(playfair(function))


alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def playfair(function):
    phrase = input("Enter Text: ").lower().replace("j", "i")
        
    # remove invalid chars from key
    key = input("Key: ").lower().replace("j", "i")
    for char in key:
        if char not in alpha:
            key = key.replace(char, "")
            
    grid = generatekey(key)

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

    #if last charcater is single add bogus character
    if len(splitted[-1]) < 2:
        splitted[-1] += "x"

    if function == "encrypt":
        return encrypt(splitted, grid)

    elif function == "decrypt":
        return decrypt(splitted, grid)
    return


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
