from railfence import encrypt
from railfence import decrypt


def test_encrypt():
    # test encrypting alphabet
    assert encrypt("Arwa", 3) == "Araw"
    # test encrypting numbers
    assert encrypt("Arwa is 18 years old", 5) == "A1 r 8sows rlaiyad e" 
    # test encrypting special characters
    assert encrypt("Arwa's email is: {aa2101585@tkh.edu.eg}//..", 8) == "Ast.ri:@k.w  5h/al{8./'ia5e}saa1dg m20uee1."


def test_decrypt():
    # test decrypting alphabet
    assert decrypt("Araw", 3) == "Arwa"
    # test decrypting numbers
    assert decrypt("A1 r 8sows rlaiyad e", 5) == "Arwa is 18 years old"
    # test decrypting special characters
    assert decrypt("Ast.ri:@k.w  5h/al{8./'ia5e}saa1dg m20uee1.", 8) == "Arwa's email is: {aa2101585@tkh.edu.eg}//.."


# using pytest, all tests passed