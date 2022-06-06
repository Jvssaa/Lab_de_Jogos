from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*

def spawn(linha,matrizDeInimigos):    
    for i in range(linha):
        linhas = []
        for j in range(12):
            if linha==3:
                if i==0:
                    inimigoAtras = Sprite("inimigo3.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linhas.append(inimigoAtras)
                elif i==1:
                    inimigoMeio = Sprite("inimigo2.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linhas.append(inimigoMeio)
                else:
                    inimigoFrente = Sprite("inimigo1.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linhas.append(inimigoFrente)
            if linha==4:
                if i==0:
                    inimigoAtras = Sprite("inimigo3.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linhas.append(inimigoAtras)
                elif 1<=i<=2:
                    inimigoMeio = Sprite("inimigo2.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linhas.append(inimigoMeio)
                else:
                    inimigoFrente = Sprite("inimigo1.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linhas.append(inimigoFrente)
            if linha==5:
                if i==0:
                    inimigoAtras = Sprite("inimigo3.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linhas.append(inimigoAtras)
                elif 1<=i<=3:
                    inimigoMeio = Sprite("inimigo2.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linhas.append(inimigoMeio)
                else:
                    inimigoFrente = Sprite("inimigo1.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linhas.append(inimigoFrente)
            if linha==6:
                if i==0:
                    inimigoAtras = Sprite("inimigo3.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linhas.append(inimigoAtras)
                elif 1<=i<=3:
                    inimigoMeio = Sprite("inimigo2.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linhas.append(inimigoMeio)
                elif i==4:
                    inimigoFrente = Sprite("inimigo1.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linhas.append(inimigoFrente)
                else:
                    inimigoBonus = Sprite("inimigoBonus.png",1)
                    inimigoBonus.x = -100
                    inimigoBonus.y = 0
                    break
        matrizDeInimigos.append(linhas)
    if linha==6:
        return inimigoBonus

def draw(linhaDeInimigos):
    for i in range(len(linhaDeInimigos)):
        linhaDeInimigos[i].draw()

def moveInimigos(janela, matrizDeInimigos, movimentoInimigo):
    bateu = False
    for i in matrizDeInimigos:
        for j in i:
            j.x += movimentoInimigo*janela.delta_time()
            if ((j.x >= janela.width - j.width - 5) or (j.x<-5)):
                bateu = True
    if (bateu):
        movimentoInimigo *= -1
        for i in matrizDeInimigos:
            for j in i:
                j.x += movimentoInimigo*janela.delta_time()
                j.y += 50
    return movimentoInimigo

def kill(listaProjeteis,matrizDeInimigos,score,linha):
    for k,linhaDeInimigos in enumerate(matrizDeInimigos):
        for i,inimigo in enumerate(linhaDeInimigos):
            for j,projetil in enumerate(listaProjeteis):
                if (projetil.collided(inimigo)):
                    listaProjeteis.pop(j)
                    linhaDeInimigos.pop(i)
                    if linha==3:
                        if k==0:
                            score+=30
                        elif k==1:
                            score+=20
                        else:
                            score+=10
                    elif linha==4:
                        if k==0:
                            score+=30
                        elif 1<=k<=2:
                            score+=20
                        else:
                            score+=10
                    elif linha==5:
                        if k==0:
                            score+=30
                        elif 1<=k<=3:
                            score+=20
                        else:
                            score+=10
                    else:
                        if k==0:
                            score+=30
                        elif 1<=k<=3:
                            score+=20
                        elif k==4:
                            score+=10
                        else:
                            score+=100
    return score 
def hit(vidas,player,listaDeInimigos,listaProjeteisInimigos,score):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(player)):
            listaProjeteisInimigos.pop(i)
            vidas-=1
    for i,inimigo in enumerate(listaDeInimigos):
        if (inimigo.collided(player) or inimigo.y==player.y):
            from ranking import fimDoJogoDerrota
            fimDoJogoDerrota(score)
    return vidas