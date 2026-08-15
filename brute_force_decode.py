from substitution import Substitution

def brute_force_substitution(ciphertext, keyword_list):
    """
    Given a cipher and a list of keywords, iterates through all 26 possible shifts and prints out the results.
    Decoded ciphertexts are also saved to a list for later analysis.

    :param ciphertext:
    :param keyword_list:
    :return: List of decoded ciphertexts
    """
    for keyword in keyword_list:
        decoded_text = []
        for x in range(1, 26): # don't need to actually go to 26
            s = Substitution(ciphertext, x, keyword)
            print(s.decode())
            decoded_text.append(s.decode())
    return decoded_text



if __name__ == "__main__":
    ciphertext = "QH QC NDQZLYN"
    # expected plaintext is "AS AN EXAMPLE"
    b = brute_force_substitution(ciphertext, ["hello", "cipher", ""])