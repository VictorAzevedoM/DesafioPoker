
import itertools
from card import Card


class Hand():
    def __init__(self, hand):
        self.hand = hand
        self.type_of_hand = ""
        self.value_of_hand = 0
        self.highest_value_of_combination = 0
        self.cards = []
        for card in self.hand:
            card = Card(rank=card[0], suit=card[1])
            self.cards.append(card)

    def verify_hand(self):
        for card in self.cards:
            card.ranks()
            card.suits()
        for card_one, card_two in itertools.combinations(self.cards, 2):
            if card_one.is_equal_rank(card_two) and card_one.is_equal_suit(card_two):
                raise ValueError('''O valor informado para pelo menos duas cartas na mão é exatamente igual, certifique-se que
                as cartas com o memso rank tenham naipes diferentes''')

    def even(self):
        for card_one, card_two, card_three, card_four, card_five in itertools.combinations(self.cards, 5):
            if card_one.is_equal_rank(card_two) and card_one.is_equal_rank(card_three) and card_four.is_equal_rank(card_five) and not card_one.is_equal_rank(card_four):
                self.type_of_hand = "Full House"
                self.value_of_hand = 6
                return True
            elif card_one.is_equal_rank(card_two) and card_one.is_equal_rank(card_three) and card_one.is_equal_rank(card_four):
                self.type_of_hand = "Four of a kind"
                self.value_of_hand = 7
                self.highest_value_of_combination = int(card_one.rank)
                return True
            elif card_one.is_equal_rank(card_two) and card_three.is_equal_rank(card_four) and not card_one.is_equal_rank(card_three):
                self.type_of_hand = "Two Pairs"
                self.value_of_hand = 2
                self.highest_value_of_combination = int(card_one.rank)
                return True
            elif card_one.is_equal_rank(card_two) and card_one.is_equal_rank(card_three):
                self.type_of_hand = "Three of a kind"
                self.value_of_hand = 3
                self.highest_value_of_combination = int(card_one.rank)
                return True
            elif card_one.is_equal_rank(card_two):
                self.type_of_hand = "Pair"
                self.value_of_hand = 1
                self.highest_value_of_combination = int(card_one.rank)
                return True
            else:
                return False

    def highest_rank(self):
        highest_card = []
        for card in self.cards:
            highest_card.append(int(card.rank))
        return max(highest_card)

    def straight(self):
        list_of_ranks = []
        for card in self.cards:
            list_of_ranks.append(int(card.rank))
        if sorted(list_of_ranks) == [10, 11, 12, 13, 14]:
            self.type_of_hand = "Royal"
            return True
        elif sorted(list_of_ranks) == list(range(min(list_of_ranks), max(list_of_ranks)+1)):
            self.type_of_hand = "Straight"
            self.value_of_hand = 4
            return True
        else:
            return False

    def flush(self):
        if self.straight():
            for card_one, card_two, card_three, card_four, card_five in itertools.combinations(self.cards, 5):
                if card_one.is_equal_suit(card_two) and card_one.is_equal_suit(card_three) and card_one.is_equal_suit(card_four) and card_one.is_equal_suit(card_five) and self.type_of_hand == "Royal":
                    self.type_of_hand = "Royal Flush"
                    self.value_of_hand = 9
                    return True
                elif card_one.is_equal_suit(card_two) and card_one.is_equal_suit(card_three) and card_one.is_equal_suit(card_four) and card_one.is_equal_suit(card_five):
                    self.type_of_hand = "Straight Flush"
                    self.value_of_hand = 8
                    return True
        elif not self.straight():
            for card_one, card_two, card_three, card_four, card_five in itertools.combinations(self.cards, 5):
                if card_one.is_equal_suit(card_two) and card_one.is_equal_suit(card_three) and card_one.is_equal_suit(card_four) and card_one.is_equal_suit(card_five):
                    self.type_of_hand = "Flush"
                    self.value_of_hand = 5
                    return True
        else:
            return False

    def valorize_hand(self):
        self.even()
        self.highest_rank()
        self.straight()
        self.flush()
        if self.value_of_hand == 0:
            self.type_of_hand = "Highest rank"

    def compare_hands(self, other_hand):
        if self.value_of_hand > other_hand.value_of_hand:
            print("O primeiro jogador venceu com: ")
            print(self.type_of_hand)
            print(self.hand)
        elif self.value_of_hand == other_hand.value_of_hand:
            if self.highest_value_of_combination == other_hand.highest_value_of_combination:
                if self.type_of_hand == "Straight Flush" or self.type_of_hand == "Straight":
                    print("Empate, ambos jogadores tem uma sequência de cartas igual")
                    print(self.type_of_hand)
                    print(self.hand)
                    print(other_hand.type_of_hand)
                    print(other_hand.hand)
                else:
                    while self.highest_rank() == other_hand.highest_rank():
                        if len(self.cards) == 0:
                            print(
                                "Empate ambos jogadores possuem a mesma mão e os mesmos valores")
                            print(self.type_of_hand)
                            print(self.hand)
                            print(other_hand.type_of_hand)
                            print(other_hand.hand)
                            break

                        else:
                            self.cards.pop(card for card in self.cards
                                           if int(card.rank) == self.highest_rank())
                            other_hand.cards.pop(card for card in other_hand.cards
                                                 if int(card.rank) == other_hand.highest_rank())
                    if self.highest_rank() > other_hand.highest_rank():
                        print("O primeiro jogador venceu com: ")
                        print(self.type_of_hand)
                        print(self.hand)
                    else:
                        print("O segundo jogador venceu com: ")
                        print(other_hand.type_of_hand)
                        print(other_hand.hand)

            elif self.highest_value_of_combination > other_hand.highest_value_of_combination:
                print("O primeiro jogador venceu com: ")
                print(self.type_of_hand)
                print(self.hand)
            elif self.type_of_hand == "Royal Flush":
                print("Empate, ambos jogadores tem um Royal Flush")
                print(self.type_of_hand)
                print(self.hand)
                print(other_hand.type_of_hand)
                print(other_hand.hand)
            else:
                print("O segundo jogador venceu com: ")
                print(other_hand.type_of_hand)
                print(other_hand.hand)
        else:
            print("O segundo jogador venceu com: ")
            print(other_hand.type_of_hand)
            print(other_hand.hand)
