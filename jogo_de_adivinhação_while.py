print("*********************************")
print("Bem vindos ao jogo de adivinhação")
print("*********************************")

total_de_tentativas = 3
numero_secreto = 54
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # as {} funcionam como se fossem a rodada e o total de tentativas ou seja as strings.
    # o format serve como um direcionamento, fala qual valor vai para cada chave -> interpolação de strings
    chute=(int(input("Digite o seu número: ")))
    print("Você digitou: ", chute)

    if chute == 54:
        print("Parábens, você acertou!")
    else:
        if chute <= 53:
            print("Tente novamente, o número secreto é maior")
        elif chute >= 55:
            print("Tente novamente! O número é menor!")
    rodada = rodada  + 1

print("Obrigada por jogar!")
