# import pygame, sys
# from pygame.locals import QUIT

# # Inicializa o Pygame
# pygame.init()

# # Criar a janela
# janela = pygame.display.set_mode([500, 500])
# pygame.display.set_caption('Ping Pong')

# # Cores
# BRANCO = (255, 255, 255)
# PRETO = (0, 0, 0)
# AZUL = (0, 0, 255)
# VERMELHO = (255, 0, 0)

# # Carregar as imagens
# # Para simplificar, estamos usando apenas retângulos coloridos para representar as raquetes e a bola

# raquete_img = pygame.Surface((10, 100))  # Criando uma raquete de 10x100 pixels
# raquete_img.fill(AZUL)  # Cor da raquete (azul)

# bola_img = pygame.Surface((20, 20))  # Criando a bola com 20x20 pixels
# bola_img.fill(VERMELHO)  # Cor da bola (vermelha)

# # Posições iniciais
# raquete1_x, raquete1_y = 50, 225
# raquete2_x, raquete2_y = 450, 225
# bola_x, bola_y = 250, 250

# # Velocidades
# velocidade_raquete = 5
# velocidade_bola_x, velocidade_bola_y = 3, 3

# # Tamanho da raquete (usando os valores definidos para a raquete)
# raquete_largura, raquete_altura = raquete_img.get_width(), raquete_img.get_height()

# # Pontuação inicial
# pontos_player1 = 0
# pontos_player2 = 0

# # Fonte para desenhar a pontuação
# fonte = pygame.font.SysFont('arial', 30)

# # Função para desenhar tudo
# def desenhar():
#     # Limpa a tela
#     janela.fill(BRANCO)

#     # Desenha as raquetes e a bola
#     janela.blit(raquete_img, (raquete1_x, raquete1_y))
#     janela.blit(raquete_img, (raquete2_x, raquete2_y))
#     janela.blit(bola_img, (bola_x, bola_y))

#     # Desenha a pontuação
#     pontos_texto = fonte.render(f'{pontos_player1} - {pontos_player2}', True, PRETO)
#     janela.blit(pontos_texto, (200, 20))

# # Função para reiniciar a bola após um ponto
# def reiniciar_bola():
#     global bola_x, bola_y, velocidade_bola_x, velocidade_bola_y
#     bola_x, bola_y = 250, 250
#     velocidade_bola_x = -velocidade_bola_x  # Inverte a direção para o jogador que marcou ponto

# while True:
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     # Movimentação das raquetes
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w] and raquete1_y > 0:
#         raquete1_y -= velocidade_raquete
#     if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
#         raquete1_y += velocidade_raquete
#     if keys[pygame.K_UP] and raquete2_y > 0:
#         raquete2_y -= velocidade_raquete
#     if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
#         raquete2_y += velocidade_raquete

#     # Movimentação da bola
#     bola_x += velocidade_bola_x
#     bola_y += velocidade_bola_y

#     # Colisões com as bordas da janela
#     if bola_y <= 0 or bola_y >= 500 - bola_img.get_height():
#         velocidade_bola_y = -velocidade_bola_y

#     # Colisão com as raquetes
#     if (bola_x <= raquete1_x + raquete_largura and bola_x >= raquete1_x and
#         bola_y + bola_img.get_height() > raquete1_y and bola_y < raquete1_y + raquete_altura):
#         velocidade_bola_x = -velocidade_bola_x
#     if (bola_x + bola_img.get_width() >= raquete2_x and bola_x + bola_img.get_width() <= raquete2_x + raquete_largura and
#         bola_y + bola_img.get_height() > raquete2_y and bola_y < raquete2_y + raquete_altura):
#         velocidade_bola_x = -velocidade_bola_x

#     # Pontuação (quando a bola sai da tela)
#     if bola_x <= 0:  # Player 2 marcou um ponto
#         pontos_player2 += 1
#         reiniciar_bola()
#     elif bola_x >= 500 - bola_img.get_width():  # Player 1 marcou um ponto
#         pontos_player1 += 1
#         reiniciar_bola()

#     # Desenhar os elementos na tela
#     desenhar()

#     # Atualizar a tela
#     pygame.display.update()

#     # Controlar o FPS
#     pygame.time.Clock().tick(60)