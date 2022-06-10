from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*
from PPlay.mouse import*
from PPlay.sound import*
import menu
import Player
import shooting
import pygame
from pygame import mixer

################################################################################################################################
################################################ Inicializações / Start() ######################################################
################################################################################################################################

def game(vidas,vidasInimigo,movimento,movimentoInimigo,velProjetil,velProjetilInimigo,delay,delayInimigo):
    # Instancio o tamanho da janela
    janela = Window(1280,720)

    # Inicializo o teclado
    teclado = janela.get_keyboard()

    # Adiciono musica
    mixer.music.load("EnvironmentMusic.wav")
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    
    # Instancio os cenários
    cenarioFloresta = GameImage("Floresta.jpg")
    cenarioCastelo = GameImage("Castelo.jpg")
    cenarioDungeon = GameImage("Dungeon.jpg")
    cenario = 1
    
    # Instancio os objetos
    placa = Sprite("Placa.png",1)
    placa.x = janela.width - placa.width - 50
    placa.y = janela.height-placa.height-240    
    chaoFloresta = Sprite("FlorestaChao.png",1)
    chaoFloresta.y = janela.height-chaoFloresta.height
    
    plataforma = GameImage("Plataforma.jpg")
    
    # Instancio os personagens
    player_Esq_Run = Sprite("Emih_invertido.png", 8)
    player_Esq_Run.x = 0
    player_Esq_Run.y = janela.height-player_Esq_Run.height
    player_Esq_Run.set_total_duration(1000)
    
    player_Dir_Run = Sprite("Emih.png", 8)
    player_Dir_Run.x = 0
    player_Dir_Run.y = janela.height-player_Dir_Run.height
    player_Dir_Run.set_total_duration(1000)
    
    player_Esq = Sprite("Emih_invertido_Idle.png", 1)
    player_Esq.x = 0
    player_Esq.y = janela.height-player_Esq.height
    
    player_Dir = Sprite("Emih_Idle.png", 1)
    player_Dir.x = 0
    player_Dir.y = janela.height-player_Dir.height
    
    player = player_Dir
    
    goblin = Sprite("Goblin.png", 1)
    cultista = Sprite("Cultista.png", 1)
    guardas = Sprite("Guardas.png", 1)
    caebralum = Sprite("Caebralum.png", 1)
    
    # Crio o vetor de projeteis aliados e sua direçao
    listaProjeteisE = []
    listaProjeteisD = []
    checkPos=0
    
    # Crio o vetor de projeteis inimigos
    listaProjeteisInimigosE = []
    listaProjeteisInimigosD = []
    checkPosInim=0
    
    # Crio a lista de inimigos
    listaInimigos = []
    
    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()
    
    ################################################################################################################################
    ##################################################### Game Loop / Update() #####################################################
    ################################################################################################################################
    while(True):
        # Desenho o cenario desejado
        if cenario==1:
            cenarioFloresta.draw()
        elif cenario==2:
            cenarioCastelo.draw()
        elif cenario==3:
            cenarioDungeon.draw()
        
        # Defino o Framerate
        clock.tick(FPS)
        
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            mixer.music.stop()
            menu.menu()
        
        # Chamo a funçao que lidará com o desenho da barra de vida
        life(vidas)
        
        # Crio a movimentacao do personagem principal
        checkPos = Player.movePlayer(janela,teclado,player,movimento,chaoFloresta,checkPos)
        if checkPos==0:
            if (teclado.key_pressed("D") or teclado.key_pressed("RIGHT")):
                player = Player.SetPlayer(player_Dir_Run,player)
                player.update()
            else:
                player = Player.SetPlayer(player_Dir,player)
        elif checkPos==1:
            if (teclado.key_pressed("A") or teclado.key_pressed("LEFT")):
                player = Player.SetPlayer(player_Esq_Run,player)
                player.update()
            else:
                player = Player.SetPlayer(player_Esq,player)

        # Crio a condiçao para mudar de cenário
        if ((player.x>janela.width-player.width/2) and (len(listaInimigos) == 0)):
            cenario+=1
        
        # Chamo a funçao que irá lidar com a criaçao dos tiros
        if (teclado.key_pressed("SPACE") and delay==0):
            Player.criaProjetil(player,listaProjeteisE,listaProjeteisD,checkPos)
            delay = shooting.recarga(movimentoInimigo,delay)
            
        # Faço o movimento dos tiros
        Player.magicAttack(janela,listaProjeteisE,listaProjeteisD,velProjetil,checkPos)
        if delay>0:
            delay-=1
        if delayInimigo>0:
            delayInimigo-=1
        
        # Desenho a placa que indica o que precisa ser feito
        placa.draw()
        
        # Desenho o personagem principal
        player.draw()
        
        # Desenho o fps
        if player.collided(placa):
            janela.draw_text(("DERROTE TODOS OS INIMIGOS PARA PROSSEGUIR!"), (janela.width/2)-325, 20, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        
        # Desenho o fps
        janela.draw_text(str(clock), janela.width-200, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()

def life(vidas):
    # Instancio as barras de vida
    healthBarFull = Sprite("HealthBarFull.png", 1)
    healthBarMedium1 = Sprite("HealthBarMedium1.png", 1)
    healthBarMedium2 = Sprite("HealthBarMedium2.png", 1)
    healthBarMedium3 = Sprite("HealthBarMedium3.png", 1)
    healthBarLow = Sprite("HealthBarLow.png", 1)
    # Defino a posiçao das imagens de Vida
    healthBarFull.set_position(0,0)
    healthBarMedium1.set_position(0,0)
    healthBarMedium2.set_position(0,0)
    healthBarMedium3.set_position(0,0)
    healthBarLow.set_position(0,0)
    # Desenho a barra de vida desejada
    if (vidas==5):
        healthBarFull.draw()
    if (vidas==4):
        healthBarMedium1.draw()
    if (vidas==3):
        healthBarMedium2.draw()
    if (vidas==2):
        healthBarMedium3.draw()
    if (vidas==1):
        healthBarLow.draw()