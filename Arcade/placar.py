PLACAR_GERAL = {}

NOMES_DOS_JOGOS = {
    1: "Jogo da Adivinhacao",
    2: "Jogo da Forca",
    3: "Jogo da Velha",
    4: "Quiz e Enigmas",
    5: "Pedra, Papel e Tesoura",
    6: "Palavra Embaralhada",
}


def garantir_jogador(nome_jogador):
    if nome_jogador not in PLACAR_GERAL:
        PLACAR_GERAL[nome_jogador] = {
            "total": 0,
            "partidas": 0,
            "jogos": {nome_jogo: 0 for nome_jogo in NOMES_DOS_JOGOS.values()},
        }


def registrar_pontos(nome_jogador, nome_jogo, pontos):
    garantir_jogador(nome_jogador)

    if not isinstance(pontos, (int, float)):
        pontos = 0

    pontos = int(pontos)

    PLACAR_GERAL[nome_jogador]["total"] += pontos
    PLACAR_GERAL[nome_jogador]["partidas"] += 1
    PLACAR_GERAL[nome_jogador]["jogos"][nome_jogo] += pontos


def obter_total(nome_jogador):
    garantir_jogador(nome_jogador)
    return PLACAR_GERAL[nome_jogador]["total"]


def exibir_resumo_jogador(nome_jogador):
    garantir_jogador(nome_jogador)
    dados = PLACAR_GERAL[nome_jogador]

    print("\n=========== PLACAR GERAL ===========")
    print(f"Jogador: {nome_jogador}")
    print(f"Jogos jogados: {dados['partidas']}")
    print(f"Pontuacao total: {dados['total']}")
    print("\nPontos por jogo:")

    for nome_jogo, pontos in dados["jogos"].items():
        print(f"- {nome_jogo}: {pontos} ponto(s)")


def exibir_tabela_pontos(nome_jogador):
    garantir_jogador(nome_jogador)
    dados = PLACAR_GERAL[nome_jogador]

    print("\n========== TABELA DE PONTOS ==========")
    print(f"Jogador: {nome_jogador}")
    print(f"Total geral: {dados['total']} ponto(s)")
    print(f"Partidas registradas: {dados['partidas']}")
    print("Onde os pontos foram feitos:")
    print("--------------------------------------")

    for nome_jogo, pontos in dados["jogos"].items():
        if pontos > 0:
            print(f"{nome_jogo}: {pontos} ponto(s)")
        else:
            print(f"{nome_jogo}: nenhum ponto ate agora")


def exibir_ranking_final():
    print("\n=========== RANKING FINAL ===========")

    ranking = sorted(
        PLACAR_GERAL.items(),
        key=lambda item: (-item[1]["total"], item[0].lower()),
    )

    for posicao, (nome_jogador, dados) in enumerate(ranking, start=1):
        print(
            f"{posicao}. {nome_jogador} - "
            f"{dados['total']} ponto(s) em {dados['partidas']} jogo(s)"
        )
