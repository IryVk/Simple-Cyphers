from playfair import encrypt
from playfair import decrypt
from playfair import generatekey
from playfair import split


def test_split():
    # test splitting the input
    assert split("hello") == ["he", "lx", "lo"]


def test_generatekey():
    # test generation of 5x5 grid key
    assert generatekey("bg") == [["b", "g", "a", "c", "d"],
                                 ["e", "f", "h", "i", "k"],
                                 ["l", "m", "n", "o", "p"],
                                 ["q", "r", "s", "t", "u"],
                                 ["v", "w", "x", "y", "z"]]


def test_encrypt():
    # test encrypting alphabet
    assert encrypt(split("Arwa"), generatekey("bg")) == "gsxg"


def test_decrypt():
    # test decrypting alphabet
    assert decrypt(split("gsxg"), generatekey("bg")) == "arwa"


# using pytest, all tests passed