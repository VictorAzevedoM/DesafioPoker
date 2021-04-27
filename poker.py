import re
import itertools


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def ranks(self):
        pattern = r"([2-9]|10|A|Q|K|J)"
        if bool(re.match(pattern, self.rank)):
            if self.rank == "J":
                self.rank = "11"
            elif self.rank == "Q":
                self.rank = "12"
            elif self.rank == "K":
                self.rank = "13"
            elif self.rank == "A":
                self.rank = "14"
            else:
                self.rank
            print(self.rank)
        else:
            raise ValueError(
                '''O primeiro valor informado de cada carta deve ser um número de 2 à 10 ou as letras A,K,Q e J''')

    def suits(self):
        pattern = r"(D|S|C|H)"
        if bool(re.match(pattern, self.suit)):
            print(self.suit)
        else:
            raise ValueError(
                '''O primeiro valor informado de cada carta deve ser um número de 2 à 10 ou as letras A,K,Q e J''')

    def is_equal(self, other_card):
        if int(self.rank) == int(other_card.rank):
            return True
        else:
            return False


class Hand():
    def __init__(self, hand):
        self.hand = hand
        self.type_of_hand = ""
        self.cards = []
        for card in self.hand:
            card = Card(rank=card[0], suit=card[1])
            self.cards.append(card)

    def verify_hand(self):
        for card in self.cards:
            card.ranks()
            card.suits()

    def even(self):
        for card_one, card_two, card_three, card_four, card_five in itertools.combinations(self.cards, 5):
            if card_one.is_equal(card_two) and card_one.is_equal(card_three) and card_four.is_equal(card_five) and not card_one.is_equal(card_four):
                self.type_of_hand = "Full House"
                return True
            elif card_one.is_equal(card_two) and card_one.is_equal(card_three) and card_one.is_equal(card_four):
                self.type_of_hand = "Four of a kind"
                return True
            elif card_one.is_equal(card_two) and card_three.is_equal(card_four) and not card_one.is_equal(card_three):
                self.type_of_hand = "Two Pairs"
                return True
            elif card_one.is_equal(card_two) and card_one.is_equal(card_three):
                self.type_of_hand = "Three of a kind"
                return True
            elif card_one.is_equal(card_two):
                self.type_of_hand = "Pair"
                return True
            else:
                return False

    def highest_rank(self):
        highest_card = []
        for card in self.cards:
            highest_card.append(int(card.rank))
        print(highest_card)
        return max(highest_card)

    def straight(self):
        list_of_ranks = []
        for card in self.cards:
            list_of_ranks.append(int(card.rank))
        if sorted(list_of_ranks) == list(range(min(list_of_ranks), max(list_of_ranks)+1)):
            self.type_of_hand = "Straight"
            return True
        else:
            return False

    def flush(self):
        if self.straight():
            pass
        pass

    def result(self):
        self.even()
        print(self.type_of_hand)
        print(self.highest_rank())
        print(self.straight())


def who_win():
    player_one_hand = input("Digite a mão do primeiro jogador: ")
    player_two_hand = input("Digite a mão do segundo jogador: ")
    pattern = r"(\w{2}\s){4}(\w{2})"
    if bool(re.match(pattern, player_one_hand)) and bool(re.match(pattern, player_two_hand)):
        player_one = Hand(player_one_hand.split(" "))
        player_two = Hand(player_two_hand.split(" "))
        player_one.verify_hand()
        player_two.verify_hand()
        player_one.result()
    else:
        raise ValueError(
            '''O valor digitado para uma das mãos está incorreto certifique-se que o valor de cada carta esteja separado
            por espaços entre elas''')


who_win()
