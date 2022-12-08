import pygame as pg
from figura_class import Pelota, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("P O N G")

# Definir tasa de refresco del programa (FPS)
cronometro = pg.time.Clock()

pelota = Pelota(400,300)
raqueta1 = Raqueta(20,300)
raqueta2 = Raqueta(780,300)

# Asignando velovidad
raqueta1.vy=6
raqueta2.vy=6
pelota.vx=2




game_over = False
while not game_over:
    # Imprimir los milisegundos que tarde actualmente cada fotograma
    vt = cronometro.tick(144) # Variable para contrtolar la velocidad entre fotogramas
    #print(vt)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

        # Mopver raqueta
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_UP:
                #print("ARRIBA")
                raqueta1.pos_y -= 5


    raqueta1.mover(pg.K_UP,pg.K_DOWN)
    raqueta2.mover(pg.K_w, pg.K_s)

    pelota.mover()
    


    pantalla_principal.fill( (50,128,94) )

    pelota.comprobar_choqueV2(raqueta2,raqueta1)
    pelota.marcador(pantalla_principal)
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)
    

    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()


