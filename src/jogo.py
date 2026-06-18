import pygame

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
    
    # nave = {
    #     "imagem": nave_img,
    #     "rect": nave_img.get_rect(topleft=(100, 100))
    # }

    # meteoro = {
    #     "imagem": meteoro_img,
    #     "rect": meteoro_img.get_rect(topleft=(500, 300))
    # }
    
    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        dt = relogio.tick(FPS) 

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        teclas = pygame.key.get_pressed()
        mover_nave(estado["nave"]["rect"], teclas, NAVE_VELOCIDADE)

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
                estado["vidas"] = tomar_dano(estado["vidas"], 1)
                estado["meteoros"].remove(meteoro)
                estado["meteoros"].append(criar_meteoro(estado["meteoro_img"]))
                break

        # Encerra o jogo quando o jogador perde
        if jogador_perdeu(estado["vidas"]):                                             
            if estado["pontos"] > recorde:
                salvar_recorde(CAMINHO_RECORDE, estado["pontos"])
            rodando = False

        
        renderizar_cena(tela, estado, fundo_img, recorde, fonte)
        pygame.display.flip()

    pygame.quit()