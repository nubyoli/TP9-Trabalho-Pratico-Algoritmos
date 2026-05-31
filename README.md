# Star Storm

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- [Aiandra de Sousa Silva](https://github.com/aiandramoraes)
- [Gabriel Vinícius Soares Doti](https://github.com/GabrielDoti)
- [Núbia Torres de Oliveira](https://github.com/nubyoli)

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

O jogo consiste em controlar uma nave no espaço que deve desviar de meteóros. Esses elementos aparecerão aleatoriamente na jornada do jogador e a cada colisão o personagem pede uma vida. O jogo acaba quando todas as 3 vidas forem perdidas. Ao final é exibido o tempo máximo do jogador desviando dos meteóros, se ele superar o tempo anterior seu novo score é exibido.  


## Objetivo do jogador

O objetivo é desviar dos obstáculos que apareceram aleatoriamente, fazendo isso pelo maior tempo possível.


## Regras do jogo

Liste as principais regras do jogo.

Exemplo:

- O jogador se movimenta usando as setas do teclado.
- Colidir com um obstáculo reduz a quantidade de vidas.
- A partida termina quando o jogador perde todas as vidas.

## Controles

Informe as teclas ou comandos utilizados no jogo.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
