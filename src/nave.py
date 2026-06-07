import pygame
from src.config import LARGURA_TELA, ALTURA_TELA
from src.funcoes import limitar_valor

def mover_nave(nave_rect, teclas, velocidade):
    """Move a nave com base nas teclas pressionadas (setas ou letras wasd) e limita dentro da tela. COntrole da movimentação do jogador"""
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:  # Suporte para setas e WASD
        nave_rect.x -= velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        nave_rect.x += velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        nave_rect.y -= velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        nave_rect.y += velocidade

    # Limitando a nave dentro das bordas da tela usando as propriedades do Rect
    nave_rect.x = limitar_valor(nave_rect.x, 0, LARGURA_TELA - nave_rect.width)
    nave_rect.y = limitar_valor(nave_rect.y, 0, ALTURA_TELA - nave_rect.height)