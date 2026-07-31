import string
from _pytest import unittest
from sliding_substitution import sliding_substitution_encode, sliding_substitution_decode
from keyword_substitution import keyword_substitution_decode, keyword_substitution_encode

class test_slding_substitution_encode(unittest.TestCase):
    plaintext = "hello world!"

    def test_ROT13(self):
        # ROT13 encoded on itself returns the plaintext
        encode = sliding_substitution_encode(13, self.plaintext)
        encode_again = sliding_substitution_encode(13, encode.ciphertext)
        assert encode.plaintext == encode_again.ciphertext

    def test_shift_26(self):
        encode = sliding_substitution_encode(26, self.plaintext)
        assert encode.plaintext == encode.ciphertext

    def test_shift_0(self):
        encode = sliding_substitution_encode(0, self.plaintext)
        assert encode.plaintext == encode.ciphertext

    def test_caesar(self):
        expected_ciphertext = "KHOOR ZRUOG!"
        encode = sliding_substitution_encode(3, self.plaintext)
        assert encode.ciphertext == expected_ciphertext

    def test_negative_num(self):
        expected_ciphertext = "VSZZC KCFZR!" # same as shifting +16
        encode = sliding_substitution_encode(-12, self.plaintext)
        assert encode.ciphertext == expected_ciphertext

    def test_more_than_26(self):
        expected_ciphertext = "XUBBE MEHBT!"
        encode = sliding_substitution_encode(42, self.plaintext)
        assert encode.ciphertext == expected_ciphertext

class test_sliding_substitution_decode(unittest.TestCase):
    expected_plaintext = "HELLO WORLD!" # uppercase this one so i don't have to do it later

    # with the first three, they all just return the plaintext, so no need to create ciphertext
    def test_ROT13(self):
        # ROT13 decoded on itself returns the plaintext
        decode = sliding_substitution_decode(13, self.expected_plaintext)
        decode_again = sliding_substitution_encode(13, decode.ciphertext)
        assert decode.ciphertext == decode_again.plaintext

    def test_shift_26(self):
        decode = sliding_substitution_decode(26, self.expected_plaintext)
        assert decode.ciphertext == decode.plaintext

    def test_shift_0(self):
        decode = sliding_substitution_decode(0, self.expected_plaintext)
        assert decode.ciphertext == decode.plaintext

    def test_caesar(self):
        ciphertext = "KHOOR ZRUOG!"
        decode = sliding_substitution_decode(3, ciphertext)
        assert decode.plaintext == self.expected_plaintext

    def test_negative_num(self):
        ciphertext = "YVCCF NFICU!"
        decode = sliding_substitution_decode(-9, ciphertext)
        assert decode.plaintext == self.expected_plaintext

    def test_more_than_26(self):
        ciphertext = "AXEEH PHKEW!"
        decode = sliding_substitution_decode(97, ciphertext)
        assert decode.plaintext == self.expected_plaintext

class test_keyword_substitution_encode(unittest.TestCase):
    plaintext = "hello world!"
    keyword = "cipher"

    def test_cipher_alphabet(self):
        expected_alphabet = ['C', 'I', 'P', 'H', 'E', 'R', 'A', 'B', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        encode = keyword_substitution_encode(self.keyword, self.plaintext)
        assert encode.cipher_alphabet == expected_alphabet

    def test_cipher_alphabet_duplicates(self):
        expected_alphabet = ['C', 'I', 'P', 'H', 'E', 'R', 'A', 'B', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        encode = keyword_substitution_encode(self.keyword + self.keyword, self.plaintext) # use keyword twice for duplicates bc why not
        assert encode.cipher_alphabet == expected_alphabet

    def test_cipher_alphabet_none(self):
        expected_alphabet = list(string.ascii_uppercase)
        encode = keyword_substitution_encode("", self.plaintext)
        assert encode.cipher_alphabet == expected_alphabet

    def test_encode(self):
        expected_ciphertext = "BEJJM WMQJH!"
        encode = keyword_substitution_encode(self.keyword, self.plaintext)
        assert encode.ciphertext == expected_ciphertext

class test_keyword_substitution_decode(unittest.TestCase):
    pass
