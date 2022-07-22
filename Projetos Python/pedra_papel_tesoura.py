import random


def joga():
    usuario = input(
        "Bem vindo ao jogo: Pedra, Papel e Tesoura!!\n"
        "'r' para pedra, 'p' para papel e 't' para tesoura\n"
        "Escolha umas das opções: ")
    computador = random.choice(['r', 'p', 't'])

    if usuario == 'r':
        escolha1 = 'Pedra'

    if usuario == 'p':
        escolha1 = 'Papel'

    if usuario == 't':
        escolha1 = 'Tesoura'

    if computador == 'r':
        escolha2 = 'Pedra'

    if computador == 'p':
        escolha2 = 'Papel'

    if computador == 't':
        escolha2 = 'Tesoura'

    if usuario == computador:
        print('O usuário escolheu {} e o computador escolheu {}.'.format(
            escolha1, escolha2))
        return 'Empate'

     # Pedra > Tesoura, Tesoura > Papel, Papel > Pedra

    if vence(usuario, computador):
        print('O usuário escolheu {} e o computador escolheu {}.'.format(
            escolha1, escolha2))
        return "Você venceu!"

    print('O usuário escolheu {} e o computador escolheu {}.'.format(
        escolha1, escolha2))
    return 'Você perdeu!'


def vence(jogador, oponente):
    # Retorna verdadeiro se o jogador vencer

    if (jogador == 'r' and oponente == 't')\
            or (jogador == 't' and oponente == 'p')\
            or (jogador == 'p' and oponente == 'r'):
        return True


print(joga())
