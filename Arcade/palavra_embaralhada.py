import random


PONTOS_POR_ACERTO = 10
MAX_TENTATIVAS = 3

PALAVRAS = [
    "python",
    "arcade",
    "computador",
    "programacao",
    "desafio",
    "teclado",
    "monitor",
    "algoritmo",
    "variavel",
    "internet",
    "jogador",
    "pontuacao",
    "terminal",
    "memoria",
    "processador",
    "sistema",
    "janela",
    "caderno",
    "escola",
    "estudante",
    "professor",
    "atividade",
    "raciocinio",
    "biblioteca",
    "interface",
    "comando",
    "arquivo",
    "funcao",
    "repeticao",
    "condicao",
]


def embaralhar_palavra(palavra):
    letras = list(palavra)

    while True:
        random.shuffle(letras)
        palavra_embaralhada = "".join(letras)

        if palavra_embaralhada != palavra:
            return palavra_embaralhada


def jogar_palavra_embaralhada():
    print("\n===================================")
    print("BEM-VINDO A PALAVRA EMBARALHADA")
    print("===================================")

    pontuacao_partida = 0
    palavras_sorteadas = random.sample(PALAVRAS, 3)

    for rodada, palavra in enumerate(palavras_sorteadas, start=1):
        palavra_embaralhada = embaralhar_palavra(palavra)

        print(f"\nRodada {rodada}")
        print(f"Descubra a palavra: {palavra_embaralhada}")

        acertou = False

        for tentativa in range(1, MAX_TENTATIVAS + 1):
            chute = input(
                f"Tentativa {tentativa}/{MAX_TENTATIVAS}: "
            ).strip().lower()

            if chute == palavra:
                print("Parabens! Voce acertou a palavra.")
                pontuacao_partida += PONTOS_POR_ACERTO
                acertou = True
                break

            print("Palavra incorreta.")

        if not acertou:
            print(f"A palavra correta era: {palavra}")

    print(f"\nFim do jogo! Voce fez {pontuacao_partida} pontos.")
    return pontuacao_partida


def jogar():
    return jogar_palavra_embaralhada()
