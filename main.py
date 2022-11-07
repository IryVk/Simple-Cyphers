import sys
import caesar as c
import vigenere as v
import railfence as r
import autokey as a
import playfair as p


def main():
    # checks if command line arguments provided are valid
    if len(sys.argv) != 3:
        sys.exit(
            "Invalid command line arguments.\nUsage: python main.py (encrypt/decrypt) (type of cipher)"
        )

    function = sys.argv[1].lower().strip()
    cipher = sys.argv[2].lower().strip()

    if function not in ["encrypt", "decrypt"]:
        sys.exit(
            "Invalid function, please choose one of the following (encrypt/decrypt).\nUsage: python main.py (encrypt/decrypt) (type of cipher)"
        )

    if cipher not in ["caesar", "vigenere", "railfence", "autokey", "playfair"]:
        sys.exit(
            "Invalid Cipher, please choose one of the following (caesar, vigenere, railfence, autokey, playfair).\nUsage: python main.py (encrypt/decrypt) (type of cipher)"
        )

    # runs appropriate cipher file according to chosen cipher
    if cipher == "caesar":
        output = c.caesar(function)
        # type comparison to know how many values we will output
        if type(output) is str:
            print(f"Output: {output}")
        # if key is also outputted, print both
        elif type(output) is tuple:
            print(f"Output: {output[0]}")
            print(f"Generated Key: {output[1]}")

    elif cipher == "vigenere":
        output = v.vigenere(function)
        # type comparison to know how many values we will output
        if type(output) is str:
            print(f"Output: {output}")
        # if key is also outputted, print both
        elif type(output) is tuple:
            print(f"Output: {output[0]}")
            print(f"Generated Key: {output[1]}")

    elif cipher == "railfence":
        output = r.railfence(function)
        # type comparison to know how many values we will output
        if type(output) is str:
            print(f"Output: {output}")
        # if key is also outputted, print both
        elif type(output) is tuple:
            print(f"Output: {output[0]}")
            print(f"Generated Key: {output[1]}")

    elif cipher == "autokey":
        output = a.autokey(function)
        # type comparison to know how many values we will output
        if type(output) is str:
            print(f"Output: {output}")
        # if key is also outputted, print both
        elif type(output) is tuple:
            print(f"Output: {output[0]}")
            print(f"Generated Key: {output[1]}")

    elif cipher == "playfair":
        output = p.playfair(function)
        # type comparison to know how many values we will output
        if type(output) is str:
            print(f"Output: {output}")
        # if key is also outputted, print both
        elif type(output) is tuple:
            print(f"Output: {output[0]}")
            print(f"Generated Key: {output[1]}")



if __name__ == "__main__":
    main()
