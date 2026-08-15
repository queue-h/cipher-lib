import string

alphabet = list(string.ascii_uppercase)

def get_cipher_alphabet(keyword):
    """
    This will return a shuffled alphabet to encode and decode from. Non-alpha and duplicated characters are eliminated,
    and everything is converted and returned in uppercase. For example: get_cipher_alphabet('foobar') will
    return ['F', 'O', 'B', 'A', 'R', 'C', 'D', 'E', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    :param keyword: The keyword used to shuffle the alphabet.
    :type keyword: str
    :return: Shuffled alphabet.
    :rtype: list
    """
    alpha_copy = alphabet.copy()
    keyword_arr = list(keyword.upper())

    # remove chars in keyword
    for x in range(len(keyword)):
        if keyword_arr[x] in alpha_copy:
            alpha_copy.remove(keyword_arr[x])

    # add keyword alphabet to clean array
    temp_arr = keyword_arr + alpha_copy
    cipher_alphabet = []
    for x in range(len(temp_arr)):
        # check for duplicates
        if temp_arr[x] not in cipher_alphabet:
            # check for punctuation chars
            if temp_arr[x] in alphabet:
                cipher_alphabet.append(temp_arr[x])

    return cipher_alphabet

class Substitution:
    """
    Encodes plaintext in a Caesar cipher with a custom shift. Default is 3.

    :param message: The text to be encoded or decoded.
    :type message: str
    :param shift: The amount to shift the cipher alphabet. Optional; default is value is three.
    :type shift: int
    :param keyword: The keyword with which to scramble the message. Optional; default is value is "".
    :type keyword: str
    """

    def __init__(self, message, shift = 3, keyword = ""):
        self.message = message.upper()
        self.shift = shift
        self.keyword = keyword.upper()

        # get_cipher_alphabet("") will return the basic alphabet, but this saves some time
        if self.keyword != "":
            self.alphabet = get_cipher_alphabet(self.keyword)
        else:
            self.alphabet = alphabet

    def encode(self):
        """
        Uses self.shift to encode self.message using a slding substitution cipher. Default is three.
        This is the inverse of self.decode().

        :returns: The encoded message
        :rtype: str
        """
        text_arr = list(self.message)
        for x in range(len(text_arr)):
            # if it's a punctuation mark, ignore
            if text_arr[x] in self.alphabet:
                plaintext_index = self.alphabet.index(text_arr[x])
                ciphertext_index = (plaintext_index + self.shift) % len(self.alphabet)
                text_arr[x] = self.alphabet[ciphertext_index]
        return ''.join(text_arr)

    def decode(self):
        """
        Uses self.shift to decode self.message using a slding substitution cipher. Default is three.
        This is the inverse of self.encode().

        :returns: The decoded message
        :rtype: str
        """
        text_arr = list(self.message)
        for x in range(len(text_arr)):
            # if it's a punctuation mark, ignore
            if text_arr[x] in self.alphabet:
                ciphertext_index = self.alphabet.index(text_arr[x])
                plaintext_index = (ciphertext_index - self.shift) % len(self.alphabet)
                text_arr[x] = self.alphabet[plaintext_index]
        return ''.join(text_arr)


if __name__ == '__main__':
    s = Substitution("as an example", 11, "cipher")
    print(s.encode())
