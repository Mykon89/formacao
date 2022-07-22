import os
import random
from colorama import Fore, Back, Style

# Declaração das variáveis utilizadas no jogo da velha
jogarNovamente = "s"
# Numero máximo de jogadas são 9 no jogo da velha
jogadas = 0
maxJogadas = 9
quemJoga = 2  # 1 = CPU e 2 = Jogador
# Pode ser do tipo boolean
vit = "n"
# Criação de uma matriz (list)
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# função da tela para redesenhar as jogadas na matriz "velha"
def tela():
    global velha
    global jogadas
    # Limpar a tela, importado direto do "import os"
    os.system('cls')
    # Impressão das colunas e linhas
    print("    0   1   2")
    print("0:   " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -------------")
    print("1:   " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -------------")
    print("2:   " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    # Imprimindo as jogadas na cor verde com a biblioteca Fore
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

# Função das jogadas do jogador
def jogadorJoga():
    # Variáveis da rotina da função jogadorJoga
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        # Testando se as informações de linha e coluna estão corretas
        try:
            l = int(input("Linha..: "))
            c = int(input("Coluna..: "))
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna..: "))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha e/ou coluna inválida!")
            os.system("pause")
            #vit = "n"

# Função da CPU
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        # Jogadas randomizadas da CPU
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        quemJoga = 2
        jogadas += 1

# Função para verificar quem ganhou, ao todo de 8 verificações para cada jogador
def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    # Executa uma iteração do for para X e O
    for s in simbolos:
        vitoria = "n"
        # Verificar vitorias em linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(velha[il][ic] == s):
                    soma += 1
                ic += 1
            il += 1
            if(soma == 3):
                vitoria = s
                break
        if(vitoria != "n"):
            break

        # Verificar vitorias em colunas
        ic = il = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(velha[il][ic] == s):
                    soma += 1
                il += 1
            ic += 1
            if(soma == 3):
                vitoria = s
                break
        if(vitoria != "n"):
            break

        # Verificar vitoria na diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if(velha[idiag][idiag] == s):
                soma += 1
            idiag += 1
            if(soma == 3):
                vitoria = s
                break
        if(vitoria != "n"):
            break

        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagl < 3:
            if(velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
            if(soma == 3):
                vitoria = s
                break
        if(vitoria != "n"):
            break
    return vitoria

def redefinir():
    # Declaração das variáveis utilizadas no jogo da velha
    # Numero máximo de jogadas são 9 no jogo da velha
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    maxJogadas = 9
    quemJoga = 2  # 1 = CPU e 2 = Jogador
    # Pode ser do tipo boolean
    vit = "n"
    # Criação de uma matriz (list)
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]    
while(jogarNovamente == "s"):
    # Loop principal do jogo
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarVitoria()
        if(vit != "n") or (jogadas >= maxJogadas):
            break

    print(Fore.RED + "Fim de Jogo" + Fore.YELLOW)
    if(vit == "X" or vit == "O"):
        print("Resultado: Jogador " + vit + " venceu")
    else:
        print("Resultado: Empate")
    jogarNovamente = input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
    redefinir()
        
