import string
from tableau import tableau

alphabet = list(string.ascii_uppercase)


def get_keyword_arr(keyword, text):
    keyword_arr = list(text)

    for index in range(len(keyword_arr)):
        # maintain punctuation
        if keyword_arr[index] in alphabet:
            keyword_index = index % len(keyword)
            keyword_arr[index] = keyword[keyword_index]

    return keyword_arr

class vignere_basic_encode():

    tableau = tableau()

    def __init__(self, plaintext, keyword):

        self.plaintext = plaintext.upper()
        self.keyword = keyword.upper()
        self.basic_tableau = self.tableau.basic_tableau
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
    tableau = tableau()

    def __init__(self, ciphertext, keyword):
        self.ciphertext = ciphertext.upper()
        self.keyword = keyword.upper()
        self.basic_tableau = self.tableau.basic_tableau
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



if __name__ == "__main__":
    print(vignere_basic_encode.tableau)

    encode = vignere_basic_encode("hello world!", "abc")
    print(encode.ciphertext)

    decode = vignere_basic_decode("HFNLP WPTLE!", "abc")
    print(decode.plaintext)
