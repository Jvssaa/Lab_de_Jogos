from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *

def sair():
    janela = Window(1280,720)

    teclado = janela.get_keyboard()

    mouseClick = janela.get_mouse()

    simButton = Sprite("Sim.png", 1)
    naoButton = Sprite("Nao.png", 1)

    # Instancio o fundo
    fundo = GameImage("FundoInicial.jpg")
    fundo.draw()

    while (True):
        if(teclado.key_pressed("ESC")):
            import menu
            menu.menu()
        
        janela.draw_text(("DESEJA MESMO SAIR?"), (janela.width / 2)-280, 100, size=48, font_name="Arial", bold=True,color=[255, 0, 255])
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(simButton)):
            janela.close()
        if((mouseClick.is_button_pressed(1) and mouseClick.is_over_object(naoButton)) or (teclado.key_pressed("ESC"))):
            import menu
            menu.menu()
        
        simButton.set_position((janela.width/2) -120, (janela.height/2))
        naoButton.set_position((janela.width/2) -120, (janela.height/2)+120)
        
        simButton.draw()
        naoButton.draw()
        
        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Atualizo o Gameloop
        janela.update()
