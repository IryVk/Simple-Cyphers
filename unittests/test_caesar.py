from caesar import encrypt
from caesar import decrypt


def test_encrypt():
    # test encrypting alphabet
    assert encrypt("Arwa", 4) == "Ev{e"
    # test encrypting numbers
    assert encrypt("Arwa is 18 years old", 5) == "Fw|f%nx%6=%~jfwx%tqi" 
    # test encrypting special characters
    assert encrypt("Arwa's email is: {aa2101585@tkh.edu.eg}//..", 8) == "Iz i/{(muiqt(q{B($ii:989=@=H|sp6ml}6mo&7766"


def test_decrypt():
    # test decrypting alphabet
    assert decrypt("Ev{e", 4) == "Arwa"
    # test decrypting numbers
    assert decrypt("Fw|f%nx%6=%~jfwx%tqi", 5) == "Arwa is 18 years old"
    # test decrypting special characters
    assert decrypt("Iz i/{(muiqt(q{B($ii:989=@=H|sp6ml}6mo&7766", 8) == "Arwa's email is: {aa2101585@tkh.edu.eg}//.."


# using pytest, all tests passed
