from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor

import pygame

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    separar_inimigos,
    spawnar_inimigo_na_borda,
    tomar_dano,
    verificar_colisao,
)

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_tomar_dano_reduz_vida():
    """Deve reduzir a vida atual de acordo com o dano recebido."""
    assert tomar_dano(3, 1) == 2

def test_jogador_perdeu_com_vidas_negativas():
    """Deve indicar derrota caso a vida fique abaixo de zero."""
    assert jogador_perdeu(-1) is True