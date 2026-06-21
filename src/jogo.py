import pygame
import random

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    CAMINHO_NAVE,
    CAMINHO_METEORO,
    CAMINHO_FUNDO,
    METEORO_QTD_INICIAL,
    NAVE_VELOCIDADE,
    PONTOS_POR_SEGUNDO,
    METEORO_INTERVALO_MS,
    CAMINHO_VIDA,
    CAMINHO_FONTE
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

from src.meteoro import criar_meteoro, mover_meteoro, meteoro_saiu_da_tela
from src.nave import mover_nave

def carrega_imagens():
    """" Carrega as imagens da nave e do meteoro usando os caminhos definidos em config.py. """

    nave_img = pygame.image.load(CAMINHO_NAVE).convert_alpha()
    meteoro_img = pygame.image.load(CAMINHO_METEORO).convert_alpha()
    fundo_img = pygame.image.load(CAMINHO_FUNDO).convert_alpha()
    vida_img = pygame.image.load(CAMINHO_VIDA).convert_alpha()

    nave_img = pygame.transform.scale(nave_img, (50, 50))
    meteoro_img = pygame.transform.scale(meteoro_img, (50, 50))
    fundo_img = pygame.transform.scale(fundo_img, (LARGURA_TELA, ALTURA_TELA)) # Para ocupar toda a tela
    vida_img = pygame.transform.scale(vida_img, (30, 30))

    return nave_img, meteoro_img, fundo_img, vida_img

def atualiza_estado(nave_img, meteoro_img, vida_img):
    """"
    Cria e retorna um dicionário com o estado inicial do jogo.

    Essa função é chamada tanto no início da partida quanto ao reiniciar,
    garantindo que todos os valores voltem ao ponto de partida. Ela retorna um dicionário, contendo as informações relevantes para o jogo."""

    nave = {
        "imagem": nave_img,
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
        "ms_meteoros": 0
    }

def renderizar_cena(tela, estado, fundo_img, recorde, fonte):
    """" Desenha os elementos do jogo, como a nave, meteoros, fundo, pontuação e recorde."""
    tela.blit(fundo_img, (0, 0))

    for meteoro in estado["meteoros"]:
        tela.blit(meteoro["imagem"], meteoro["rect"])

    tela.blit(estado["nave"]["imagem"], estado["nave"]["rect"])

    for i in range(estado["vidas"]):
        x = 10 + i * 38
        tela.blit(estado["vida_img"], (x, 10)) 

    texto_pontos = fonte.render(f"Pontos: {estado['pontos']}", True, (255, 255, 255))
    tela.blit(texto_pontos, (10, 50))

    texto_recorde = fonte.render(f"Recorde: {recorde}", True, (255, 255, 255))
    tela.blit(texto_recorde, (10, 80))


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    fonte = pygame.font.Font(CAMINHO_FONTE, 24)

    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens 
    nave_img, meteoro_img, fundo_img, vida_img = carrega_imagens()

    recorde = carregar_recorde(CAMINHO_RECORDE)
    estado = atualiza_estado(nave_img, meteoro_img, vida_img)
    
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
        
        # Correção direta do movimento para garantir o funcionamento do Shift
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            estado["nave"]["rect"].x -= velocidade_atual_nave
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            estado["nave"]["rect"].x += velocidade_atual_nave
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            estado["nave"]["rect"].y -= velocidade_atual_nave
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            estado["nave"]["rect"].y += velocidade_atual_nave

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
                # INVENCIBILIDADE INICIAL: Só perde vida após 3 segundos de jogo
                if tempo_atual - tempo_inicial_partida > 3000:
                    estado["vidas"] = tomar_dano(estado["vidas"], 1)
                    ultimo_tempo_combo = tempo_atual  # Reseta o combo
                
                estado["meteoros"].remove(meteoro)
                estado["meteoros"].append(criar_meteoro(estado["meteoro_img"]))
                break

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
                "tipo": cor_estrela
            })
        
        for estrela in estrelas[:]:
            estrela["rect"].y += estrela["velocidade"]
            if estado["nave"]["rect"].colliderect(estrela["rect"]):
                # Se pegar a estrela MARROM... EXPLOSÃO e Fim de Jogo!
                if estrela.get("tipo") == "marrom":
                    pygame.draw.circle(tela, (244, 67, 54), estado["nave"]["rect"].center, 80)
                    pygame.display.flip()
                    pygame.time.wait(400)
                    
                    if estado["pontos"] > recorde:
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

        # MECÂNICA DE COMBO (Sobreviver 30 segundos)
        if tempo_atual - ultimo_tempo_combo >= 30000:
            estado["pontos"] += 500
            ultimo_tempo_combo = tempo_atual

        # Renderização customizada para desenhar seus elementos na tela
        renderizar_cena(tela, estado, fundo_img, recorde, fonte)
        
        # Desenha as estrelas na tela (Amarela dá pontos, Marrom mata)
        for estrela in estrelas:
            cor_rgb = (139, 69, 19) if estrela.get("tipo") == "marrom" else (255, 235, 59)
            pygame.draw.circle(tela, cor_rgb, estrela["rect"].center, 10)
        
        # Desenha o coração da vida extra se ele existir
        if item_vida_rara is not None:
            tela.blit(vida_img, (item_vida_rara.x, item_vida_rara.y))

        # Encerra o jogo quando o jogador perde normalmente por vidas
        if jogador_perdeu(estado["vidas"]):                                             
            if estado["pontos"] > recorde:
                salvar_recorde(CAMINHO_RECORDE, estado["pontos"])
            rodando = False

        pygame.display.flip()

    pygame.quit()