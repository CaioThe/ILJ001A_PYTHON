#Programa 2 – Este programa deve ter o nome Ex2.py                              Valor: de 0 a 10 pontos
#   A primeira coisa que o programa deve fazer são os prints com o número do grupo, os nomes completos dos
#   alunos e o número da questãoVamos criar um jogo de adivinhação de números. São dois jogadores e a ideia é
#   a seguinte: dado um intervalo fechado [Min, Max] um jogador sorteia (escolhe) um número qualquer que
#   esteja dentro do intervalo. O segundo jogador tem como desafio descobrir qualnúmero  foi  escolhido.
#   Para  isso  ele  deve  escolher  um  valor  e  anunciá-lo.  O  primeiro  jogador  deve  então  declarar
#   se  está  certo  ou errado. Se estiver certo, terminou o jogo. Se estiver errado deve ser informado se o
#   número a ser adivinhado é menor ou maiorque o palpite dado e o jogo continua. Ao final é preciso verificar
#   quantos palpites foram dados até que o valor tenha sido adivinhado e também quais foram esses palpites.
#   Escreva um programa no qual esse jogo seja implementado cumprindo os seguintes requisitos:
#
#   1.O programa deve ser implementado em duas opções(o programa é um só, com duas opções –não devem ser
#   feitos dois programas):
#       a.o sorteador é o computador e o adivinhador é humano;
#       b.o sorteador é o humano e o adivinhador é o computador;
#   2.Os valores Min e Max são fornecidos pelo usuário e podem ser quaisquer valores desde que Max seja maior
#   que Min + 100 (Max > Min + 100). É obrigatório que o programa verifique isso e não deixe jogar se essa
#   condição não for satisfeita.
#
#   Resposta:

import random


print("Grupo 6")      # nesta linha substitua a palavra TAL pelo número do seu grupo
print("CAIO THEMISTOCLES LIMA RIBEIRO")
print("TARCISIO DA SILVA SOUZA")
print("IGOR MENDES DA SILVA")
print("Questao 2")   # nesta linha substitua 999 pelo número da questão

Escolha = int(input("1 para adivinhar, 2 para sortear\n"))
Minimo = int(input("Digite um valor inteiro minimo maior que 1\n"))
Maximo = int(input("Digite um valor inteiro maximo maior que o minimo, em ao menos 100\n"))

print("Min = {}   e   Max = {}".format(Minimo, Maximo))

Primo = False
Soma = 0
Contador = 0
numero = 0
i = j = 0

if(Escolha == 1 and (Maximo-Minimo>=100)):
    numero = random.randint(Minimo,Maximo)
    while not Primo:
        teste = int(input("Digite o numero para verificar se acertou\n"))
        if (teste == numero):
            Primo = True
            print("Voce Acertou!!")
        else:
            print("Tente novamente\n")
        Contador +=1
    print("voce acertou o numero {} com {} tentativas, parabens!!".format(numero, Contador))
elif(Escolha == 2 and (Maximo-Minimo>=100)):
    while not Primo:
        numero = random.randint(Minimo,Maximo)
        print("Eu escolho o numero {}".format(numero))
        teste = int(input("Digite 1 para verificar se acertei\n"))
        if (teste == 1):
            Primo = True
            print("Acertei!!")
        else:
            print("Tentarei novamente\n")
        Contador +=1
    print("Acertei o numero {} com {} tentativas, parabens!!".format(numero, Contador))