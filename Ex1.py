#   Programa 1 –Este programa deve ter o nome Ex1.py                         Valor: de 0 a 10 pontos
#   A primeira coisa que o programa deve fazer são os prints com o número do grupo, os nomes completos
#   dos alunos e o número da questão.
#
#   Escreva um programa que leia o número inteiro Min, obrigatoriamente maior que 1. Leia outro  número inteiro
#   Max, obrigatoriamente maior que Min. Após a leitura, o programa deve mostrar na tela esses dois valores
#   Min e Max, conforme os exemplos abaixo. Em  seguida  o  programa  deve  mostrar  na  tela  todos  os
#   números  primos  situados  no  intervalo  fechado  definido  pelos  valores  [Min, Max]. Quando se diz que
#   o intervalo é fechado, isso inclui os extremos, Min e Max. O programa também deve apresentar na tela a
#   quantidade  de  números  primos  e  a  soma  de  todos  eles,  conforme  mostrado  nos  exemplos.  Caso
#   não  haja  primos  no  intervalo,  o programa deve exibir a mensagem: "Não há primos no intervalo [Min, Max]"
#   (veja o Exemplo 3).
#   
#   Exemplo 1
#   Min = 2   e   Max = 20
#   2
#   3
#   5
#   7
#   11
#   13
#   17
#   19
#   Quantidade de primos no intervalo [2, 20] = 8
#   Soma dos primos no intervalo [2, 20] = 77
#   
#   Exemplo 2
#   Min = 401   e   Max = 449
#   401
#   409
#   419
#   421
#   431
#   433
#   439
#   443
#   449
#   Quantidade de primos no intervalo [401, 449] = 9
#   Soma dos primos no intervalo [401, 449] = 3845
#   
#   Exemplo 3
#   Min = 19610 e   Max = 19660
#   Não há primos no intervalo [19610, 19660]
#
#   Resposta:


print("Grupo 6")      # nesta linha substitua a palavra TAL pelo número do seu grupo
print("CAIO THEMISTOCLES LIMA RIBEIRO")
print("TARCISIO DA SILVA SOUZA")
print("IGOR MENDES DA SILVA")
print("Questao 1")   # nesta linha substitua 999 pelo número da questão

Minimo = int(input("Digite um valor inteiro minimo maior que 1\n"))
Maximo = int(input("Digite um valor inteiro maximo maior que o minimo\n"))

print("Min = {}   e   Max = {}".format(Minimo, Maximo))

Primo = False
Soma = 0
Contador = 0
i = 2
j = Minimo

while j <= Maximo:
    Primo = False
    if Minimo > 1:
        while i < j:
            if (j % i) == 0:
                Primo = True
            i += 1
    i=2
    if not Primo:
        print("{}".format(j))
        Soma = Soma + j
        Contador+=1        
    j+=1
if Contador == 0:
    print("Não há primos no intervalo [{}, {}]".format(Minimo, Maximo))
else:
    print("Quantidade de primos no intervalo [{}, {}] = {}". format(Minimo, Maximo, Contador))
    print("Soma dos primos no intervalo [{}, {}] = {}". format(Minimo, Maximo, Soma))
