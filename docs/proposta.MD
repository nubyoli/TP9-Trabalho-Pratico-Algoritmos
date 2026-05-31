# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- [Aiandra de Sousa Silva](https://github.com/aiandramoraes)
- [Gabriel Vinícius Soares Doti](https://github.com/GabrielDoti)
- [Núbia Torres de Oliveira](https://github.com/nubyoli)


## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Nave desviando de meteoros.

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> O jogo se passa no espaço, onde o jogador controla uma nave e deve desviar de meteoros que surgem aleatoriamente na tela. Durante a partida, os obstáculos aparecem em diferentes posições, exigindo atenção e reflexos rápidos. A cada colisão, a nave perde uma vida, e o jogo termina quando as três vidas são esgotadas. O desafio é sobreviver pelo maior tempo possível, superando o próprio recorde e alcançando uma pontuação cada vez maior.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Sobreviver pelo maior tempo possível controlando uma nave espacial e desviando dos meteoros que surgem aleatoriamente na tela. Quanto mais tempo o jogador permanecer sem perder todas as suas vidas, maior será sua pontuação e a chance de superar o recorde anterior.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O jogador começa o jogo com 3 vidas.
- Regra 2: Cada colisão com um meteoro reduz 1 vida do jogador.
- Regra 3: Se o jogador zerar as vidas o jogo é encerrado. 
- Regra 4: O tempo de sobrevivência é utilizado como pontuação do jogador.
- Regra 5: O jogador pode controlar a nave movimentando-a para cima, para baixo, para a esquerda e para a direita.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> Sobreviver pelo maior tempo possível.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> O jogador é derrotado quanto perde todas as 3 vidas.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Uma nave espacial controlada pelas setas do teclado.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Meteoros aparecem aleatoriamente e devem ser evitados pelo jogador para que este não perca suas vidas.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Escreva aqui.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa com 3 vidas e o tempo decorrido de jogo é exibido na tela, para mostrar o progresso.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> - main.py: inicia o jogo, carrega as configurações principais e chama a execução da partida;
- src/jogo.py: contém o loop principal do jogo, controlando eventos, atualização da tela, colisões, vidas e encerramento da partida;
- src/config.py: guarda configurações gerais, como largura e altura da tela e cores;
- src/nave.py: contém funções relacionadas à nave do jogador, como movimentação e desenho na tela;
- src/meteoro.py: contém a criação, movimentação e posicionamento dos meteoros que aparecem aleatoriamente;
- src/funcoes.py: contém funções auxiliares, como exibir textos na tela, verificar colisões e reiniciar a partida;
- src/dados.py: contém funções de leitura e escrita de arquivos, salvando o tempo decorrido (e/ou sistema de pontuação se implementado) da partida para registrar a pontuação ou recorde do jogador;
- assets/: armazena imagens, sons e outros recursos usados no jogo.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> - Imagens: obtidas de bancos os sites de assets, para o background, nave, meteoros e vidas.
- Sons: obtidos de sites, para trilha do jogo e sons de colisão.
- Fonte: personalizada no estilo pixel.
- Tutorial: referência base.

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Detectar colisão entre os objetos.
- Dificuldade 2: Testes.
- Dificuldade 3: Criação de um sistema de pontuação.
- Dificuldade 4: Exibição do score baseado no tempo salvo no arquivo.
- Dificuldade 5: Controlar o surgimento aleatório e a movimentação dos meteoros na tela.
- Dificuldade 6: Implementar a tela de fim de jogo e a opção de reiniciar a partida.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá uma nave controlada pelo teclado, meteoros surgindo aleatoriamente na tela, sistema de colisão, sistema de vidas, contagem do tempo de sobrevivência como pontuação, exibição da pontuação na tela, salvamento do recorde em arquivo e tela de fim de jogo quando o jogador perder todas as vidas.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Criação de uma tela inicial de menu, que da a opção de iniciar o jogo ou ver uma tela de tutorial (sobre a movimentação e objetivo do jogo).
- Melhoria 2: Implementação de power up para a nave, como elemento de escudo que dura por determinado período e ignora colisões.
- Melhoria 3: Implementação de ação da nave com os meteoros, como balas para atirar e eliminar os obstaculos. 
- Melhoria 4: Menu de pausa.
- Melhoria 5: Aumento de dificuldade, para no decorrer do tempo aumentar a velocidade e/ou a quantidade de obstáculos na tela. 
