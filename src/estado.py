""" Funções que tratam do estado do jogo, e suas mudanças ao longo do tempo"""

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    METEORO_QTD_INICIAL,
    DURACAO_ESCUDO,
    DURACAO_NAVE_GRANDE,
)
 
from src.meteoro import criar_meteoro
from src.funcoes import limitar_valor

def atualiza_estado(nave_img, nave_grande_img, meteoro_img, vida_img, item_img, estrela_amarela_img, estrela_azul_img):
    """"
    Cria e retorna um dicionário com o estado inicial do jogo.

    Essa função é chamada tanto no início da partida quanto ao reiniciar,
    garantindo que todos os valores voltem ao ponto de partida. Ela retorna um dicionário, contendo as informações relevantes para o jogo."""

    nave = {
        "imagem": nave_img,
        "imagem_normal": nave_img,
        "imagem_grande": nave_grande_img,
        "rect": nave_img.get_rect(midbottom=(LARGURA_TELA // 2, ALTURA_TELA - 20))
    }

    meteoros = []
    for i in range(METEORO_QTD_INICIAL):
        meteoros.append(criar_meteoro(meteoro_img))
    
    return {
        "nave": nave,
        "meteoros": meteoros,
        "meteoro_img": meteoro_img,
        "vida_img": vida_img,
        "pontos": 0,
        "vidas": 3,
        "segundos": 0,
        "ms_acumulados": 0,
        "ms_meteoros": 0,
        "itens": [],
        "item_img": item_img,
        "ms_itens": 0,
        "escudo_ate_ms": 0,
        "nave_grande_ate_ms": 0,
        "mensagem_power": "",
        "mensagem_ate_ms": 0,
        "estrela_amarela_img": estrela_amarela_img,
        "estrela_azul_img": estrela_azul_img
    }

def escudo_ativo(estado, tempo_atual):
    """ Verifica se o escudo está ativo, comparando o tempo atual com o tempo de término do escudo. """
    return tempo_atual < estado["escudo_ate_ms"]

def nave_grande_ativa(estado, tempo_atual):
    """ Verifica se a nave grande está ativa, comparando o tempo atual com o tempo de término da nave grande. """
    return tempo_atual < estado["nave_grande_ate_ms"]

def aumentar_tamanho_nave(estado, imagem):
    """ Atualiza o tamnho da nave para ela ficar maior e o jogador ter mais dificuldade para desviar dos meteoros. """
    centro = estado["nave"]["rect"].center
    estado["nave"]["imagem"] = imagem
    estado["nave"]["rect"] = estado["nave"]["imagem"].get_rect(center=centro)
    estado["nave"]["rect"].x = limitar_valor(estado["nave"]["rect"].x, 0, LARGURA_TELA - estado["nave"]["rect"].width)
    estado["nave"]["rect"].y = limitar_valor(estado["nave"]["rect"].y, 0, ALTURA_TELA - estado["nave"]["rect"].height)

def aplicar_power(estado, tempo_atual):
    """ Aplica o power de acordo com o efeito sorteado na função do item """
    if estado["mensagem_power"] == "escudo":
        estado["escudo_ate_ms"] = tempo_atual + DURACAO_ESCUDO
    elif estado["mensagem_power"] == "nave_grande":
        estado["nave_grande_ate_ms"] = tempo_atual + DURACAO_NAVE_GRANDE
        aumentar_tamanho_nave(estado, estado["nave"]["imagem_grande"])

def remover_power(estado, tempo_atual):
    """ Remove o efeito do power up ou power down, voltando a nave ao estado normal. """
    if not nave_grande_ativa(estado, tempo_atual):
        if estado["nave"]["imagem"] == estado["nave"]["imagem_grande"]:
            aumentar_tamanho_nave(estado, estado["nave"]["imagem_normal"])


