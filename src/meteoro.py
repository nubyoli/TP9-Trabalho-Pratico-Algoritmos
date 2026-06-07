""" Funções para cuidar dos meteoros: criação, movimentação, colisão e dano. Obstáculos do jogo"""

import pygame
import random
from src.config import LARGURA_TELA, ALTURA_TELA, METEORO_VELOCIDADE_MIN, METEORO_VELOCIDADE_MAX

def criar_meteoro(imagem):
    """Cria um meteoro com posição aleatória no topo da tela e velocidade aleatória."""
    meteoro_rect = imagem.get_rect()
    meteoro_rect.x = random.randint(0, LARGURA_TELA - meteoro_rect.width)
    meteoro_rect.y = random.randint(-150, -meteoro_rect.height)  # Começa acima da tela
    velocidade = random.randint(METEORO_VELOCIDADE_MIN, METEORO_VELOCIDADE_MAX)
    return {
        "imagem": imagem, 
        "rect": meteoro_rect, 
        "velocidade": velocidade
    }

def mover_meteoro(meteoro):
    """Move o meteoro para baixo com base em sua velocidade."""
    meteoro["rect"].y += meteoro["velocidade"]


def meteoro_saiu_da_tela(meteoro):
    """Retorna True se o meteoro ultrapassou a borda inferior."""
    return meteoro["rect"].top > ALTURA_TELA