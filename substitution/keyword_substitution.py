import string

alphabet = list(string.ascii_uppercase)

def get_cipher_alphabet(keyword):
    alpha_copy = alphabet.copy()
    keyword_arr = list(keyword)

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

class keyword_substitution_encode():
    """
    Takes in a keyword to shuffle the alphabet and encodes the plaintext based on the ciphered alphabet.

    :param keyword: The keyword used to shuffle the alphabet.
    :type keyword: str
    :param plaintext: The plaintext to be encoded.
    :type plaintext: str
    :return: None. Use self.ciphertext to access the encoded plaintext.
    :rtype: None
    """

    def __init__(self, keyword, plaintext):
        self.keyword = keyword.upper()
        self.plaintext = plaintext.upper()
        self.cipher_alphabet = get_cipher_alphabet(self.keyword)
        self.ciphertext = self.encode()

    # returns ciphertext that gets held in self.ciphertext
    def encode(self):
        text_arr = list(self.plaintext)

        # match plaintext with ciphertext
        for x in range(len(text_arr)):
            char = text_arr[x]
            if char in alphabet: # leave punctuation alone
                plaintext_index = alphabet.index(char)
                text_arr[x] = self.cipher_alphabet[plaintext_index]

        return "".join(text_arr)

class keyword_substitution_decode():
    """
    Takes in a keyword to shuffle the alphabet and decodes the ciphertext based on the ciphered alphabet. This is the
    inverse to keyword_substitution_encode.

    :param keyword: The keyword used to shuffle the alphabet.
    :type keyword: str
    :param ciphertext: The ciphertext to be decoded.
    :type ciphertext: str
    :return: None. Use self.plaintext to access the decoded ciphertext.
    :rtype: None
    """

    def __init__(self, keyword, ciphertext):
        self.keyword = keyword.upper()
        self.ciphertext = ciphertext.upper()
        self.cipher_alphabet = get_cipher_alphabet(self.keyword)
        self.plaintext = self.decode()

    def decode(self):
        text_arr = list(self.ciphertext)

        # match ciphertext with plaintext
        for x in range(len(text_arr)):
            char = text_arr[x]
            if char in alphabet: # leave punctuation alone
                ciphertext_index = self.cipher_alphabet.index(char)
                text_arr[x] = alphabet[ciphertext_index]

        return "".join(text_arr)



if __name__ == "__main__":
    encode = keyword_substitution_encode("ciphercipher", "hello world")
    print(encode.cipher_alphabet)
    print(encode.ciphertext)

    decode = keyword_substitution_decode("ciphercipher", "BEJJM WMQJH")
    print(decode.plaintext)