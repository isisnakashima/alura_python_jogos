import random

print("*****************")
print("Sejam bem vindos!")
print("*****************")

numero_secreto = int(round(random.randrange(1, 101)))
total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou: ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue

    if numero_secreto == chute:
        print("Parábens, você acertou!")
        break
    else:
        if numero_secreto > chute:
            print("Tente novamente, o número secreto é maior")
        elif numero_secreto < chute:
            print("Tente novamente! O número é menor!")
    rodada = rodada + 1
    print("Obrigada por jogar!")
