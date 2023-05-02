import pygame as pg

from objects import Square

FPS = 144
BACKGROUND_COLOR = pg.Color(40, 42, 54)
SQUARE_COLOR = (0, 0, 255)
SQUARE_COLOR_2 = (0, 255, 0)
SQUARE_MASS = 1
SQUARE_MASS_2 = 100**3
SQUARE_TAM = 50
SQUARE_TAM_2 = 200
WALL_TAM = 50, 1000


def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    sound_collision = pg.mixer.Sound("data/collision_song.mp3")
    collisions = 0
    wall = Square((0, 0), WALL_TAM, float("inf"))
    square_1 = Square((200, 400), SQUARE_TAM, SQUARE_MASS)

    square_2 = Square((300, 400), SQUARE_TAM_2, SQUARE_MASS_2)
    square_2.y = 400 - SQUARE_TAM_2 + SQUARE_TAM
    square_2.velocity = -100
    # main loop
    running = True
    while running:
        clock.tick(FPS)
        dt = clock.get_time() / 1000  # millisec to sec

        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                return pg.quit()

        screen.fill(BACKGROUND_COLOR)
        
        match SQUARE_MASS_2:
            case 1:
                x = 1
            case 100:
                x = 10
            case 10_000:
                x = 70
            case 1_000_000:
                x = 650
            case _:
                x = 1000 

        for _ in range(x):
            square_2.move(dt / x)
            square_1.move(dt / x)
            if square_1.colliderect(square_2) or square_1.right > square_2.left:
                sound_collision.play()
                collisions += 1
                square_1.apply_collision(square_2)
                square_1.right = square_2.left
                square_1.update_real_x()

            if square_1.colliderect(wall) or square_1.left  < wall.right:
                sound_collision.play()
                collisions += 1
                square_1.velocity *= -1
                square_1.left = wall.right
                square_1.update_real_x()

            if square_2.x < square_1.width + wall.width:
                square_2.x = square_1.width + wall.width
                square_2.update_real_x()

        print(collisions)
        print(not (square_1.velocity > 0 and square_1.velocity < square_2.velocity))


        pg.draw.rect(screen, (255, 0, 0), wall)
        pg.draw.rect(screen, SQUARE_COLOR_2, square_2)
        pg.draw.rect(screen, SQUARE_COLOR, square_1)

        pg.display.set_caption(f"fps: {round(clock.get_fps(), 2)}")
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
