# Pong com Pygame

Projeto desenvolvido para a disciplina de **Computação Gráfica e Tecnologias Imersivas** utilizando a biblioteca **Pygame** em Python.

O objetivo do projeto é implementar e evoluir um jogo clássico de **Pong**, aplicando conceitos de **refatoração de código, organização de classes, princípios SOLID e versionamento com Git**.

---

# Estrutura do Projeto

```
Pygame/
│
├── main.py
├── game.py
├── player.py
├── ball.py
├── config.py
│
└── assets/
    └── sounds/
        ├── bola.wav
        └── win.wav
```

Descrição dos arquivos:

* **main.py** → ponto de entrada do jogo
* **game.py** → lógica principal do jogo
* **player.py** → controle das raquetes
* **ball.py** → comportamento da bola
* **config.py** → constantes do jogo (cores, tamanho da tela, velocidade etc.)
* **assets/sounds** → arquivos de áudio utilizados no jogo

---

# Refatoração do Código

O projeto foi refatorado para melhorar:

* Organização do código
* Separação de responsabilidades
* Legibilidade
* Manutenção
* Escalabilidade

Cada elemento do jogo foi separado em **classes específicas**.

### Classes principais

**Game**
Responsável por controlar:

* Loop principal do jogo
* Atualização da lógica
* Renderização na tela
* Controle de pontuação
* Eventos de teclado

**Player**

Responsável pela raquete do jogador.

Funções principais:

* movimentação
* renderização na tela
* detecção de colisão

**Ball**

Responsável pelo comportamento da bola:

* movimento
* colisões
* reinício da posição após pontuação

---

# Task 1 — Feedback Sonoro e Áudio

Nesta etapa foi implementado um sistema de **feedback sonoro para melhorar a experiência do jogador**.

### Funcionalidades adicionadas

1. **Som de colisão**

Quando a bola colide com as raquetes, um efeito sonoro é reproduzido.

```
self.paddle_sound.play()
```

Isso melhora o feedback do jogador durante a gameplay.

---

2. **Som de pontuação**

Quando um jogador marca ponto, um som específico é executado.

```
self.score_sound.play()
```

Além disso, a bola é reiniciada no centro da tela.

---

3. **Carregamento dos sons**

Os efeitos sonoros são carregados utilizando o módulo **pygame.mixer**.

```
pygame.mixer.init()

self.paddle_sound = pygame.mixer.Sound("assets/sounds/bola.wav")
self.score_sound = pygame.mixer.Sound("assets/sounds/win.wav")
```

---

# Controle do Jogo

* **Seta para cima** → mover raquete para cima
* **Seta para baixo** → mover raquete para baixo
* **SPACE** → iniciar o jogo

---

# Princípios aplicados

Durante o refatoramento foram aplicados conceitos de **SOLID**, principalmente:

**Single Responsibility Principle**

Cada classe possui apenas uma responsabilidade:

* Game → controle do jogo
* Player → controle da raquete
* Ball → comportamento da bola

Isso torna o código mais organizado e fácil de manter.

---

# Tecnologias utilizadas

* Python
* Pygame
* Git
* GitHub

---

# Execução do Projeto

Para rodar o projeto:

```
python main.py
```

---

# Autor Victor Gustavo Jerba :D

Projeto desenvolvido como atividade acadêmica para a disciplina de **Computação Gráfica e Tecnologias Imersivas**.
