import adivinhacao
import forca
import main
import pedra_papel_tesoura
import quiz_enigmas
import velha


def exibir_menu(nome_jogador):
    total = main.obter_total(nome_jogador)
    print("\n===================================")
    print("BEM-VINDO AO PYTHON ARCADE")
    print("===================================")
    print(f"Jogador: {nome_jogador} | Pontos: {total}")
    print("1 - Jogo da Adivinhacao")
    print("2 - Jogo da Forca")
    print("3 - Jogo da Velha")
    print("4 - Quiz e Enigmas")
    print("5 - Pedra, Papel e Tesoura")
    print("6 - Ver tabela detalhada de pontos")
    print("0 - Sair da Plataforma")


def executar_jogo(escolha, nome_jogador):
    if escolha == 1:
        return adivinhacao.jogar()
    if escolha == 2:
        return forca.jogar()
    if escolha == 3:
        return velha.jogar()
    if escolha == 4:
        return quiz_enigmas.jogar()
    if escolha == 5:
        return pedra_papel_tesoura.jogar(nome_jogador)
    if escolha == 6:
        main.exibir_tabela_pontos(nome_jogador)
        return None
    return 0


def iniciar_plataforma():
    nome_jogador = input("Digite seu nickname: ").strip()

    if not nome_jogador:
        nome_jogador = "Jogador"

    main.garantir_jogador(nome_jogador)

    while True:
        exibir_menu(nome_jogador)

        try:
            escolha = int(input("Escolha seu jogo: "))
        except ValueError:
            print("Erro: por favor, digite apenas numeros.")
            continue

        if escolha == 0:
            main.exibir_resumo_jogador(nome_jogador)
            main.exibir_ranking_final()
            print("\nObrigado por jogar! Ate a proxima.")
            break

        if escolha not in main.NOMES_DOS_JOGOS and escolha != 6:
            print("Opcao invalida! Escolha um numero do menu.")
            continue

        pontos = executar_jogo(escolha, nome_jogador)

        if escolha == 6:
            continue

        main.registrar_pontos(nome_jogador, main.NOMES_DOS_JOGOS[escolha], pontos)

        print(
            f"\nPontuacao atualizada: {nome_jogador} agora tem "
            f"{main.obter_total(nome_jogador)} ponto(s)."
        )


if __name__ == "__main__":
    iniciar_plataforma()
