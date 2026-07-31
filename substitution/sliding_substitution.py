import string

class sliding_substitution_encode():

    alphabet = list(string.ascii_uppercase)

    def __init__(self, shift, plaintext):
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
    # really best not to think of this as plaintext for this one
    alphabet = list(string.ascii_uppercase)

    def __init__(self, shift, ciphertext):
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
