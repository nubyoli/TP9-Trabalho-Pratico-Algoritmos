import math
import random
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
    METEORO_QTD_INICIAL,
    CAMINHO_VIDA,
    DURACAO_ESCUDO,
    DURACAO_NAVE_GRANDE,
    NAVE_GRANDE_TAMANHO,
    CAMINHO_ITEM,
    CAMINHO_ESTRELA_AZUL,
    CAMINHO_ESTRELA_AMARELA
)

from src.meteoro import criar_meteoro, mover_meteoro, meteoro_saiu_da_tela

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def separar_inimigos(inimigos, distancia_minima=60):
    """Empurra inimigos que estão sobrepostos para longe um do outro."""
    for i in range(len(inimigos)):
        for j in range(i + 1, len(inimigos)):
            a = inimigos[i]["rect"]
            b = inimigos[j]["rect"]

            dx = a.centerx - b.centerx
            dy = a.centery - b.centery
            distancia = math.hypot(dx, dy)

            if 0 < distancia < distancia_minima:
                empurrao = (distancia_minima - distancia) / 2
                fator_x = (dx / distancia) * empurrao
                fator_y = (dy / distancia) * empurrao

                a.x += int(fator_x)
                a.y += int(fator_y)
                b.x -= int(fator_x)
                b.y -= int(fator_y)


def spawnar_inimigo_na_borda(largura_tela, altura_tela):
    """Retorna uma posição aleatória fora de uma das quatro bordas da tela."""
    borda = random.choice(["cima", "baixo", "esquerda", "direita"])

    if borda == "cima":
        return random.randint(0, largura_tela), -50
    elif borda == "baixo":
        return random.randint(0, largura_tela), altura_tela + 50
    elif borda == "esquerda":
        return -50, random.randint(0, altura_tela)
    else:
        return largura_tela + 50, random.randint(0, altura_tela)
    

def spawnar_meteoro(largura_tela, altura_tela, vel_min=2, vel_max=5):
    """Cria um meteoro numa borda aleatória com velocidade e direção fixas."""
    borda = random.choice(["cima", "baixo", "esquerda", "direita"])

    if borda == "cima":
        x = random.randint(0, largura_tela)
        y = -50
        vx = random.uniform(-1.5, 1.5)
        vy = random.uniform(vel_min, vel_max)
    elif borda == "baixo":
        x = random.randint(0, largura_tela)
        y = altura_tela + 50
        vx = random.uniform(-1.5, 1.5)
        vy = -random.uniform(vel_min, vel_max)
    elif borda == "esquerda":
        x = -50
        y = random.randint(0, altura_tela)
        vx = random.uniform(vel_min, vel_max)
        vy = random.uniform(-1.5, 1.5)
    else:
        x = largura_tela + 50
        y = random.randint(0, altura_tela)
        vx = -random.uniform(vel_min, vel_max)
        vy = random.uniform(-1.5, 1.5)

    return x, y, vx, vy      
 