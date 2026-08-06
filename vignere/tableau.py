import string

alphabet = string.ascii_uppercase

class tableau():

    # add keyword functionality later
    def __init__(self, keyword = ""):
        self.keyword = keyword
        self.basic_tableau = self.get_tableau()

    def get_tableau(self):
        basic_tableau = [["" for _ in alphabet] for _ in alphabet]

        # fill
        for r in range(len(basic_tableau)):
            shift = r
            for c in range(len(basic_tableau[r])):
                alphabet_index = shift % len(alphabet)
                basic_tableau[r][c] = alphabet[alphabet_index]
                shift += 1

        return basic_tableau

    def __str__(self):
        string_tableau = ""
        for r in range(len(self.basic_tableau)):
            for c in range(len(self.basic_tableau[r])):
                string_tableau += (self.basic_tableau[r][c] + " ")

            string_tableau += "\n"
        return string_tableau
