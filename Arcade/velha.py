def jogar():

    tabuleiro = [" " for i in range(9)]

    def mostrar():
        print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
        print("--+---+--")
        print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
        print("--+---+--")
        print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

    def venceu(jogador):
        if (tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or \
           (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or \
           (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) or \
           (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or \
           (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or \
           (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) or \
           (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or \
           (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador):
            return True
        return False

    jogador = "X"

    for rodada in range(9):
        mostrar()

        pos = int(input(f"Jogador {jogador}, escolha uma posição (0 a 8): "))

        if tabuleiro[pos] == " ":
            tabuleiro[pos] = jogador
        else:
            print("Posição ocupada!")
            continue

        if venceu(jogador):
            mostrar()
            print(f"Parabéns, jogador {jogador}, você venceu!")
            return 0

        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"

    mostrar()
    print("Deu velha (empate)!")
    return 0