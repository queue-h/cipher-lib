import string
from substitution.keyword_substitution import get_cipher_alphabet

alphabet = string.ascii_uppercase

class tableau():
    """
    This class is used to create a tableau that will be referenced by the Vignere classes. There is an option to pass
    a keyword, but there is not yet a distinction between the keyword to scramble the tableau and the keyword to encode
    and decode text.

    :param keyword: Defaults to "" for a basic tableau.
    :type keyword: str
    :return: None. Use str(self) for pretty printing.
    """

    def __init__(self, keyword = ""):
        self.keyword = keyword.upper()
        self.tableau = self.get_tableau()

    # TODO: Does this work?
    def get_tableau(self):

        # get_cipher_alphabet would still work with a blank keyword, but its faster to check
        cipher_alphabet = alphabet
        if self.keyword != "":
           cipher_alphabet = get_cipher_alphabet(self.keyword)

        tableau = [["" for _ in cipher_alphabet] for _ in cipher_alphabet]

        # fill
        for r in range(len(tableau)):
            shift = r
            for c in range(len(tableau[r])):
                alphabet_index = shift % len(cipher_alphabet)
                tableau[r][c] = cipher_alphabet[alphabet_index]
                shift += 1

        return tableau

    def __str__(self):
        """
        Prints the tableau in a friendly format.

        :return: tableau
        :rtype: str
        """
        string_tableau = ""
        for r in range(len(self.tableau)):
            for c in range(len(self.tableau[r])):
                string_tableau += (self.tableau[r][c] + " ")

            string_tableau += "\n"
        return string_tableau
