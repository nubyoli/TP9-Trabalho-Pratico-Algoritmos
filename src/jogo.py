import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    AMARELO,
    BRANCO,
    CIANO,
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
    CAMINHO_FONTE,
    POWER_ITEM_ITERVALO_MS,
    POWER_ITEM_VELOCIDADE_MIN,
    POWER_ITEM_VELOCIDADE_MAX,
    DURACAO_ESCUDO,
    DURACAO_NAVE_GRANDE,
    NAVE_GRANDE_TAMANHO,
    CAMINHO_ITEM
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

from src.item import criar_item, mover_item, item_saiu_da_tela, sortear_efeito

def carrega_imagens():
    """" Carrega as imagens da nave e do meteoro usando os caminhos definidos em config.py. """

    nave_img = pygame.image.load(CAMINHO_NAVE).convert_alpha()
    meteoro_img = pygame.image.load(CAMINHO_METEORO).convert_alpha()
    fundo_img = pygame.image.load(CAMINHO_FUNDO).convert_alpha()
    vida_img = pygame.image.load(CAMINHO_VIDA).convert_alpha()
    item_img = pygame.image.load(CAMINHO_ITEM).convert_alpha()

    nave_img = pygame.transform.scale(nave_img, (50, 50))
    nave_grande_img = pygame.transform.scale(nave_img, NAVE_GRANDE_TAMANHO)
    meteoro_img = pygame.transform.scale(meteoro_img, (50, 50))
    fundo_img = pygame.transform.scale(fundo_img, (LARGURA_TELA, ALTURA_TELA)) # Para ocupar toda a tela
    vida_img = pygame.transform.scale(vida_img, (30, 30))
    item_img = pygame.transform.scale(item_img, (30, 30))

    return nave_img, nave_grande_img, meteoro_img, fundo_img, vida_img, item_img

def atualiza_estado(nave_img, nave_grande_img, meteoro_img, vida_img, item_img):
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
        "mensagem_ate_ms": 0
    }

def escudo_ativo(estado, agora_ms):
    """ Verifica se o escudo está ativo, comparando o tempo atual com o tempo de término do escudo. """
    return agora_ms < estado["escudo_ate_ms"]

def nave_grande_ativa(estado, agora_ms):
    """ Verifica se a nave grande está ativa, comparando o tempo atual com o tempo de término da nave grande. """
    return agora_ms < estado["nave_grande_ate_ms"]

def aumentar_tamanho_nave(estado, imagem):
    """ Atualiza o tamnho da nave para ela ficar maior e o jogador ter mais dificuldade para desviar dos meteoros. """
    centro = estado["nave"]["rect"].center
    estado["nave"]["imagem"] = imagem
    estado["nave"]["rect"] = estado["nave"]["imagem"].get_rect(center=centro)
    estado["nave"]["rect"].x = limitar_valor(estado["nave"]["rect"].x, 0, LARGURA_TELA - estado["nave"]["rect"].width)
    estado["nave"]["rect"].y = limitar_valor(estado["nave"]["rect"].y, 0, ALTURA_TELA - estado["nave"]["rect"].height)

def aplicar_power(estado, agora_ms):
    """ Aplica o power de acordo com o efeito sorteado na função do item """
    if estado["mensagem_power"] == "escudo":
        estado["escudo_ate_ms"] = agora_ms + DURACAO_ESCUDO
    elif estado["mensagem_power"] == "nave_grande":
        estado["nave_grande_ate_ms"] = agora_ms + DURACAO_NAVE_GRANDE
        aumentar_tamanho_nave(estado, estado["nave"]["imagem_grande"])

def remover_power(estado, agora_ms):
    """ Remove o efeito do power up ou power down, voltando a nave ao estado normal. """
    if not nave_grande_ativa(estado, agora_ms):
        if estado["nave"]["imagem"] == estado["nave"]["imagem_grande"]:
            aumentar_tamanho_nave(estado, estado["nave"]["imagem_normal"])

def renderizar_cena(tela, estado, fundo_img, recorde, fonte):
    """" Desenha os elementos do jogo, como a nave, meteoros, fundo, pontuação e recorde."""
    tela.blit(fundo_img, (0, 0))

    for meteoro in estado["meteoros"]:
        tela.blit(meteoro["imagem"], meteoro["rect"])

    for item in estado["itens"]:
        tela.blit(item["imagem"], item["rect"])

    tela.blit(estado["nave"]["imagem"], estado["nave"]["rect"])

    agora_ms = pygame.time.get_ticks()
    if escudo_ativo(estado, agora_ms):
        pygame.draw.circle(tela, (CIANO), estado["nave"]["rect"].center, max(estado["nave"]["rect"].width, estado["nave"]["rect"].height), 3)

    for i in range(estado["vidas"]):
        x = 10 + i * 38
        tela.blit(estado["vida_img"], (x, 10)) 

    texto_pontos = fonte.render(f"Pontos: {estado['pontos']}", True, (BRANCO))
    tela.blit(texto_pontos, (10, 50))

    texto_recorde = fonte.render(f"Recorde: {recorde}", True, (BRANCO))
    tela.blit(texto_recorde, (10, 80))

    if estado["mensagem_power"] and agora_ms < estado["mensagem_ate_ms"]:
        texto_power = fonte.render(estado["mensagem_power"].capitalize(), True, (AMARELO))
        tela.blit(texto_power, (LARGURA_TELA // 2 - texto_power.get_width() // 2, 10))
    

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    fonte = pygame.font.Font(CAMINHO_FONTE, 24)

    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens 
    nave_img, nave_grande_img, meteoro_img, fundo_img, vida_img, item_img = carrega_imagens()

    recorde = carregar_recorde(CAMINHO_RECORDE)
    estado = atualiza_estado(nave_img, nave_grande_img, meteoro_img, vida_img, item_img)
    
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
        agora_ms = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        teclas = pygame.key.get_pressed()
        remover_power(estado, agora_ms)
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
                if not escudo_ativo(estado, agora_ms):
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
                estado["mensagem_ate_ms"] = agora_ms + 2000
                aplicar_power(estado, agora_ms)
            elif not item_saiu_da_tela(item):
                novos_itens.append(item)
        estado["itens"] = novos_itens


        # Encerra o jogo quando o jogador perde
        if jogador_perdeu(estado["vidas"]):                                             
            if estado["pontos"] > recorde:
                salvar_recorde(CAMINHO_RECORDE, estado["pontos"])
            rodando = False

        
        renderizar_cena(tela, estado, fundo_img, recorde, fonte)
        pygame.display.flip()

    pygame.quit()