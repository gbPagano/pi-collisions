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

    def update_real_x(self):
        self.real_x = self.x
        






def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    
    collisions = 0

    test = Square((200, 200), (150, 150), 1)
    test.velocity = 0
    test.acceleration = 0

    test2 = Square((600, 200), (150,150), 100**2)
    test2.velocity = -100
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
        counter = 0

        test.move(dt)
        test2.move(dt)
        
        check_collision(test, test2)

        wall = Square((0, 0), (50, 1000), 0)


        if counter: 
            collisions += counter
            print(collisions)
            print(test.velocity, test2.velocity)

        pg.draw.rect(screen, (255,0,0), wall)
        pg.draw.rect(screen, SQUARE_COLOR_2, test2)
        pg.draw.rect(screen, SQUARE_COLOR, test)

        pg.display.set_caption(f"fps: {round(clock.get_fps(), 2)}")
        pg.display.flip()
        

    pg.quit()


def check_collision(obj_a, obj_b):
    if obj_a.colliderect(obj_b):
        #counter += 1
        # print(obj_a.x, obj_b.x - obj_b.width)
        print("bloco")

        obj_a.right = obj_b.left
        obj_b.update_real_x()
        obj_a.update_real_x()
        
        mass_sum = obj_a.mass + obj_b.mass

        vel_obj_a = (((obj_a.mass - obj_b.mass) / (mass_sum)) * obj_a.velocity) + ((2*obj_b.mass / (mass_sum)) * obj_b.velocity)
        vel_obj_b = (((obj_b.mass - obj_a.mass) / (mass_sum)) * obj_b.velocity) + ((2*obj_a.mass / (mass_sum)) * obj_a.velocity)

        # print("antes:", obj_a.velocity * obj_a.mass + obj_b.velocity * obj_b.mass)
        # print("depois:", vel_obj_a * obj_a.mass + vel_obj_b * obj_b.mass)

        obj_a.velocity = round(vel_obj_a, 4)
        obj_b.velocity = round(vel_obj_b, 4)





if __name__ == "__main__":
    main()
