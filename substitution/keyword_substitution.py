import string

class keyword_substitution_encode():
    alphabet = list(string.ascii_uppercase)

    def __init__(self, keyword, plaintext):
        self.keyword = keyword.upper()
        self.plaintext = plaintext.upper()
        self.cipher_alphabet = self.get_cipher_alphabet()
        self.ciphertext = self.encode

    def get_cipher_alphabet(self):
        alpha_copy = self.alphabet.copy()
        keyword_arr = list(self.keyword)

        # remove chars in keyword
        for x in range(len(self.keyword)):
            if keyword_arr[x] in alpha_copy:
                alpha_copy.remove(keyword_arr[x])

        # add keyword alphabet to clean array
        temp_arr = keyword_arr + alpha_copy
        cipher_alphabet = []
        for x in range(len(temp_arr)):
            # check for duplicates
            if temp_arr[x] not in cipher_alphabet:
                # check for punctuation chars
                if temp_arr[x] in self.alphabet:
                    cipher_alphabet.append(temp_arr[x])

        return cipher_alphabet

    def encode(self):
        pass

if __name__ == "__main__":
    encode = keyword_substitution_encode("ciphercipher", "hello world")
    print(encode.cipher_alphabet)