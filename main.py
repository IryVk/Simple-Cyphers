import sys
import caesar as c
import vigenere as v
import railfence as r
import autokey as a
import playfair as p


def main():
    #checks if command line arguments provided are valid
    if len(sys.argv) != 3:
        print("""Invalid command line arguments.
        Usage: python main.py (encrypt/decrypt) (type of cipher)""")
        return 1
        
    function = sys.argv[1].lower().strip()
    cipher = sys.argv[2].lower().strip()
    
    if function not in ["encrypt", "decrypt"]:
        print("""Invalid function, please choose one of the following (encrypt/decrypt).
        Usage: python main.py (encrypt/decrypt) (type of cipher)""")
        return 1
        
    if cipher not in ["caesar", "vigenere", "railfence", "autokey", "playfair"]:
        print("""Invalid Cipher, please choose one of the following (caesar, vigenere, railfence, autokey, playfair).
        Usage: python main.py (encrypt/decrypt) (type of cipher)""")
        return 1

    #runs appropriate cipher file according to chosen cipher
    if cipher == "caesar":
        c.caesar(function)

    elif cipher == "vigenere":
        v.vigenere(function)
    
    elif cipher == "railfence":
        r.railfence(function)

    elif cipher == "autokey":
        a.autokey(function)

    elif cipher == "playfair":
        p.playfair(function)


if __name__ == "__main__":
    main()

    

