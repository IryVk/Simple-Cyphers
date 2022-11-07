import filecmp

from vigenere import encrypt
from vigenere import decrypt


def test_encrypt():
    # test encrypting alphabet
    assert encrypt("Arwa", "BGhi") == "$Z!k"
    # test encrypting numbers
    assert encrypt("Arwa is 18 years old", "OnOl") == r"""1"gnoxc-!Go'Upb!o~\q"""
    # test encrypting special characters
    assert encrypt("Arwa's email is: {aa2101585@tkh.edu.eg}//..", "UhUjj") == "7{ml2i)[xl_uut~0)qll(:&<@.>6 v^7[o!$n]):%7$"


def test_decrypt():
    # test decrypting alphabet
    assert decrypt("$Z!k", "BGhi") == "Arwa"
    # test decrypting numbers
    assert decrypt(r"""1"gnoxc-!Go'Upb!o~\q""", "OnOl") == "Arwa is 18 years old"
    # test decrypting special characters
    assert decrypt("7{ml2i)[xl_uut~0)qll(:&<@.>6 v^7[o!$n]):%7$", "UhUjj") == "Arwa's email is: {aa2101585@tkh.edu.eg}//.."


def test_files():
    # test if file decrypted from the encrypted file is the same as the original file
    assert filecmp.cmp("arwa.txt", "testfiles/de_vig_arwa.txt", shallow=False)

# using pytest, all tests passed