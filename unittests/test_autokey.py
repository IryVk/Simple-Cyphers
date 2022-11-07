import filecmp

from autokey import encrypt
from autokey import decrypt


def test_encrypt():
    # test encrypting alphabet
    assert encrypt("Arwa", "BG") == "$ZYt"
    # test encrypting numbers
    assert encrypt("Arwa is 18 years old", "OnOl") == """1"gna|,"QB4:7:3.&q x"""
    # test encrypting special characters
    assert encrypt("Arwa's email is: {aa2101585@tkh.edu.eg}//..", "UhUjj") == r"""7{ml2U3}o)}-&wuD-<kulQL37jfpFAAcFy"74m#E]46"""


def test_decrypt():
    # test decrypting alphabet
    assert decrypt("$ZYt", "BG") == "Arwa"
    # test decrypting numbers
    assert decrypt("""1"gna|,"QB4:7:3.&q x""", "OnOl") == "Arwa is 18 years old"
    # test decrypting special characters
    assert decrypt( r"""7{ml2U3}o)}-&wuD-<kulQL37jfpFAAcFy"74m#E]46""", "UhUjj") == "Arwa's email is: {aa2101585@tkh.edu.eg}//.."


def test_files():
    # test if file decrypted from the encrypted file is the same as the original file
    assert filecmp.cmp("arwa.txt", "testfiles/de_auto_arwa.txt", shallow=False)


# using pytest, all tests passed