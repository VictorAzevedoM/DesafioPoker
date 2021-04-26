class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def ranks(self):
        print(self.rank)

    def suits(self):
        print(self.suit)

    def is_equal(self, other_card):
        if int(self.rank) == int(other_card.rank):
            return True
        else:
            return False

    def is_greater(self, other_card):
        if int(self.rank) > int(other_card.rank):
            return True
        else:
            return False

    def is_lower(self, other_card):
        if int(self.rank) < int(other_card.rank):
            return True
        else:
            return False


class Hand():
    def __init__(self, hand):
        self.hand = hand
        self.cards = []
        for card in self.hand:
            card = Card(rank=card[0], suit=card[1])
            self.cards.append(card)

    def verify_hand(self):
        for card in self.cards:
            card.ranks()
            card.suits()


def who_win():
    player_one_hand = input("Digite a mão do primeiro jogador: ")
    player_two_hand = input("Digite a mão do segundo jogador: ")
    if player_one_hand and player_two_hand:
        player_one = Hand(player_one_hand.split(" "))
        player_two = Hand(player_two_hand.split(" "))
        player_one.verify_hand()
        player_two.verify_hand()
    else:
        raise ValueError(
            "O valor digitado para uma das mãos está incorreto certifique-se que o valor apresentado seja:")


who_win()
