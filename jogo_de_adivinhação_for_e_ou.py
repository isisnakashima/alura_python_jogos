total_de_tentativas = 3
numero_secreto = 54

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou: ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue

    if chute == numero_secreto:
        print("Parábens, você acertou!")
        break
    else:
        if chute <= 53:
            print("Tente novamente, o número secreto é maior")
        elif chute >= 55:
            print("Tente novamente! O número é menor!")
    rodada = rodada + 1

    print("Obrigada por jogar!")
