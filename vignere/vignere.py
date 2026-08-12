import string
from tableau import tableau

alphabet = list(string.ascii_uppercase)

# holy shit there is an algorithm for this (of course there is)
# TODO: hold my beer (decaf coffee)
def get_keyword_arr(keyword, text):
    """
    Helper method to create the string of repeating keywords in the punctuation of the plaintext.

    :param keyword: The keyword to added to the arr
    :param text: The plaintext that serves as the basis for the array (for punctuation purposes)
    :return: the desired array
    :rtype: str list
    """
    keyword_arr = list(text)

    for index in range(len(keyword_arr)):
        # maintain punctuation
        if keyword_arr[index] in alphabet:
            keyword_index = index % len(keyword)
            keyword_arr[index] = keyword[keyword_index]

    return keyword_arr

class vignere_basic_encode():
    """
    This class takes in a plaintext and keyword and uses a standard Vignere tableau to encode it. The __init__ function
    automatically creates and fills the paramaters to be accessed as needed.

    :param plaintext: The plaintext to be encoded
    :type plaintext: str
    :param keyword: The keyword to encode with
    :type keyword: str
    :returns: None
    :rtype: None
    """

    tableau = tableau()

    def __init__(self, plaintext, keyword):
        self.plaintext = plaintext.upper()
        self.keyword = keyword.upper()
        self.basic_tableau = self.tableau.tableau
        self.keyword_arr = get_keyword_arr(self.keyword, self.plaintext)
        self.ciphertext = self.encode()


    def encode(self):
        text_arr = self.keyword_arr.copy()

        for index in range(len(self.keyword_arr)):
            keyletter = self.keyword_arr[index]
            plainletter = self.plaintext[index]

            if keyletter in alphabet: # preserve punctuation

                # get cipher alphabet
                keyletter_index = alphabet.index(keyletter) # to match to vignere tableau, since the first col is alphabetical
                cipher_alphabet = self.basic_tableau[keyletter_index]

                # encode letter
                plainletter_index = alphabet.index(plainletter)
                text_arr[index] = cipher_alphabet[plainletter_index]

        return "".join(text_arr)

class vignere_basic_decode():
    """
    This class takes in a ciphertext and keyword and uses a standard Vignere tableau to decode it. The __init__ function
    automatically creates and fills the paramaters to be accessed as needed. This is the inverse of the vignere_basic_encode class.

    :param ciphertext: The ciphertext to be encoded
    :type ciphertext: str
    :param keyword: The keyword to decode with
    :type keyword: str
    :returns: None
    :rtype: None
    """
    tableau = tableau()

    def __init__(self, ciphertext, keyword):
        self.ciphertext = ciphertext.upper()
        self.keyword = keyword.upper()
        self.basic_tableau = self.tableau.tableau
        self.keyword_arr = get_keyword_arr(self.keyword, self.ciphertext)
        self.plaintext = self.decode()

    def decode(self):
        text_arr = self.keyword_arr.copy()

        for index in range(len(self.keyword_arr)):
            keyletter = self.keyword_arr[index]
            cipherletter = self.ciphertext[index]

            if keyletter in alphabet: # preserve punctuation

                # get cipher alphabet
                keyletter_index = alphabet.index(keyletter) # to match to vignere tableau, since the first col is alphabetical
                cipher_alphabet = self.basic_tableau[keyletter_index]

                # decode
                cipherletter_index = cipher_alphabet.index(cipherletter)
                text_arr[index] = alphabet[cipherletter_index]
        return "".join(text_arr)

class vignere_autokey_decode():
    pass


if __name__ == "__main__":
    t = tableau("ciphertext")
    print(t)

    encode = vignere_basic_encode("hello world!", "cipher")
    print(encode.ciphertext)

    decode = vignere_basic_decode("JMASS YWGSH!", "cipher")
    print(decode.plaintext)
