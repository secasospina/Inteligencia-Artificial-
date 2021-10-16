import pygame
import random

ANCHO=1200
ALTO=700
NEGRO=[0,0,0]
VERDE=[0,255,0]
Azul=[0,0,255]

class Bloque(pygame.sprite.Sprite): #esta heredando de la clase sprite.Sprite (clase padre)
    #constructor de la clase
    def __init__(self, p, cl=VERDE):
        pygame.sprite.Sprite.__init__(self) #invocamos al constructor de la case padre "self" es atributo por defecto
        self.image=pygame.Surface([60,60]) #crea un objeto con la dimension dada
        self.image.fill(cl) #pinta el objeto de color verde
        self.rect=self.image.get_rect() #guarda la ubicacion y tamano de la figura (define los limites)
        self.rect.x=p[0] #cambio las posiciones del objeto
        self.rect.y=p[1]
        self.velx=0 #creo las velocidades en x y
        self.vely=0
    
    def rotary(self): #fdfsf
        x=random.randint(0,1)
        
        if x == 0:
            self.vely=5
        else:
            self.vely=-5
                    
        
    def rotarx(self):
        x=random.randint(0,1)

        if x == 0:
            self.velx=5
        else:
            self.velx=-5
                

    def update(self): #mueve la figura sumando las velocidades a la posicion
        self.rect.x+=self.velx
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        for b in ls_col:
            if self.velx>0:
                if self.rect.right>b.rect.left:
                    self.rect.right=b.rect.left
                    self.velx=0
                    self.rotary()

            else:
                if self.rect.left<b.rect.right:
                    self.rect.left=b.rect.right
                    self.velx=0
                    self.rotary()

        self.rect.y+=self.vely
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        for b in ls_col:
        # Colision en x
            if self.vely>0:
                if self.rect.bottom>b.rect.top:
                    self.rect.bottom=b.rect.top
                    self.vely=0
                    self.rotarx()

            else:
                if self.rect.top<b.rect.bottom:
                    self.rect.top=b.rect.bottom
                    self.vely=0
                    self.rotarx()

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos,dims):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dims)
        self.image.fill(Azul)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

if __name__ == '__main__':
    ventana=pygame.display.set_mode([ANCHO,ALTO])

    #Crear grupo de sprites y plataformas
    jugadores=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()

    #Implementar clase
    j=Bloque([150,200]) #invoco al constructor y envie el valor de p

    #Bordes
    b=Plataforma([-30,0],[50,700])
    b2=Plataforma([0,670],[1200,50])
    b3=Plataforma([1180,0],[50,700])
    b4=Plataforma([0,-30],[1200,50])

    #Obstaculos
    n=30
    for i in range(n):
        x=random.randint(0,ANCHO-30)
        y=random.randint(0,ALTO-60)
        p=Plataforma([x,y],[50,50])
        plataformas.add(p)
    
    """p2=Plataforma([800,450],[100,100])
    p3=Plataforma([400,500],[100,100])
    p4=Plataforma([600,180],[100,100])

    p5=Plataforma([0,150],[150,50])
    p6=Plataforma([0,400],[50,150])
    p7=Plataforma([1050,180],[150,50])
    p8=Plataforma([1150,450],[50,150])

    p9=Plataforma([350,0],[50,150])
    p10=Plataforma([800,0],[150,50])
    p11=Plataforma([400,500],[100,100])
    p12=Plataforma([600,180],[100,100])"""

    #adiciono objeto al grupo
    jugadores.add(j)

    plataformas.add(b)
    plataformas.add(b2)
    plataformas.add(b3)
    plataformas.add(b4)
    """
    plataformas.add(p2)
    plataformas.add(p3)
    plataformas.add(p4)

    plataformas.add(p5)
    plataformas.add(p6)
    plataformas.add(p7)
    plataformas.add(p8)

    plataformas.add(p9)
    plataformas.add(p10)
    plataformas.add(p11)
    plataformas.add(p12)"""

    j.plataformas=plataformas

    #ciclo de control
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=-5
                if event.key == pygame.K_LEFT:
                    j.vely=0
                    j.velx=-5
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_DOWN:
                    j.vely=5
                    j.velx=0

        jugadores.update()
        #refresco de pantalla
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        plataformas.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)