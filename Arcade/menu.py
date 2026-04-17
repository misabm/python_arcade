import forca
import palavra_embaralhada
import pedra_papel_tesoura
import placar
import quiz_enigmas
import velha


def exibir_menu(nome_jogador):
    total = placar.obter_total(nome_jogador)
    print("\n===================================")
    print("BEM-VINDO AO PYTHON ARCADE")
    print("===================================")
    print(f"Jogador: {nome_jogador} | Pontos: {total}")
    print("1 - Jogo da Forca")
    print("2 - Jogo da Velha")
    print("3 - Quiz e Enigmas")
    print("4 - Pedra, Papel e Tesoura")
    print("5 - Palavra Embaralhada")
    print("6 - Ver tabela detalhada de pontos")
    print("0 - Sair da Plataforma")


def executar_jogo(escolha, nome_jogador):
    if escolha == 1:
        return forca.jogar_forca()
    if escolha == 2:
        return velha.jogar()
    if escolha == 3:
        return quiz_enigmas.jogar()
    if escolha == 4:
        return pedra_papel_tesoura.jogar(nome_jogador)
    if escolha == 5:
        return palavra_embaralhada.jogar()
    if escolha == 6:
        placar.exibir_tabela_pontos(nome_jogador)
        return None
    return 0


def iniciar_plataforma():
    nome_jogador = input("Digite seu nickname: ").strip()

    if not nome_jogador:
        nome_jogador = "Jogador"

    placar.garantir_jogador(nome_jogador)

    while True:
        exibir_menu(nome_jogador)

        try:
            escolha = int(input("Escolha seu jogo: "))
        except ValueError:
            print("Erro: por favor, digite apenas números.")
            continue

        if escolha == 0:
            placar.exibir_resumo_jogador(nome_jogador)
            placar.exibir_ranking_final()
            print("\nObrigado por jogar! Até a próxima.")
            break

        if escolha not in placar.NOMES_DOS_JOGOS and escolha != 6:
            print("Opção inválida! Escolha um número do menu.")
            continue

        pontos = executar_jogo(escolha, nome_jogador)

        if escolha == 6:
            continue

        placar.registrar_pontos(
            nome_jogador,
            placar.NOMES_DOS_JOGOS[escolha],
            pontos,
        )

        print(
            f"\nPontuação atualizada: {nome_jogador} agora tem "
            f"{placar.obter_total(nome_jogador)} ponto(s)."
        )