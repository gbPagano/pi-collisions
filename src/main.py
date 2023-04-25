import pygame as pg


FPS = 60
BACKGROUND_COLOR = pg.Color(40, 42, 54)


def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    delta_time = 0

    # main loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                return pg.quit()

        screen.fill(BACKGROUND_COLOR)
        pg.display.flip()
        delta_time = clock.tick(FPS)
        pg.display.set_caption(f"fps: {round(clock.get_fps(), 2)}")

    pg.quit()


if __name__ == "__main__":
    main()
