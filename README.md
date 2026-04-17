# 🎮 Python Arcade

## 📖 Descrição do Projeto
O **Python Arcade** é uma plataforma interativa de minijogos via linha de comando (CLI) desenvolvida 100% em Python. 

O projeto foi construído para colocar em prática os fundamentos da linguagem, unindo lógica matemática e diversão. A arquitetura do sistema foi desenhada de forma modular: cada jogo possui o seu próprio ficheiro (módulo) e funciona de forma independente, mas todos são orquestrados por um "Hub Central" que gere a sessão do utilizador e um sistema global de pontuação.

Durante o desenvolvimento, foram aplicados conceitos vitais de programação, incluindo:
* Estruturas de Dados complexas (**Listas, Tuplas e Dicionários**).
* **Controlo de Fluxo** (`if/else`, `for`, `while`).
* Tratamento de Erros e **Exceptions** (`try/except`).
* Criação e modularização de **Funções** e importação de módulos.

---

## ✨ Principais Funcionalidades e Estrutura

### ⚙️ Hub Central e Gestão de Dados
* **Ponto de Entrada (`main.py` & `menu.py`):** O sistema é iniciado através do `main.py`, que invoca o menu interativo.
* **Sistema de Placar Global (`placar.py`):** Um módulo dedicado exclusivamente a gerir o estado do jogador. Regista o total de partidas, soma os pontos de cada jogo em tempo real e gera relatórios detalhados e o ranking final ao encerrar a plataforma.

### 🕹️ Os Minijogos Disponíveis
* **🔤 Jogo da Forca (`forca.py`):** O clássico jogo de adivinhar a palavra, agora com categorias temáticas geradas aleatoriamente e controlo de vidas.
* **❌ Jogo da Velha (`velha.py`):** Partida tradicional de "X" contra "O", com renderização do tabuleiro e mapeamento de posições (0 a 8) no próprio terminal.
* **🧠 Quiz e Enigmas (`quiz_enigmas.py`):** Um jogo de trívia com perguntas gerais.
* **✂️ Pedra, Papel e Tesoura (`pedra_papel_tesoura.py`):** Traz opções de jogo contra o Computador (usando a biblioteca `random`) ou um modo multijogador local (Jogador 1 vs Jogador 2).
* **🔀 Palavra Embaralhada (`palavra_embaralhada.py`):** Sorteia e embaralha palavras de um banco de dados ligado à programação e tecnologia, dando ao jogador um limite de tentativas para acertar.

---

## 🚀 Instruções de Execução

**Pré-requisitos:**
* É necessário ter o **Python 3.11** instalado na sua máquina. O projeto utiliza apenas bibliotecas nativas (`random`, `os`), não sendo necessário instalar pacotes externos.

**Passo a Passo:**
1. Clone este repositório para o seu computador:
   ```bash
   git clone [https://github.com/misabm/python_arcade.git](https://github.com/misabm/python_arcade.git)

2. Acesse ao diretório do projeto:
    ```bash
    cd python_arcade

3. Execute o ficheiro principal da plataforma para iniciar o Arcade:
    ```bash
    python main.py

4. Insira o seu Nickname, escolha o seu jogo e divirta-se a acumular pontos!
