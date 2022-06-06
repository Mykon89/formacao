import random
import math

min = int(input("Informe o menor número: "))
max = int(input("Informe o maior número: "))

x = random.randint(min, max)
print("\n\tVocê tem somente {} chutes para acertar o número!" .format(round(math.log(max - min + 1, 2))))

cont = 0

while cont < math.log(max - min +1, 2):
    cont += 1

    chute = int(input("Chute um número: "))

    if x == chute:
        print("O número é {}" .format(x))
        print("Parabéns você acertou o chute em {} tentativas" .format(cont))

        break
    elif x > chute:
        print("Seu chute foi menor que o número escolhido!")
    elif x < chute:
        print("Seu chute foi maior que o número escolhido!")

if cont == math.log(max - min +1, 2):
    print("\nO número é {}" .format(x))
elif cont > math.log(max - min +1, 2):
    print("\tAcabou as chances, boa sorte da próxima!")
    
