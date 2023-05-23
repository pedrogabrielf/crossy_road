import pygame
import sys

pygame.init()
#configs posicao frog
posicao_frog_x=380 # posicao max 745 - min 12 - - 380
posicao_frog_y=545

#configs carro 1

carro1_posicao_x = -120
carro1_posicao_y = 320
velocidade_car1 = 0.3

#configs carro 2

carro2_posicao_x = 850
carro2_posicao_y = 470
velocidade_car2 = 0.2

#configs carro 2

carro3_posicao_x = 800
carro3_posicao_y = 398
velocidade_car3 = 0.35


largura = 800
altura = 600
#velocidade tartaruga
velocidade = 0.11

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Crossy Road")

#load imagens
novo_tamanho_frog = (43, 43)

sapo = pygame.image.load('frogger.png')
sapo = pygame.transform.scale(sapo, novo_tamanho_frog)

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (largura, altura))

carro1 = pygame.image.load('carro_azul_direita.png')
carro1 = pygame.transform.scale(carro1, (120, 75))

carro2 = pygame.image.load('carro_azul2_esquerda.png')
carro2 = pygame.transform.scale(carro2, (120, 75))

carro3 = pygame.image.load('caminhao_esquerda.png')
carro3 = pygame.transform.scale(carro3, (120, 75))


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #movimentacao do sapo
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        posicao_frog_y-= velocidade
    if comandos[pygame.K_DOWN]:
        posicao_frog_y+= velocidade
    if comandos[pygame.K_RIGHT] and posicao_frog_x <= 745:
        posicao_frog_x+= velocidade
    if comandos[pygame.K_LEFT] and posicao_frog_x >= 12:
        posicao_frog_x-= velocidade

    #CONFIGS CARRO 1
    if (carro1_posicao_x >= 850):
        carro1_posicao_x = -120
    carro1_posicao_x += velocidade_car1

    #CONFIGS CARRO 2
    if (carro2_posicao_x <= -150):
        carro2_posicao_x = 850
    carro2_posicao_x -= velocidade_car2

    #CONFIGS CARRO 3
    if (carro3_posicao_x <= -150):
        carro3_posicao_x = 850
    carro3_posicao_x -= velocidade_car3


    #desenhos fundo e sapo e carros
    window.blit(background, (0, 0))
    window.blit(sapo, (posicao_frog_x,posicao_frog_y))
    window.blit(carro1, (carro1_posicao_x, carro1_posicao_y))
    window.blit(carro2, (carro2_posicao_x, carro2_posicao_y))
    window.blit(carro3, (carro3_posicao_x, carro3_posicao_y))
    #update da tela
    pygame.display.update()
