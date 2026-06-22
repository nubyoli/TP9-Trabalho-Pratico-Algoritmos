# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Star Storm

## 2. Integrantes do grupo

- [Aiandra de Sousa Silva](https://github.com/aiandramoraes)
- [Gabriel Vinícius Soares Doti](https://github.com/GabrielDoti)
- [Núbia Torres de Oliveira](https://github.com/nubyoli)


## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Nave desviando de meteoros.

## 4. Descrição geral do jogo

Descrição:

> O jogo se passa no espaço, onde o jogador controla uma nave e deve desviar de meteoros que surgem aleatoriamente na tela. Durante a partida, os obstáculos aparecem em diferentes posições, exigindo atenção e reflexos rápidos. A cada colisão, a nave perde uma vida, e o jogo termina quando as três vidas são esgotadas. O desafio é sobreviver pelo maior tempo possível, superando o próprio recorde e alcançando uma pontuação cada vez maior. A cada segundo, são somados 10 pontos ao jogador. Além disso, itens coletáveis aparecem na tela, sendo 2 tipos de estrela, se o jogador coletar uma estrela amarela, ele soma 100 pontos, mas, se coletar a estrela azul ele perde o jogo na hora. São lançados aleatóriamente elementos de power para o jogador coletar, no entanto, existem duas opções: um power up, em que o jogador ganha um escudo de proteção por 6 segundos, assim sua colisão com os meteoros não o faz perder vidas, e um power down, que aumenta o tamanho da nave, dificultando o desvio dos elementos. 

## 5. Objetivo do jogador

Objetivo:

> Sobreviver pelo maior tempo possível controlando uma nave espacial e desviando dos meteoros que surgem aleatoriamente na tela. Quanto mais tempo o jogador permanecer sem perder todas as suas vidas, maior será sua pontuação e a chance de superar o recorde anterior.

## 6. Regras principais

Regras do grupo:

- Regra 1: O jogador começa o jogo com 3 vidas.
- Regra 2: Cada colisão com um meteoro reduz 1 vida do jogador.
- Regra 3: Se o jogador zerar as vidas o jogo é encerrado. 
- Regra 4: A cada segundo sobrevivido são somados 10 pontos ao jogador.
- Regra 5: O jogador pode controlar a nave movimentando-a para cima, para baixo, para a esquerda e para a direita.
- Regra 6: Ao coletar uma estrela amarela 100 pontos são somados ao jogador.
- Regra 7: Ao coletar uma estrela azul o jogo é encerrado.
- Regra 8: Ao coletar o elemento de power o jogador pode receber um power up (escudo) ou power down (aumento da nave).

## 7. Condição de vitória

Condição de vitória:

> Sobreviver pelo maior tempo possível.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> O jogador é derrotado quanto perde todas as 3 vidas ou coleta uma estrela azul.

## 9. Elementos previstos no jogo

Descrição:

> Uma nave espacial controlada pelas setas do teclado.

## Obstáculos, inimigos ou desafios

Descrição:

> Meteoros aparecem aleatoriamente e devem ser evitados pelo jogador para que este não perca suas vidas.

## Itens, alvos ou objetos de interação

Descrição:

> Estrelas amarelas aparecem na tela e aumentam a pontuação do jogador. Estrelas azul encerram o jogo. Elementos de power podem ajudar ou atrapalhar o jogador.

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador começa com 3 vidas e o tempo decorrido de jogo e a pontuação são exibidos na tela, para mostrar o progresso.

## 10. Controles previstos

Controles do grupo:

- Seta para cima (ou W): mover para cima
- Seta para baixo (ou S): mover para baixo
- Seta para esquerda (ou A): mover para esquerda
- Seta para direita (ou D): mover para direita

## 11. Organização inicial do código

Organização planejada:

- `main.py`: inicia o jogo;
- `src/jogo.py`: loop principal.
- `src/estado.py`: trata do estado do jogo e suas atualizações.
- `src/tela.py`: renderização dos elementos do jogo.
- `src/item.py`: trata dos powers aleatórios gerados no jogo.
- `src/nave.py`: movimentação da nave do jogador.
- `src/meteoro.py`: criação e movimentação dos meteoros.
- `src/config.py`: constantes globais (tela, cores, caminhos, FPS).
- `src/funcoes.py`: funções auxiliares de regra e lógica.
- `src/dados.py`: leitura e gravação de dados (recorde/ranking).


## 12. Recursos externos previstos

Recursos previstos:

> - Imagens: obtidas de bancos os sites de assets, para o background, nave, meteoros e vidas.
- Sons: obtidos de sites, para trilha do jogo e sons de colisão.
- Fonte: personalizada no estilo pixel. (link: [Fonte Pixel](https://www.dafont.com/pt/upheaval.font))
- Nave: sprite link: [Sprite Nave](https://opengameart.org/content/spaceships-32x32)
- Estrelas: [Sprite Estrela Amarela](https://opengameart.org/content/star-svg) [Sprite Estrela Azul](https://opengameart.org/content/star)
- Tutorial: referência base.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Detectar colisão entre os objetos.
- Dificuldade 2: Testes.
- Dificuldade 3: Criação de um sistema de pontuação.
- Dificuldade 4: Exibição do score baseado no tempo salvo no arquivo.
- Dificuldade 5: Controlar o surgimento aleatório e a movimentação dos meteoros na tela.
- Dificuldade 6: Implementar a tela de fim de jogo e a opção de reiniciar a partida.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá uma nave controlada pelo teclado, meteoros surgindo aleatoriamente na tela, sistema de colisão, sistema de vidas, contagem do tempo de sobrevivência como pontuação, exibição da pontuação na tela, salvamento do recorde em arquivo e tela de fim de jogo quando o jogador perder todas as vidas.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Criação de uma tela inicial de menu, que da a opção de iniciar o jogo ou ver uma tela de tutorial (sobre a movimentação e objetivo do jogo).
- Melhoria 2: Implementação de power up para a nave, como elemento de escudo que dura por determinado período e ignora colisões.
- Melhoria 3: Implementação de ação da nave com os meteoros, como balas para atirar e eliminar os obstaculos. 
- Melhoria 4: Aumento de dificuldade, para no decorrer do tempo aumentar a velocidade e/ou a quantidade de obstáculos na tela. 
