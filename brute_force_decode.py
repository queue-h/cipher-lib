from substitution.sliding_substitution import sliding_substitution_decode
from substitution.keyword_substitution import keyword_substitution_decode

class brute_force_decode:
    ciphertext = "TL TG XQTFIEX"

    def brute_force_sliding(self):
        for x in range(1, 26): # don't need to actually go to 26
            decode = sliding_substitution_decode(x, self.ciphertext)
            print(decode.plaintext)

    # keyword is a little trickier, many more options
    def brute_force_keyword(self, keyword_list):
        for keyword in keyword_list:
            decode = keyword_substitution_decode(keyword, self.ciphertext)
            print(decode.plaintext)



if __name__ == "__main__":
    b = brute_force_decode()
    b.brute_force_sliding()