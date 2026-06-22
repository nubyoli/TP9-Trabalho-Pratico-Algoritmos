import pygame
import random

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CAMINHO_RECORDE,
    NAVE_VELOCIDADE,
    PONTOS_POR_SEGUNDO,
    METEORO_INTERVALO_MS,
    CAMINHO_FONTE,
    POWER_ITEM_ITERVALO_MS,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.dados import salvar_recorde, carregar_recorde
from src.meteoro import criar_meteoro, mover_meteoro, meteoro_saiu_da_tela
from src.nave import mover_nave
from src.item import criar_item, mover_item, item_saiu_da_tela, sortear_efeito
from src.tela import renderizar_cena, carrega_imagens, renderizar_game_over
from src.estado import escudo_ativo, nave_grande_ativa, remover_power, aplicar_power, atualiza_estado
   
def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    fonte = pygame.font.Font(CAMINHO_FONTE, 24)

    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens 
    nave_img, nave_grande_img, meteoro_img, fundo_img, vida_img, item_img, estrela_amarela_img, estrela_azul_img = carrega_imagens()

    recorde = carregar_recorde(CAMINHO_RECORDE)
    estado = atualiza_estado(nave_img, nave_grande_img, meteoro_img, vida_img, item_img, estrela_amarela_img, estrela_azul_img)

    #  VARIÁVEIS DE CONTROLE 
    estrelas = []
    item_vida_rara = None
    tempo_inicial_partida = pygame.time.get_ticks()
    ultimo_tempo_combo = pygame.time.get_ticks()
    turbo_ativo = False
    tempo_inicio_turbo = 0
    velocidade_atual_nave = NAVE_VELOCIDADE

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        dt = relogio.tick(FPS) 
        tempo_atual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                
                # MECÂNICA DO TURBO: Ativa ao apertar Shift Esquerdo
                if evento.key == pygame.K_LSHIFT and not turbo_ativo:
                    turbo_ativo = True
                    tempo_inicio_turbo = tempo_atual
                    velocidade_atual_nave = NAVE_VELOCIDADE * 2.0

        # Controla a duração do turbo (desliga após 2 segundos)
        if turbo_ativo and tempo_atual - tempo_inicio_turbo > 2000:
            turbo_ativo = False
            velocidade_atual_nave = NAVE_VELOCIDADE

        # Movimentação usando a velocidade corrigida
        teclas = pygame.key.get_pressed()
        remover_power(estado, tempo_atual)
        
        mover_nave(estado["nave"]["rect"], teclas, velocidade_atual_nave)

        # Garante que a nave não saia dos limites da tela
        estado["nave"]["rect"].x = limitar_valor(estado["nave"]["rect"].x, 0, LARGURA_TELA - estado["nave"]["rect"].width)
        estado["nave"]["rect"].y = limitar_valor(estado["nave"]["rect"].y, 0, ALTURA_TELA - estado["nave"]["rect"].height)

        # A cada segundo a pontuação do jogador vai incrementar em 10 pontos
        estado["ms_acumulados"] += dt
        if estado["ms_acumulados"] >= 1000:
            estado["pontos"] = calcular_pontos(estado["pontos"], PONTOS_POR_SEGUNDO)
            estado["ms_acumulados"] -= 1000
            estado["segundos"] += 1

        # Gerar mais meteoros a cada intervalo definido
        estado["ms_meteoros"] += dt
        if estado["ms_meteoros"] >= METEORO_INTERVALO_MS:
            estado["meteoros"].append(criar_meteoro(meteoro_img))
            estado["ms_meteoros"] -= METEORO_INTERVALO_MS

        # Movimento dos meteoros
        novos = []
        for meteoro in estado["meteoros"]:
            mover_meteoro(meteoro)
            if meteoro_saiu_da_tela(meteoro):
                novos.append(criar_meteoro(estado["meteoro_img"]))
            else:
                novos.append(meteoro)
        estado["meteoros"] = novos

        # Verificar colisões entre a nave e os meteoros
        for meteoro in estado["meteoros"]:
            if verificar_colisao(estado["nave"]["rect"], meteoro["rect"]):
                if not escudo_ativo(estado, tempo_atual):
                    estado["vidas"] = tomar_dano(estado["vidas"], 1)
                
                estado["meteoros"].remove(meteoro)
                estado["meteoros"].append(criar_meteoro(estado["meteoro_img"]))
                break

        # Gerar os powers surpresa e verificar a colisão da nave com esse item para aplicar o efeito sorteado
        estado["ms_itens"] += dt
        if estado["ms_itens"] >= POWER_ITEM_ITERVALO_MS:
            estado["itens"].append(criar_item(item_img))
            estado["ms_itens"] -= POWER_ITEM_ITERVALO_MS

        novos_itens = []
        for item in estado["itens"]:
            mover_item(item)
            if verificar_colisao(estado["nave"]["rect"], item["rect"]):
                estado["mensagem_power"] = sortear_efeito()
                estado["mensagem_ate_ms"] = tempo_atual + 2000
                aplicar_power(estado, tempo_atual)
            elif not item_saiu_da_tela(item):
                novos_itens.append(item)
        estado["itens"] = novos_itens


        # PROGRESSÃO DE DIFICULDADE: A quantidade de estrelas aumenta com a pontuação
        # Começa em 200 (raro) e vai diminuindo até o limite de 40 (muito frequente)
        chance_atual = max(40, 200 - (estado["pontos"] // 25))

        # MECÂNICA DAS ESTRELAS 
        if random.randint(1, chance_atual) == 1:
            # 35% de chance de nascer uma estrela marrom perigosa
            cor_estrela = "marrom" if random.randint(1, 10) <= 3 else "amarela"
            estrelas.append({
                "rect": pygame.Rect(random.randint(0, LARGURA_TELA - 20), -20, 20, 20),
                "velocidade": random.randint(3, 6),
                "tipo": cor_estrela,
                "imagem": estrela_amarela_img if cor_estrela == "amarela" else estrela_azul_img
            })
        
        bateu_recorde = estado["pontos"] > recorde

        for estrela in estrelas[:]:
            estrela["rect"].y += estrela["velocidade"]
            if estado["nave"]["rect"].colliderect(estrela["rect"]):
                # Fim do jogo se coletar estrela marrom
                if estrela.get("tipo") == "marrom":
                    pygame.display.flip()
                    pygame.time.wait(400)
                    
                    if bateu_recorde:
                        salvar_recorde(CAMINHO_RECORDE, estado["pontos"])
                    rodando = False
                    break
                else:
                    # Estrela amarela normal  dá exatamente 100 pontos
                    estado["pontos"] += 100
                estrelas.remove(estrela)
            elif estrela["rect"].y > ALTURA_TELA:
                estrelas.remove(estrela)

        if not rodando:
            break

        # MECÂNICA DA VIDA EXTRA RARA
        if item_vida_rara is None and random.randint(1, 1500) == 777:
            item_vida_rara = pygame.Rect(random.randint(40, LARGURA_TELA - 40), random.randint(40, ALTURA_TELA - 40), 30, 30)
        
        if item_vida_rara is not None:
            if estado["nave"]["rect"].colliderect(item_vida_rara):
                if estado["vidas"] < 5:
                    estado["vidas"] += 1
                item_vida_rara = None

        # Renderização customizada para desenhar seus elementos na tela
        renderizar_cena(tela, estado, fundo_img, recorde, fonte)
        
        # Desenha as estrelas na tela (Amarela dá pontos, Marrom mata)
        for estrela in estrelas:
            tela.blit(estrela["imagem"], estrela["rect"])
        
        # Desenha o coração da vida extra se ele existir
        if item_vida_rara is not None:
            tela.blit(vida_img, (item_vida_rara.x, item_vida_rara.y))

        # Encerra o jogo quando o jogador perde normalmente por vidas
        if jogador_perdeu(estado["vidas"]):                                             
            if bateu_recorde:
                salvar_recorde(CAMINHO_RECORDE, estado["pontos"])
            renderizar_game_over(tela, fundo_img, fonte, estado["pontos"], estado["segundos"], bateu_recorde, recorde)
            rodando = False

        pygame.display.flip()
        

    pygame.quit()