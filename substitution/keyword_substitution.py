import string

class keyword_substitution_encode():
    alphabet = list(string.ascii_uppercase)

    def __init__(self, keyword, plaintext):
        self.keyword = keyword.upper()
        self.plaintext = plaintext.upper()
        self.cipher_alphabet = self.get_cipher_alphabet()
        self.ciphertext = self.encode()

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

    # returns ciphertext that gets held in self.ciphertext
    def encode(self):
        plaintext_arr = list(self.plaintext)
        ciphertext = ""

        # match plaintext with ciphertext
        for x in range(len(plaintext_arr)):
            char = plaintext_arr[x]
            if char in self.alphabet:
                plaintext_index = self.alphabet.index(char)
                plaintext_arr[x] = self.cipher_alphabet[plaintext_index]

        return "".join(plaintext_arr)

class keyword_substitution_decode():
    alphabet = list(string.ascii_uppercase)


if __name__ == "__main__":
    encode = keyword_substitution_encode("ciphercipher", "hello world")
    print(encode.cipher_alphabet)
    print(encode.ciphertext)