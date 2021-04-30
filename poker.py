import re
from hand import Hand


def who_win():
    player_one_hand = input("Digite a mão do primeiro jogador: ")
    player_two_hand = input("Digite a mão do segundo jogador: ")
    if player_one_hand != player_two_hand:
        pattern = r"(\w{2}\s){4}(\w{2})"
        if bool(re.match(pattern, player_one_hand)) and bool(re.match(pattern, player_two_hand)):
            for card_one in player_one_hand.split(" "):
                for card_two in player_two_hand.split(" "):
                    if card_one == card_two:
                        raise ValueError(
                            '''Uma das cartas passada para uma das mãos é igual ao valor de uma carta passada para outra mão''')
            player_one = Hand(player_one_hand.split(" "))
            player_two = Hand(player_two_hand.split(" "))
            player_one.verify_hand()
            player_two.verify_hand()
            player_one.valorize_hand()
            player_two.valorize_hand()
            player_one.compare_hands(player_two)

        else:
            raise ValueError(
                '''O valor digitado para uma das mãos está incorreto certifique-se que o valor de cada carta esteja separado
                por espaços entre elas''')
    else:
        raise ValueError(
            '''O valor digitados para ambas as mãos é igual, tente novamente com valores diferentes''')


who_win()
