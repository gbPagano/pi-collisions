import pygame as pg


FPS = 144
BACKGROUND_COLOR = pg.Color(40, 42, 54)


class Square(pg.Rect):
    def __init__(self, position, dimensions, mass):
        super().__init__(position, dimensions)
        self.mass = mass
        self.velocity = 0
        self.acceleration = 0
        self.position_x = 200


import time
def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    delta_time = 0


    test = Square((200, 200), (50, 50), 50)

    # main loop
    a = time.time()
    running = True
    while running:
        clock.tick(FPS)
        dt2 = clock.get_time() / 1000

        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                return pg.quit()

        screen.fill(BACKGROUND_COLOR)


        # print(dt)
        # print(dt2)
        # print(clock.get_time())
        
        # print(test.x, test.y)
        pg.draw.rect(screen, (0, 0, 255), test)

        test.position_x += 600 * dt2
        # test.move_ip(200 * dt2, 0)
        test.x = test.position_x
        # print(delta_time)
        if test.x > 800: 
            b = time.time() - a
            print(b)
            print(test.position_x)
            print(test.x)
            print((test.position_x  - 200) / b)
            break
        

        pg.display.set_caption(f"fps: {round(clock.get_fps(), 2)}")
        pg.display.flip()
        

    pg.quit()


if __name__ == "__main__":
    main()
