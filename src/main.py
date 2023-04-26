import pygame as pg


FPS = 144
BACKGROUND_COLOR = pg.Color(40, 42, 54)
SQUARE_COLOR = (0, 0, 255)
SQUARE_COLOR_2 = (0, 255, 0)


class Square(pg.Rect):
    def __init__(self, position, dimensions, mass):
        super().__init__(position, dimensions)
        self.mass = mass
        self.velocity = 0.
        self.acceleration = 0
        self.real_x = position[0]
    
    def move(self, dt):
        
        self.velocity += self.acceleration * dt
        self.real_x += self.velocity * dt

        self.x = self.real_x
        






def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()


    test = Square((200, 200), (150, 150), 50)
    test.velocity = 250
    test.acceleration = 0

    test2 = Square((800, 200), (150,150), 250)
    test2.velocity = -50
    test2.acceleration = 0
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


        test.move(dt)
        test2.move(dt)
        
        if test.colliderect(test2):

            test.x = test2.x - test2.width
            
            vel_test = (((test.mass - test2.mass) / (test.mass + test2.mass)) * test.velocity) + ((2*test2.mass / (test.mass + test2.mass)) * test2.velocity)
            vel_test2 = (((test2.mass - test.mass) / (test.mass + test2.mass)) * test2.velocity) + ((2*test.mass / (test.mass + test2.mass)) * test.velocity) 

            test.velocity = vel_test
            test2.velocity = vel_test2
            

        pg.draw.rect(screen, SQUARE_COLOR_2, test2)
        pg.draw.rect(screen, SQUARE_COLOR, test)

        pg.display.set_caption(f"fps: {round(clock.get_fps(), 2)}")
        pg.display.flip()
        

    pg.quit()


if __name__ == "__main__":
    main()
