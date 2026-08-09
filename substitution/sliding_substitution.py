import string

class sliding_substitution_encode():
    """
    Encodes plaintext in a Caesar cipher with a custom shift. Default is 3.

    :param plaintext: The plaintext to be encoded.
    :type plaintext: str
    :param shift: The amount to shift the cipher alphabet.
    :type shift: int
    :return: None. Use self.ciphertext to access the encoded plaintext.
    :rtype: None
    """

    alphabet = list(string.ascii_uppercase)

    def __init__(self, plaintext, shift = 3):
        self.shift = shift
        self.plaintext = plaintext.upper()
        self.ciphertext = self.encode()

    def encode(self):
        text_arr = list(self.plaintext)
        for x in range(len(text_arr)):
            # if it's a punctuation mark, ignore
            if text_arr[x] in self.alphabet:
                plaintext_index = self.alphabet.index(text_arr[x])
                ciphertext_index = (plaintext_index + self.shift) % len(self.alphabet)
                text_arr[x] = self.alphabet[ciphertext_index]
        return ''.join(text_arr)

class sliding_substitution_decode():
    """
    Decodes Caesar cipher ciphertext with a custom shift. Default is 3. This is the inverse to sliding_substitution_encode.

    :param ciphertext: The ciphertext to be decoded.
    :type ciphertext: str
    :param shift: The amount to shift the cipher alphabet.
    :type shift: int
    :return: None. Use self.plaintext to access the decoded ciphertext.
    :rtype: None
    """
    alphabet = list(string.ascii_uppercase)

    def __init__(self, ciphertext, shift = 3):
        self.shift = shift
        self.ciphertext = ciphertext.upper()
        self.plaintext = self.decode()

    def decode(self):
        text_arr = list(self.ciphertext)
        for x in range(len(text_arr)):
            # if it's a punctuation mark, ignore
            if text_arr[x] in self.alphabet:
                ciphertext_index = self.alphabet.index(text_arr[x])
                plaintext_index = (ciphertext_index - self.shift) % len(self.alphabet)
                text_arr[x] = self.alphabet[plaintext_index]
        return ''.join(text_arr)


if __name__ == '__main__':
    encode = sliding_substitution_encode(97, "hello world!")
    print(encode.ciphertext)
