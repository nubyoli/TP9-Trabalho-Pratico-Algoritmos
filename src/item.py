""" Funções para power surpresa, power up ou power down, que aparecem aleatoriamente durante o jogo. """

import random
import pygame

from src.config import (
    POWER_ITEM_VELOCIDADE_MIN, 
    POWER_ITEM_VELOCIDADE_MAX,
    LARGURA_TELA,
    ALTURA_TELA)

def criar_item(imagem):
    """ Cria um item com posição e velocidade aleatórias. """

    item = {
        "imagem": imagem,
        "rect": imagem.get_rect(midbottom=(random.randint(20, LARGURA_TELA - 20), -20)),
        "velocidade": random.randint(POWER_ITEM_VELOCIDADE_MIN, POWER_ITEM_VELOCIDADE_MAX)
    }
    return item

def mover_item(item):
    """ Move o item para baixo, de acordo com sua velocidade. """
    item["rect"].y += item["velocidade"]

def item_saiu_da_tela(item):
    """ Verifica se o item saiu da tela (passou do limite inferior). """
    return item["rect"].top > ALTURA_TELA

def sortear_efeito():
    """ Sorteia um efeito aleatório para o item, que pode ser um power up ou power down. """
    efeitos = ["escudo", "nave_grande"]
    return random.choice(efeitos)
