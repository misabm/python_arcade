PONTOS_POR_ACERTO = 10

def carregar_banco_perguntas():
    """
    Retorna um Dicionário onde a chave é a pergunta e o valor é uma Tupla.
    A Tupla contém as 4 alternativas e o número da resposta correta no final.
    """
    return {
        "O que tem pescoço mas não tem cabeça?": ("Uma camisola", "Uma garrafa", "Um vaso", "Uma cadeira", 2),
        "Sou alto quando jovem e baixo quando velho. O que sou?": ("Um lápis", "Uma árvore", "Um prédio", "Um rio", 1),
        "O que é que quanto mais se tira, maior fica?": ("O cabelo", "Um buraco", "A paciência", "Uma dívida", 2),
        "O que tem chaves mas não abre portas?": ("Um piano", "Um teclado", "Um cadeado", "Um mapa", 1)
    }

def jogar():    
    print("\n===================================")
    print("BEM-VINDO AO QUIZ DE ENIGMAS")
    print("===================================")
    
    banco_perguntas = carregar_banco_perguntas()
    pontuacao_partida = 0
    historico_respostas = [] # Lista para guardar o desempenho
    
    for pergunta, dados_tupla in banco_perguntas.items():
        print(f"\n❓ Enigma: {pergunta}")
        
        opcoes = dados_tupla[:4] 
        resposta_correta = dados_tupla[4]
        
        for indice, alternativa in enumerate(opcoes, 1):
            print(f"[{indice}] - {alternativa}")
            
        while True:
            try:
                chute = int(input("Escolha a opção correta (1 a 4): "))
                
                if 1 <= chute <= 4:
                    break
                else:
                    print("⚠️ Aviso: Escolhe um número entre 1 e 4.")
                    
            except ValueError:
                print("❌ Erro: Por favor, digita apenas o número da alternativa!")
        
        if chute == resposta_correta:
            print("✅ Resposta Correta! Ganhaste pontos.")
            pontuacao_partida += PONTOS_POR_ACERTO
            historico_respostas.append( (pergunta, "Acertou") ) # Guardar como Tupla na Lista
        else:
            print(f"❌ Resposta Errada! A resposta certa era a opção {resposta_correta}.")
            historico_respostas.append( (pergunta, "Errou") )
            
    print("\n--- 📊 RESUMO DA TUA PARTIDA ---")
    for enigma, resultado in historico_respostas:
        print(f"{resultado} -> {enigma}")
        
    print(f"\nFim do Quiz! Acumulaste {pontuacao_partida} pontos.")
    
    return pontuacao_partida
