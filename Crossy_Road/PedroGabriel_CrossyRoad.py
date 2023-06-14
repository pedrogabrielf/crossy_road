import pygame
import sys
import os
from pathlib import Path
class botao():
    def __init__(self,texto,x,y,largura,altura,funcao):
        # Atributos padrões para verificações por motivos de performace
        self.clicou = False

        # Especifica o retangulo que sera desenhado
        self.retanguloConteiner = pygame.Rect(x,y,largura,altura)
        self.corBotao = (100,100,100)

        # escreve o texto na superficie
        self.texto = fonte_texto.render(texto,True,(255,255,255))
        # Obtem o tamanho do texto e o guarda dentro do retangulo que ira conter-lo
        self.retanguloTamnhoTexto = self.texto.get_rect(center=(self.retanguloConteiner.centerx, self.retanguloConteiner.centery))

        self.funcao = funcao

    def desenha_botao(self):
        # Desenha o retangulo especificado
        pygame.draw.rect(window,self.corBotao,self.retanguloConteiner,border_radius=10)
        # Coloca o retangulo na tela
        window.blit(self.texto,self.retanguloTamnhoTexto)

    def click(self):

        # Obtem a posição do maouse
        mouse = pygame.mouse.get_pos()

        # Verifica se o mouse esta dentro do botão
        if self.retanguloConteiner.collidepoint(mouse):
            
            # Muda a cor do botão quando o mouse esta dentro dele
            self.corBotao = (1, 1, 254)

            # Verifica se foi clicado com o botao direito
            if pygame.mouse.get_pressed()[0]:
                # Significa que ele clicou e somente uma booleana ira ser atribuida a essa variavel
                self.clicou = True
                
            # Quando a condição acima deixar de ser verdadeira ou seja o player deixou de pressionar o botao então a booleana volta a ser falsa por padrao e se executa a ação
            else:
                # Isso é feito dessa forma por conta de que aou se colocar uma grande quantidade de frames na execução do jogo essa ação seria executada varias vezes o que pode comprometer a performace do jogo em determinados dispositivos
                if self.clicou == True:
                    self.clicou = False
                    self.funcao()
        else:
            self.corBotao = (1, 115, 254)

def teste():
    global jogar
    jogar = True

def jogarFalse():
    global jogo
    jogo = False

def caminho_arquivo(nome:str):
    global caminho_arquivo
    caminho = os.path.dirname(os.path.realpath(__file__))
    caminhoAbsoluto = os.path.join(caminho, "assets/", nome)
    return caminhoAbsoluto

def informacoes():
    global infos
    infos = True

def desenha_container_titulo():
    pygame.draw.rect(window,(21,0,80),(55,30,700,100),border_radius=90)

def desenha_container_titulo2():
    pygame.draw.rect(window,(21,0,80),(115,30,600,100),border_radius=90)

def desenha_container_info():
    pygame.draw.rect(window,(21,0,80),(15,175,770,250),border_radius=80)

def escreve_texto(texto,fonte,corTexto,posicaoX,posicaoY):
    textoEscrito = fonte.render(texto,True,corTexto)
    window.blit(textoEscrito,(posicaoX,posicaoY))

def jogarnovament():
    jogarnovamentzin()

def jogarnovamentzin():
    global jogar,jogo,ganhou,infos
    jogar = False
    jogo = True
    ganhou = False
    infos = False

if __name__ == "__main__":
    pygame.init()

    relogio = pygame.time.Clock()
    fonte_texto = pygame.font.SysFont("arial", 30)
    botaojogar = botao("JOGAR", 315, 190, 200, 100, teste)
    botaoQUIT = botao("QUIT", 360,460,100,100,jogarFalse)
    botaoinfo = botao("Informações", 270, 330, 300, 100, informacoes)
    botaoJogarNovamente = botao("JOGAR NOVAMENTE", 245, 230, 350, 100, jogarnovament)
    
    botaoQUIT2 = botao("QUIT", 440,460,200,100,jogarFalse)

    botaojogar2 = botao("JOGAR", 160, 460, 200, 100, teste)


    # configs posicao frog
    posicao_frog_x = 380 #380 
    posicao_frog_y = 530 #530
    # posicao dos carros primeira parte

    # configs carro 1.1
    carro1_posicao_x = 800
    carro1_posicao_y = 398
    velocidade_car1 = 9

    # configs carro 2.1
    carro2_posicao_x = -120
    carro2_posicao_y = 330
    velocidade_car2 = 11

    # configs carro 3.1
    carro3_posicao_x = 930
    carro3_posicao_y = 470
    velocidade_car3 = 14

    # posicao dos carros na segunda parte!!!

    # configs carro 1.2
    carro1_posicao_x_2 = 800
    carro1_posicao_y_2 = 144

    # configs carro 2.2
    carro2_posicao_x_2 = -190
    carro2_posicao_y_2 = 175

    # configs carro 3.2
    carro3_posicao_x_2 = -100
    carro3_posicao_y_2 = 57


    posicao_iglu_x = 315
    posicao_iglu_y = 530

    posicao_core_x = 366
    posicao_core_y = 10

    largura = 800
    altura = 600
    # velocidade tartaruga
    velocidade = 3.5

    window = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Crossy Road")

    # load imagens
    tamanho_pinguim = (55, 65)

    fonteGeral = pygame.font.Font(caminho_arquivo("fonte2.ttf"),34)
    fonteGeral2 = pygame.font.Font(caminho_arquivo("fonte2.ttf"),23)
    fontePEQUENA = pygame.font.Font(caminho_arquivo("fonte2.ttf"),12)

    pinguim = pygame.image.load(caminho_arquivo('pinguim_direita.png'))
    pinguim = pygame.transform.scale(pinguim, tamanho_pinguim)

    pinguim_rect = pygame.Rect(posicao_frog_x, posicao_frog_y, pinguim.get_width() - 30, pinguim.get_height() - 30)

    bgInicio = pygame.image.load(caminho_arquivo('fundo.png'))
    bgInicio = pygame.transform.scale(bgInicio, (largura,altura))

    background = pygame.image.load(caminho_arquivo('background_frogger.png'))
    background = pygame.transform.scale(background, (largura, altura))

    carro1 = pygame.image.load(caminho_arquivo('carro_azul_direita.png'))
    carro1 = pygame.transform.scale(carro1, (120, 75))

    carro2 = pygame.image.load(caminho_arquivo('carro_azul2_esquerda.png'))
    carro2 = pygame.transform.scale(carro2, (120, 65))

    carro3 = pygame.image.load(caminho_arquivo('caminhao_esquerda.png'))
    carro3 = pygame.transform.scale(carro3, (120, 65))

    carro4 = pygame.image.load(caminho_arquivo('carro_azul_esquerda.png'))
    carro4 = pygame.transform.scale(carro4, (110, 50))

    carro5 = pygame.image.load(caminho_arquivo('carro5.png'))
    carro5 = pygame.transform.scale(carro5, (120, 135))

    carro6 = pygame.image.load(caminho_arquivo('carro6.png'))
    carro6 = pygame.transform.scale(carro6, (125, 80))

    iglu = pygame.image.load(caminho_arquivo('iglu.png'))
    iglu = pygame.transform.scale(iglu,(74,70))

    coracao = pygame.image.load(caminho_arquivo('coracao.png'))
    coracao = pygame.transform.scale(coracao,(79,52))
    coracao_rect = pygame.Rect(posicao_core_x, posicao_core_y, coracao.get_width()-50, coracao.get_height() - 50)

    def personagem_right():
        global pinguim
        pinguim = pygame.image.load(caminho_arquivo('pinguim_direita.png'))
        pinguim = pygame.transform.scale(pinguim, tamanho_pinguim)

    def personagem_left():
        global pinguim
        pinguim = pygame.image.load(caminho_arquivo('pinguim_esquerda.png'))
        pinguim = pygame.transform.scale(pinguim, tamanho_pinguim)

    personagem_right()  # Inicializa o pinguim virado para a direita


    jogar = False
    jogo = True
    ganhou = False
    infos = False

    while jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if jogar:
            if ganhou:
                window.fill((0,0,0))
                window.blit(bgInicio,(0,0))
                botaoJogarNovamente.desenha_botao()
                botaoJogarNovamente.click()
                botaoQUIT.desenha_botao()
                botaoQUIT.click()
            else:
                # movimentacao do sapo
                comandos = pygame.key.get_pressed()
                if comandos[pygame.K_UP] and posicao_frog_y >= 0:
                    posicao_frog_y -= velocidade
                if comandos[pygame.K_DOWN] and posicao_frog_y <= 535:
                    posicao_frog_y += velocidade
                if comandos[pygame.K_RIGHT] and posicao_frog_x <= 745:
                    personagem_right()
                    posicao_frog_x += velocidade
                if comandos[pygame.K_LEFT] and posicao_frog_x >= 12:
                    personagem_left()
                    posicao_frog_x -= velocidade

                # CONFIGS CARRO 1.1
                if carro1_posicao_x >= 850:
                    carro1_posicao_x = -120
                carro1_posicao_x += velocidade_car1

                # CONFIGS CARRO 2.1
                if carro2_posicao_x <= -150:
                    carro2_posicao_x = 850
                carro2_posicao_x -= velocidade_car2

                # CONFIGS CARRO 3.1
                if carro3_posicao_x <= -150:
                    carro3_posicao_x = 850
                carro3_posicao_x -= velocidade_car3

                # CONFIGS CARRO 1.2
                if carro1_posicao_x_2 <= -190:
                    carro1_posicao_x_2 = 900
                carro1_posicao_x_2 -= velocidade_car1

                # CONFIGS CARRO 2.2
                if carro2_posicao_x_2 >= 850:
                    carro2_posicao_x_2 = -120
                carro2_posicao_x_2 += velocidade_car2

                # CONFIGS CARRO 3.2
                if carro3_posicao_x_2 >= 850:
                    carro3_posicao_x_2 = -120
                carro3_posicao_x_2 += velocidade_car3

                # Criar retângulos dos carros 1
                carro1_rect = pygame.Rect(carro1_posicao_x, carro1_posicao_y, carro1.get_width(), carro1.get_height() - 20)
                carro2_rect = pygame.Rect(carro2_posicao_x, carro2_posicao_y, carro2.get_width(), carro2.get_height() - 20)
                carro3_rect = pygame.Rect(carro3_posicao_x, carro3_posicao_y, carro3.get_width(), carro3.get_height() - 20)

                # Criar retângulos dos carros 2
                carro4_rect = pygame.Rect(carro1_posicao_x_2, carro1_posicao_y_2, carro4.get_width(), carro4.get_height() - 30)
                carro5_rect = pygame.Rect(carro2_posicao_x_2, carro2_posicao_y_2, carro5.get_width(), carro5.get_height() - 50)
                carro6_rect = pygame.Rect(carro3_posicao_x_2, carro3_posicao_y_2, carro6.get_width(), carro6.get_height() - 20)

                # Verificar colisão com os carros
                if pinguim_rect.colliderect(carro1_rect) or pinguim_rect.colliderect(carro2_rect) or pinguim_rect.colliderect(carro3_rect):
                    # Houve colisão, volte o pinguim para sua posição inicial
                    posicao_frog_x = 380
                    posicao_frog_y = 535

                # Verificar colisão com os carros
                if pinguim_rect.colliderect(carro4_rect) or pinguim_rect.colliderect(carro5_rect) or pinguim_rect.colliderect(carro6_rect):
                    # Houve colisão, volte o pinguim para sua posição inicial
                    posicao_frog_x = 380
                    posicao_frog_y = 535

                if pinguim_rect.colliderect(coracao_rect):
                    ganhou = True
                    posicao_frog_x = 380
                    posicao_frog_y = 535
                # Atualizar retângulo do pinguim
                pinguim_rect.x = posicao_frog_x
                pinguim_rect.y = posicao_frog_y

                

                # desenhos fundo e sapo e carros
                window.blit(background, (0, 0))
                window.blit(pinguim, (posicao_frog_x, posicao_frog_y))
                window.blit(carro1, (carro1_posicao_x, carro1_posicao_y))
                window.blit(carro2, (carro2_posicao_x, carro2_posicao_y))
                window.blit(carro3, (carro3_posicao_x, carro3_posicao_y))

                window.blit(carro4, (carro1_posicao_x_2, carro1_posicao_y_2))
                window.blit(carro5, (carro2_posicao_x_2, carro2_posicao_y_2))
                window.blit(carro6, (carro3_posicao_x_2, carro3_posicao_y_2))

                window.blit(iglu, (posicao_iglu_x, posicao_iglu_y))

                window.blit(coracao, (posicao_core_x, posicao_core_y))
        elif infos:
        
            window.fill((0,0,0))

            window.blit(bgInicio, (0,0))

            desenha_container_titulo()
            desenha_container_info()

            escreve_texto("INFORMAÇÕES ABAIXO:",fonteGeral,(255,255,255),85,65)
            escreve_texto("PARA JOGAR UTILIZE AS SETAS",fonteGeral2,(255,255,255),90,205)
            escreve_texto("DO SEU TECLADO",fonteGeral2,(255,255,255),260,255)
            escreve_texto("SEU OBJETIVO É CHEGAR ATÉ O",fonteGeral2,(255,255,255),90,320)
            escreve_texto("CORAÇÃO",fonteGeral2,(255,255,255),320,370)

            botaojogar2.desenha_botao()
            botaojogar2.click()

            botaoQUIT2.desenha_botao()
            botaoQUIT2.click()


                # update da tela
        else:
            window.blit(bgInicio, (0,0))

            desenha_container_titulo2()

            escreve_texto("CROSSY-ROAD",fonteGeral,(255,255,255),230,57)
            escreve_texto("VERSÃO: SHOPEE",fontePEQUENA,(255,255,255),330,105)


            botaojogar.desenha_botao()
            botaojogar.click()

            botaoinfo.desenha_botao()
            botaoinfo.click()

            botaoQUIT.desenha_botao()
            botaoQUIT.click()  
        pygame.display.update()

        relogio.tick(60)
