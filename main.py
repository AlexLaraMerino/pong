import pygame as pg
from figura_class import Pelota, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("P O N G")


pelota = Pelota(400,300)
raqueta1 = Raqueta(20,300)
raqueta2 = Raqueta(780,300)






game_over = False
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

        # Mopver raqueta
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_UP:
                print("ARRIBA")
                raqueta1.pos_y -= 5


    pantalla_principal.fill( (50,128,94) )
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)

    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()


