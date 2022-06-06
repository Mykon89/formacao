import random

nome = input("Qual o seu nome? ")

print("Boa sorte {}!!" .format(nome))

palavras = ["arco-iris", "computador", "ciencia", "programacao",
            "python", "matematica", "jogador", "condicao", "reverso", "agua", "quadro", "geeks"]

palavra = random.choice(palavras).upper()

print("Escolha uma letra")

chutes = ""

chances = 12

while chances > 0:

    erro = 0

    for letra in palavra:

        if letra in chutes:
            print(letra)
        else:
            print("_")
            erro += 1
    
    if erro == 0:

        print("Você ganhou!!")
        print("A palavra é: ", palavra)
        break

    chute = input("Chute uma letra: ").upper()

    chutes += chute

    if chute not in palavra:
        chances -= 1

        print("Errado")

        print("Você tem mais {} chances" .format(chances))

        if chances == 0:
            print("Você perdeu!")
            print("A palavra era {}." .format(palavra))


