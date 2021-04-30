#Desafio Poker

###Enunciado
Desenvolva um programa que, de acordo com as mãos de dois jogadores, informe qual deles é o vencedor.

###Informações para execução
Assim que executado o script vai pedir que o valor de ambas as mão seja passado, o valor deve seguir o padrão:
carta/espaço/carta/espaço/carta/espaço/carta/espaço/carta
cada carta é a combinação de um número entre 2 à 9 , ou das letras T,J,Q,K,A, e de umas da seguintes letras D,S,C,H.
Essa combinação corresponde ao rank da carta e ao naipe dela,
caso o valor seja apresentado de forma incorreta um erro será mostrado apresentando como o valor deve ser passado.

###Informações sobre a função who_win
A função pega o valor recebido pelos inputs checa se o valor digitado é compatível com o padrão de uma mão se o valor digitado for compatível então são criados dois objetos a partir da classe Hand com o valor dos inputs convertidos para listas. Após o valor ser convertido alguns métodos da classe hand são chamados para verificar se o valor de cada
carta é compatível com o esperado e para dar um valor para que a mão possa ser comparada com outra, logo após, o método
para comparar mãos é chamado, nele as mãos são comparadas
e o vencedor é informado.
###Informações sobre a classe Hand
O valor esperado por essa classe é uma lista com cinco itens
cada item deve ser uma string com dois caractéres. A partir
dessa lista são gerados alguns valores:

- O tipo de mão que é uma string informando qual a jogada
- O valor da mão que é um número usado para comparar mãos
- O maior valor dentro da jogada usado para obter a carta com maio valor
- E as cartas que são objetos do tipo Card

####Métodos da classe

- O metódo verify_hand usa os métodos ranks e suits da classe
  Card para garantir que os valores informados estão corretos
- O método even checa se a combinação de cartas é do tipo que
  envolve igualdade entre cartas ex: par, trincas e etc...
- O método highest_rank checa a carta com o maior rank na mão
- O método straight checa se a combinação é uma sequência
- O método flush checa se as cartas são do mesmo naipe
- O método compare_hands compara a mão com outra mão é retorna qual das duas é a vencedora.
- O método valorize_hand atribui os valores para a mão.

###Informações sobre a classe Card
Os valores esperados por essa classe são duas strings cada
uma com um caracter, estes são o rank e a suit da carta.

####Métodos da classe

- O método ranks garante que o valor passado como rank seja compatível com o esperado.
- O método suits garante que o valor passado como suit seja compatível com o esperado.
- O método is_equal_rank checa se o valor dos ranks de cada carta na mão são iguais
- O método is_equal_suit checa se o naipe de cada carta na mão são iguais
