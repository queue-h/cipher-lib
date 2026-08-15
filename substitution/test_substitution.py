import string
from _pytest import unittest
from substitution import Substitution
from substitution import get_cipher_alphabet


class TestSlidingSubstitutionEncode(unittest.TestCase):
    plaintext = "hello world!"

    def test_ROT13(self):
        # ROT13 encoded on itself returns the plaintext
        s = Substitution(self.plaintext, 13)
        encoded_message = s.encode()
        encode_again = Substitution(encoded_message, 13)
        assert s.message == encode_again.encode()

    def test_shift_26(self):
        s = Substitution(self.plaintext, 26)
        assert s.message == s.encode()

    def test_shift_0(self):
        s = Substitution(self.plaintext, 0)
        assert s.message == s.encode()

    def test_caesar(self):
        expected_ciphertext = "KHOOR ZRUOG!"
        s = Substitution(self.plaintext)
        assert s.encode() == expected_ciphertext

    def test_negative_num(self):
        expected_ciphertext = "VSZZC KCFZR!" # same as shifting +16
        s = Substitution(self.plaintext, -12)
        assert s.encode() == expected_ciphertext

    def test_more_than_26(self):
        expected_ciphertext = "XUBBE MEHBT!"
        s = Substitution(self.plaintext, 42)
        assert s.encode() == expected_ciphertext

class TestSlidingSubstitutionDecode(unittest.TestCase):
    expected_plaintext = "HELLO WORLD!" # uppercase this time so i don't have to do it later

    # with the first three, they all just return the plaintext, so no need to create ciphertext
    def test_ROT13(self):
        # ROT13 decoded on itself returns the plaintext
        s = Substitution(self.expected_plaintext, 13)
        decoded_message = s.decode()
        decode_again = Substitution(decoded_message, 13)
        assert s.message == decode_again.decode()

    def test_shift_26(self):
        s = Substitution(self.expected_plaintext, 26)
        assert s.decode() == s.message

    def test_shift_0(self):
        s = Substitution(self.expected_plaintext, 0)
        assert s.decode() == s.message

    def test_caesar(self):
        ciphertext = "KHOOR ZRUOG!"
        s = Substitution(ciphertext)
        assert s.decode() == self.expected_plaintext

    def test_negative_num(self):
        ciphertext = "YVCCF NFICU!"
        s = Substitution(ciphertext, -9)
        assert s.decode() == self.expected_plaintext

    def test_more_than_26(self):
        ciphertext = "AXEEH PHKEW!"
        s = Substitution(ciphertext, 97)
        assert s.decode() == self.expected_plaintext

class TestKeywordSubstitutionAlphabet(unittest.TestCase):
    keyword = "cipher"
    expected_alphabet = ['C', 'I', 'P', 'H', 'E', 'R', 'A', 'B', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    def test_cipher_alphabet(self):
        generated_alphabet = get_cipher_alphabet(self.keyword)
        assert generated_alphabet == self.expected_alphabet

    def test_cipher_alphabet_duplicates(self):
        generated_alphabet = get_cipher_alphabet(self.keyword + self.keyword)  # use keyword twice for duplicates bc why not
        assert generated_alphabet == self.expected_alphabet

    def test_cipher_alphabet_special_chars(self):
        keyword = "C1i*\\7 \p'h~2er30."
        generated_alphabet = get_cipher_alphabet(keyword)
        assert generated_alphabet == self.expected_alphabet

    def test_cipher_alphabet_none(self):
        expected_alphabet = list(string.ascii_uppercase)
        generated_alphabet = get_cipher_alphabet("")
        assert generated_alphabet == expected_alphabet

class TestKeywordSubstitutionEncode(unittest.TestCase):
    plaintext = "hello world!"
    keyword = "cipher"
    expected_ciphertext = "ABOOT ZTDOJ!"

    def test_encode(self):
        s = Substitution(self.plaintext, 3, self.keyword)
        assert s.encode() == self.expected_ciphertext

class TestKeywordSubstitutionDecode(unittest.TestCase):
    keyword = "cipher"
    ciphertext = "ABOOT ZTDOJ!"
    expected_plaintext = "HELLO WORLD!"

    def test_decode(self):
        s = Substitution(self.ciphertext, 3, self.keyword)
        assert s.decode() == self.expected_plaintext

