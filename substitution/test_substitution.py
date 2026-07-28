from _pytest import unittest
from substitution import substitution_encode, substitution_decode

class test_substitution_encode(unittest.TestCase):
    plaintext = "hello world!"

    def test_ROT13(self):
        # ROT13 encoded on itself returns the plaintext
        encode = substitution_encode(13, self.plaintext)
        encode_again = substitution_encode(13, encode.ciphertext)
        assert encode.plaintext == encode_again.ciphertext

    def test_shift_26(self):
        encode = substitution_encode(26, self.plaintext)
        assert encode.plaintext == encode.ciphertext

    def test_shift_0(self):
        encode = substitution_encode(0, self.plaintext)
        assert encode.plaintext == encode.ciphertext

    def test_caesar(self):
        expected_ciphertext = "KHOOR ZRUOG!"
        encode = substitution_encode(3, self.plaintext)
        assert encode.ciphertext == expected_ciphertext

    def test_negative_num(self):
        expected_ciphertext = "VSZZC KCFZR!" # same as shifting +16
        encode = substitution_encode(-12, self.plaintext)
        assert encode.ciphertext == expected_ciphertext

    def test_more_than_26(self):
        expected_ciphertext = "XUBBE MEHBT!"
        encode = substitution_encode(42, self.plaintext)
        assert encode.ciphertext == expected_ciphertext

class test_substitution_decode(unittest.TestCase):
    expected_plaintext = "HELLO WORLD!" # uppercase this one so i don't have to do it later

    # with the first three, they all just return the plaintext, so no need to create ciphertext
    def test_ROT13(self):
        # ROT13 decoded on itself returns the plaintext
        decode = substitution_decode(13, self.expected_plaintext)
        decode_again = substitution_encode(13, decode.ciphertext)
        assert decode.ciphertext == decode_again.plaintext

    def test_shift_26(self):
        decode = substitution_decode(26, self.expected_plaintext)
        assert decode.ciphertext == decode.plaintext

    def test_shift_0(self):
        decode = substitution_decode(0, self.expected_plaintext)
        assert decode.ciphertext == decode.plaintext

    def test_caesar(self):
        ciphertext = "KHOOR ZRUOG!"
        decode = substitution_decode(3, ciphertext)
        assert decode.plaintext == self.expected_plaintext

    def test_negative_num(self):
        ciphertext = "YVCCF NFICU!"
        decode = substitution_decode(-9, ciphertext)
        assert decode.plaintext == self.expected_plaintext

    def test_more_than_26(self):
        ciphertext = "AXEEH PHKEW!"
        decode = substitution_decode(97, ciphertext)
        assert decode.plaintext == self.expected_plaintext


