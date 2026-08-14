import string
from tableau import tableau

alphabet = list(string.ascii_uppercase)

# holy shit there is an algorithm for this (of course there is)
# TODO: hold my beer (decaf coffee)
def get_keyword_arr(message, keyword):
    """
    Helper method to create the string of repeating keywords in the punctuation of the plaintext.

    :param message: The plaintext that serves as the basis for the array (for punctuation purposes)
    :param keyword: The keyword to added to the arr
    :return: the desired array
    :rtype: str list
    """
    keyword_arr = []

    keyword_index = 0 # to iterate over the keyword
    for letter in message:
        # maintain punctuation
        if letter in alphabet:
            keyword_letter = keyword[keyword_index % len(keyword)]
        else:
            keyword_letter = letter # add punctuation
            keyword_index -= 1 # do not move forward in keyword
        keyword_index += 1
        keyword_arr.append(keyword_letter)

    return keyword_arr

class vignere_basic():
    """
    This class takes in a plaintext and keyword and uses a standard Vignere tableau to encode it. The __init__ function
    automatically creates and fills the paramaters to be accessed as needed.

    :param plaintext: The plaintext to be encoded
    :type plaintext: str
    :param keyword: The keyword to encode with
    :type keyword: str
    """
    tableau = tableau()

    def __init__(self, message, keyword):
        self.message = message.upper()
        self.keyword = keyword.upper()

    def encode(self):
        ciphertext = []
        key_arr = get_keyword_arr(self.message, self.keyword) # array to be mutated

        # iterates over every letter that needs to be encrypted
        for index in range(len(key_arr)):
            plainletter = self.message[index]  # letter to be encoded
            keyletter = key_arr[index] # keyword letter to shift by

            if plainletter in alphabet: # preserve punctuation
                # shift plainletter by the keyletter, mod, and then convert integer back to char
                encoded_letter = alphabet[(alphabet.index(plainletter) + alphabet.index(keyletter)) % len(alphabet)]
            else:
                # add punctation
                encoded_letter = plainletter
            ciphertext.append(encoded_letter)

        return "".join(ciphertext)

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
    vignere = vignere_basic("the the is a message", "key")
    print(vignere.encode())