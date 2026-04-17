import random 

PONTOS_POR_VITORIA = 10

def jogar_forca():
    print("="*40)
    print("BEM-VINDO AO JOGO DA FORCA!")
    print("="*40)

    banco_tematico = {
        "Animal": ["CACHORRO", "ELEFANTE", "GIRAFA", "MACACO", "TIGRE", "JACARE"],
        "Objeto": ["CADEIRA", "TECLADO", "TELEFONE", "RELOGIO", "MOCHILA", "GARRAFA"],
        "Profissão": ["MEDICO", "ENGENHEIRO", "PROFESSOR", "BOMBEIRO", "ADVOGADO", "PROGRAMADOR"],
        "Fruta": ["BANANA", "MORANGO", "ABACAXI", "LARANJA", "MELANCIA", "PITAYA"],
        "Ação": ["CORRER", "PULAR", "NADAR", "ESTUDAR", "TRABALHAR", "DORMIR"]
    }

    temas_disponiveis = list(banco_tematico.keys())

    tema_sorteado = random.choice(temas_disponiveis)
    
    palavra_oculta = random.choice(banco_tematico[tema_sorteado])
    
    letras_chutadas = [] 
    
    tracinhos = ["_"] * len(palavra_oculta) 
    
    vidas = 6 
    
    print(f"\nPREPARE-SE! O tema sorteado foi: >>> {tema_sorteado.upper()} <<<")
    print(f"A palavra tem {len(palavra_oculta)} letras.")
    
    while vidas > 0 and "_" in tracinhos:
        print(f"\nPalavra: {' '.join(tracinhos)}")
        print(f"Tentativas: {', '.join(letras_chutadas)}")
        print(f"Vidas restantes: {vidas}")
        chute = input("Digite uma letra: ").upper().strip()

        if len(chute) != 1 or not chute.isalpha():
            print("Entrada inválida! Digite apenas uma letra do alfabeto.")
            continue 

        if chute in letras_chutadas:
            print("Você já tentou essa letra! Escolha outra.")
            continue
        
        letras_chutadas.append(chute)

        if chute in palavra_oculta:
            print("Acertou a letra!")
            
            for indice, letra in enumerate(palavra_oculta):
                if letra == chute:
                    tracinhos[indice] = chute
        else:
            print("Letra incorreta!")
            vidas -= 1 

    print("\n" + "="*40)
    
    if "_" not in tracinhos:
            print(f"\n🏆 PARABÉNS! Você descobriu a palavra: {palavra_oculta}")
            print(f"Você ganhou {PONTOS_POR_VITORIA} pontos!")
            pontuacao_total_sessao += PONTOS_POR_VITORIA
    else:
            print(f"\n💀 INFELIZMENTE VOCÊ PERDEU!")
            print(f"A palavra era: {palavra_oculta}")
    
    return pontuacao_total_sessao
