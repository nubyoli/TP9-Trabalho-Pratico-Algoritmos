""" Funções responsáveis pela renderização dos elementos do jogo na tela """

import pygame
 
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    AMARELO,
    BRANCO,
    CIANO,
    CAMINHO_NAVE,
    CAMINHO_METEORO,
    CAMINHO_FUNDO,
    CAMINHO_VIDA,
    CAMINHO_ITEM,
    CAMINHO_ESTRELA_AMARELA,
    CAMINHO_ESTRELA_AZUL,
    NAVE_GRANDE_TAMANHO,
)
 
from src.estado import escudo_ativo

def renderizar_cena(tela, estado, fundo_img, recorde, fonte):
    """" Desenha os elementos do jogo, como a nave, meteoros, fundo, pontuação e recorde."""
    tela.blit(fundo_img, (0, 0))

    for meteoro in estado["meteoros"]:
        tela.blit(meteoro["imagem"], meteoro["rect"])

    for item in estado["itens"]:
        tela.blit(item["imagem"], item["rect"])

    tela.blit(estado["nave"]["imagem"], estado["nave"]["rect"])

    tempo_atual = pygame.time.get_ticks()
    if escudo_ativo(estado, tempo_atual):
        pygame.draw.circle(tela, (CIANO), estado["nave"]["rect"].center, max(estado["nave"]["rect"].width, estado["nave"]["rect"].height), 3)

    for i in range(estado["vidas"]):
        x = 10 + i * 38
        tela.blit(estado["vida_img"], (x, 10)) 

    texto_pontos = fonte.render(f"Pontos: {estado['pontos']}", True, (BRANCO))
    tela.blit(texto_pontos, (10, 50))

    texto_recorde = fonte.render(f"Recorde: {recorde}", True, (BRANCO))
    tela.blit(texto_recorde, (10, 80))

    texto_tempo = fonte.render(f"Tempo: {estado['segundos']}", True, (BRANCO))
    tela.blit(texto_tempo, (10, 110))

    if estado["mensagem_power"] and tempo_atual < estado["mensagem_ate_ms"]:
        texto_power = fonte.render(estado["mensagem_power"].capitalize(), True, (AMARELO))
        tela.blit(texto_power, (LARGURA_TELA // 2 - texto_power.get_width() // 2, 10))

def carrega_imagens():
    """" Carrega as imagens da nave e do meteoro usando os caminhos definidos em config.py. """

    nave_img = pygame.image.load(CAMINHO_NAVE).convert_alpha()
    meteoro_img = pygame.image.load(CAMINHO_METEORO).convert_alpha()
    fundo_img = pygame.image.load(CAMINHO_FUNDO).convert_alpha()
    vida_img = pygame.image.load(CAMINHO_VIDA).convert_alpha()
    item_img = pygame.image.load(CAMINHO_ITEM).convert_alpha()
    estrela_amarela_img = pygame.image.load(CAMINHO_ESTRELA_AMARELA).convert_alpha()
    estrela_azul_img = pygame.image.load(CAMINHO_ESTRELA_AZUL).convert_alpha()

    nave_img = pygame.transform.scale(nave_img, (50, 50))
    nave_grande_img = pygame.transform.scale(nave_img, NAVE_GRANDE_TAMANHO)
    meteoro_img = pygame.transform.scale(meteoro_img, (50, 50))
    fundo_img = pygame.transform.scale(fundo_img, (LARGURA_TELA, ALTURA_TELA)) # Para ocupar toda a tela
    vida_img = pygame.transform.scale(vida_img, (30, 30))
    item_img = pygame.transform.scale(item_img, (50, 50))
    estrela_amarela_img = pygame.transform.scale(estrela_amarela_img, (40, 40))
    estrela_azul_img = pygame.transform.scale(estrela_azul_img, (60, 60))

    return nave_img, nave_grande_img, meteoro_img, fundo_img, vida_img, item_img, estrela_amarela_img, estrela_azul_img

def renderizar_game_over(tela, fundo_img, fonte, pontos, segundos, bateu_recorde, recorde):
    """Desenha a tela final quando o jogador perde."""
    tela.blit(fundo_img, (0, 0))

    if bateu_recorde:
        mensagem_recorde = "Novo recorde! {recorde} pontos".format(recorde=pontos)
    else:        
        mensagem_recorde = "Seu recorde anterior não foi superado, tente novamente!"

    texto_perdeu = fonte.render("Voce perdeu!", True, BRANCO)
    texto_recorde = fonte.render(mensagem_recorde, True, AMARELO)
    texto_tempo = fonte.render(f"Tempo: {segundos}s", True, BRANCO)
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)

    tela.blit(texto_perdeu, (
        LARGURA_TELA // 2 - texto_perdeu.get_width() // 2,
        210
    ))

    tela.blit(texto_recorde, (
        LARGURA_TELA // 2 - texto_recorde.get_width() // 2,
        255
    ))

    tela.blit(texto_tempo, (
        LARGURA_TELA // 2 - texto_tempo.get_width() // 2,
        305
    ))

    tela.blit(texto_pontos, (
        LARGURA_TELA // 2 - texto_pontos.get_width() // 2,
        345
    ))

    pygame.display.flip()

    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                aguardando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                aguardando = False

        pygame.time.wait(50)

    