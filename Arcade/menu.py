import adivinhacao
import forca
import velha
import quiz_enigmas
import pedra_papel_tesoura


def iniciar_plataforma():
    print("===================================")
    print("🎮 BEM-VINDO AO PYTHON ARCADE 🎮")
    print("===================================")
    nome_jogador = input("Digite seu nickname: ")
    pontuacao_total = 0

    while True:
        print(f"\nJogador: {nome_jogador} | Pontos: {pontuacao_total}")
        print("1 - Jogo da Adivinhação")
        print("2 - Jogo da Forca")
        print("3 - Jogo da Velha")
        print("4 - Quiz e Enigmas")
        print("5 - Pedra, Papel e Tesoura")
        print("0 - Sair da Plataforma")

        try:
            escolha = int(input("Escolha seu jogo: "))

            if escolha == 1:
                pontuacao_total += adivinhacao.jogar()
            elif escolha == 2:
                pontuacao_total += forca.jogar()
            elif escolha == 3:
                velha.jogar()
            elif escolha == 4:
                pontuacao_total += quiz_enigmas.jogar()
            elif escolha == 5:
                pontuacao_total += pedra_papel_tesoura.jogar(nome_jogador)
            elif escolha == 0:
                print("Obrigado por jogar! Até a próxima.")
                break
            else:
                print("Opção inválida! Escolha um número do menu.")
        except ValueError:
            print("Erro: Por favor, digite apenas números!")