é necessário uma lógica para as cartas
outra para a mão

A função deve receber dois parametros que representam o valor da mão de cada jogador
e deve devolver qual dos dois é o vencedor.

A lógica para trabalhar com a mão deve ser algo como:
Pegar o input, que deve ser uma string, e transformar em uma lista
a lista deve ter os elementos separados em cartas
Ex: ["2C", "3H", etc...]

A lógica para as cartas deve "valorizar" o par número e letra
Existe 4 pares que são duas letras ex: "AH"
são 36 cartas com número e letras
são 16 cartas com letras e letras
no total 52 cartas

Garantir que os inputs sejam mãos válidas
Garantir que se válido tenha a "disposição" correta
ex["carta",espaço"carta"]
Se len = 1 siginfica que o input veio sem espaço separando as cartas
criar uma lógica que faça isso
Ou
Aceitar inputs somente no formato exato
pra isso dá pra levantar um erro

Sistema de pontuação

A função de carta vai dentro da função mão que é onde os pontos são contados
a função who_win serve para receber os dados e retornar a resposta, logo a função mão vai dentro dela

OK, como eu posso dar o valor para cada carta?

Cada carta recebe um valor individual depedendo do rank
[2,3,4,5,6,7,8,9,10,11,12,13,14]
11 = valete
12 = rainha
13 = rei
14 = ás

Separar cada carta em um formato chave valor?

Dentro do objeto card:

- regras para garantir que os inputs estejam corretos
- dentro da classe é necessário métodos para comparar o valor das cartas
- O método "igual" deve cuidar dos pares trincas e etc...
- o método sequencia deve cuidar das sequências
