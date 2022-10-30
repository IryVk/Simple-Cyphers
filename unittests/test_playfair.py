from playfair import encrypt
from playfair import decrypt
from playfair import generatekey
from playfair import split


def test_encrypt():
    # test encrypting alphabet
    assert encrypt(split("Arwa"), generatekey("bg")) == "gsxg"


def test_decrypt():
    # test decrypting alphabet
    assert decrypt(split("gsxg"), generatekey("bg")) == "arwa"


# using pytest, all tests passed