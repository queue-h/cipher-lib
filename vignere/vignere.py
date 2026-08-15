from substitution.keyword_substitution import get_cipher_alphabet
import string

def get_keyword_arr(message, keyword, alphabet):
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

class Vignere:
    """
    This class takes in a message and a keyword and uses a standard Vignere tableau to encode and decode it.
    Everything is returned in uppercase, punctuation and special characters are retained.

    :param message: The text to be encoded and decoded (case-insensitive)
    :type message: str
    :param keyword: The keyword to encode and decode with (case-insensitive)
    :type keyword: str
    :param alphabet_shuffle: An optional keyword to shuffle the alphabet using subsitution.keyword_substitution.get_cipher_alphabet(). Defaults to "".
    :type alphabet_shuffle: str
    """

    def __init__(self, message, keyword, alphabet_shuffle = ""):
        self.message = message.upper()
        self.keyword = keyword.upper()

        self.alphabet = list(string.ascii_uppercase)
        # get_cipher_alphabet will still work with an empty keyword, but for effiency:
        if alphabet_shuffle.upper() != "":
            self.alphabet = get_cipher_alphabet(alphabet_shuffle.upper())

        self.key_arr = get_keyword_arr(self.message, self.keyword, self.alphabet)


    def encode(self):
        """
        Uses self.keyword to encode self.message using the basic Vignere tableau.
        Convert alphabet to integer indexes, then E\\ :sub:`i` \\ = (P\\ :sub:`i` \\ + K\\ :sub:`i` \\) mod 26.
        This is the inverse of self.decode().

        :returns: The encoded message
        :rtype: str
        """
        ciphertext = []

        # iterates over every letter that needs to be encrypted
        for index in range(len(self.message)):
            plainletter = self.message[index]  # letter to be encoded
            keyletter = self.key_arr[index] # keyword letter to shift by

            if plainletter in self.alphabet: # preserve punctuation
                # shift plainletter by the keyletter, mod, and then convert integer back to char
                encoded_letter = self.alphabet[(self.alphabet.index(plainletter) + self.alphabet.index(keyletter)) % len(self.alphabet)]
            else: # add punctation
                encoded_letter = plainletter
            ciphertext.append(encoded_letter)

        return "".join(ciphertext)

    def decode(self):
        """
        Uses self.keyword to decode self.message using the basic Vignere tableau.
        Convert alphabet to integer indexes, then E\\ :sub:`i` \\ = (P\\ :sub:`i` \\ - K\\ :sub:`i` \\) mod 26.
        This is the inverse of self.encode().

        :returns: The decoded message
        :rtype: str
        """
        plaintext = []

        # iterate over every letter that need to be decrypted
        for index in range(len(self.message)):
            cipherletter = self.message[index] # letter to be decoded
            keyletter = self.key_arr[index] # keyword letter to shift by

            if cipherletter in self.alphabet: # preserver punctuation
                # shift cipherletter by keyletter (subtract instead of add), mod, and then convert interger back to char
                decoded_letter = self.alphabet[(self.alphabet.index(cipherletter) - self.alphabet.index(keyletter)) % len(self.alphabet)]
            else: # add punctuation
                decoded_letter = cipherletter
            plaintext.append(decoded_letter)

        return "".join(plaintext)

# TODO: write this
class VignereAutokey:
    pass


if __name__ == "__main__":
    print(Vignere("this is a message!", "key").encode())
    print(Vignere("DLGC MQ K .QCCWYQI", "key").decode())
    print(Vignere("this is a message!", "key", "cipher").encode())
