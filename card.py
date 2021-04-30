import re


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def ranks(self):
        pattern = r"([2-9]|T|A|Q|K|J)"
        if bool(re.match(pattern, self.rank)):
            if self.rank == "T":
                self.rank = "10"
            elif self.rank == "J":
                self.rank = "11"
            elif self.rank == "Q":
                self.rank = "12"
            elif self.rank == "K":
                self.rank = "13"
            elif self.rank == "A":
                self.rank = "14"
            else:
                self.rank
        else:
            raise ValueError(
                '''O primeiro valor informado de cada carta deve ser um número de 2 à 10 ou as letras A,K,Q e J''')

    def suits(self):
        pattern = r"(D|S|C|H)"
        if bool(re.match(pattern, self.suit)):
            return True
        else:
            raise ValueError(
                '''O segundo valor informado de cada carta deve ser D,S,C ou H''')

    def is_equal_rank(self, other_card):
        if int(self.rank) == int(other_card.rank):
            return True
        else:
            return False

    def is_equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else:
            return False
