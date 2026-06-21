# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Star Storm"

# Cores
BRANCO = (255, 255, 255)
PRETO = (0,   0,   0  )
CINZA = (212, 212, 212)
VERMELHO = (220, 50,  50 )
AMARELO = (255, 220, 50 )
AZUL = (100, 180, 255)

# Arquivos
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"
CAMINHO_VIDA = "assets/imagens/Coracao.png"
CAMINHO_ITEM = "assets/imagens/item.png"

# Fonte externa da imagem: https://opengameart.org/content/spaceships-32x32
CAMINHO_NAVE = "assets/imagens/Ship_4.png"

CAMINHO_METEORO = "assets/imagens/meteoro.png"
CAMINHO_FUNDO = "assets/imagens/fundo.jpg"

# SIte da fonte externa: https://www.dafont.com/pt/upheaval.font
CAMINHO_FONTE = "assets/fontes/upheavtt.ttf"

# Nave do jogador
NAVE_VELOCIDADE  = 5

# Meteoros
METEORO_VELOCIDADE_MIN = 2
METEORO_VELOCIDADE_MAX = 5
METEORO_QTD_INICIAL = 4     
METEORO_INTERVALO_MS = 5000  

# Pontuação, a cada segundo incrementa 10
PONTOS_POR_SEGUNDO = 10

# Power up e power down
POWER_ITEM_ITERVALO_MS = 8000 
POWER_ITEM_VELOCIDADE_MIN = 3
POWER_ITEM_VELOCIDADE_MAX = 6
DURACAO_ESCUDO = 6000
DURACAO_NAVE_GRANDE = 6000
NAVE_GRANDE_TAMANHO = (70, 70)