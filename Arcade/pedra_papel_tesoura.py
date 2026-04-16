import os
import random

"""Função para limpar o terminal"""
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


"""Função com parametro digitado pelo jogador ou sorteado pelo computador"""
def pegar_nome_opcao(escolha):
    if escolha == 1:
        return "Pedra"
    elif escolha == 2:
        return "Papel"
    return "Tesoura"


def verificar_vencedor(jogo1, jogo2):
    if jogo1 == jogo2:
        return 0 

    if (jogo1 == 1 and jogo2 == 3) or (jogo1 == 2 and jogo2 == 1) or (jogo1 == 3 and jogo2 == 2):
        return 1

    return 2


def escolher_jogada(nome_jogador):
    while True:
        print(f"\n{nome_jogador}, escolha uma opção:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")

        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha in [1, 2, 3]:
                return escolha
            print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Erro: digite apenas números.")


def jogar_vs_pc(nome_jogador):
    pontuacao_partida = 0

    while True:
        print("\n=== JOGADOR VS COMPUTADOR ===")
        jogador = escolher_jogada(nome_jogador)
        computador = random.randint(1, 3)

        resultado = verificar_vencedor(jogador, computador)

        print(f"\n{nome_jogador} escolheu: {pegar_nome_opcao(jogador)}")
        print(f"O computador escolheu: {pegar_nome_opcao(computador)}")

        if resultado == 0:
            print("Foi empate!")
        elif resultado == 1:
            print(f"Parabéns, {nome_jogador}! Você ganhou!")
            print("Você recebeu +10 pontos.")
            pontuacao_partida += 10
        else:
            print(f"Você perdeu, {nome_jogador}!")

        print(f"Placar atual de {nome_jogador}: {pontuacao_partida} pontos")

        novamente = input("\nDeseja tentar de novo? (s/n): ").strip().lower()
        if novamente != "s":
            break

    return pontuacao_partida


def jogar_vs_jogador():
    while True:
        print("\n=== JOGADOR 1 VS JOGADOR 2 ===")
        jogador1 = escolher_jogada("Jogador 1")

        print("\nPassando a vez para o Jogador 2...")
        input("Pressione ENTER para continuar.")
        limpar_tela()

        print("=== JOGADOR 2 ===")
        jogador2 = escolher_jogada("Jogador 2")

        resultado = verificar_vencedor(jogador1, jogador2)

        print("\n=== RESULTADO ===")
        print(f"Jogador 1 escolheu: {pegar_nome_opcao(jogador1)}")
        print(f"Jogador 2 escolheu: {pegar_nome_opcao(jogador2)}")

        if resultado == 0:
            print("Foi empate!")
        elif resultado == 1:
            print("Jogador 1 venceu!")
        else:
            print("Jogador 2 venceu!")

        novamente = input("\nDeseja tentar de novo? (s/n): ").strip().lower()
        if novamente != "s":
            break

    return 0


"""Menu do jogo"""
def jogar(nome_jogador):
    pontuacao_total_jogo = 0

    while True:
        print("\n=== PEDRA, PAPEL E TESOURA ===")
        print("1 - Jogador vs Computador")
        print("2 - Jogador 1 vs Jogador 2")
        print("0 - Voltar ao menu")

        try:
            modo = int(input("Escolha o modo: "))

            if modo == 1:
                pontuacao_total_jogo += jogar_vs_pc(nome_jogador)
            elif modo == 2:
                jogar_vs_jogador()
            elif modo == 0:
                print("Voltando ao menu...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: digite apenas números.")

    return pontuacao_total_jogo