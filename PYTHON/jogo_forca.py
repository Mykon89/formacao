import random

palavras = ["arco-iris", "computador", "ciencia", "programacao",
            "python", "matematica", "jogador", "condicao", "reverso", "agua", "quadro", "geeks"]

palavra = random.choice(palavras).upper()

for letra in palavra:
    print("_", end = " ")

tam = len(palavra)

