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
        self.collisions_counter = 0
    
    def move(self, dt):
        
        self.velocity += self.acceleration * dt
        self.real_x += self.velocity * dt

        self.x = self.real_x

    def update_real_x(self):
        self.real_x = self.x

    def check_collisions(self, objects):
        for obj in objects:
            if self.colliderect(obj):
                print(self.x, obj.x, self.velocity, obj.velocity)
                if obj.mass == float("inf"):
                    self.velocity *= -1
                else:
                    self.apply_collision(obj)


    def apply_collision(self, obj):
        self.collisions_counter += 1
        
        # if self.velocity >= 0:
        #     self.right = obj.left
        # else:
        #     self.left = obj.right

 

        
        # self.update_real_x()
        
        mass_sum = self.mass + obj.mass

        vel_self = (((self.mass - obj.mass) / (mass_sum)) * self.velocity) + ((2*obj.mass / (mass_sum)) * obj.velocity)
        vel_obj = (((obj.mass - self.mass) / (mass_sum)) * obj.velocity) + ((2*self.mass / (mass_sum)) * self.velocity)

        # print("antes:", self.velocity * self.mass + obj.velocity * obj.mass)
        # print("depois:", vel_self * self.mass + vel_obj * obj.mass)

        self.velocity = round(vel_self, 4)
        obj.velocity = round(vel_obj, 4)





def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    pg.mixer.music.load("data/collision_song.mp3") 
    collisions = 0
    wall = Square((0, 0), (50, 1000), float("inf"))
    square_1 = Square((200, 200), (50, 50), 1)
    

    square_2 = Square((300, 200), (50,50), 100**2)
    square_2.velocity = -50
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

        x = 10
        for _ in range(x):
            square_2.move(dt / x)
            square_1.move(dt / x)
            if square_1.colliderect(square_2):
                pg.mixer.music.play()
                collisions += 1
                square_1.apply_collision(square_2)
                square_1.right = square_2.left
                square_1.update_real_x()

            if square_1.colliderect(wall):
                pg.mixer.music.play()
                collisions += 1
                square_1.velocity *= -1
                square_1.left = wall.right
                square_1.update_real_x()

            if square_2.x < square_1.width + wall.width:
                square_2.x = square_1.width + wall.width
                square_2.update_real_x()

        # square_2.move(dt)
        # if square_1.colliderect(square_2):
        #     collisions += 1
        #     square_1.apply_collision(square_2)
        #     square_1.right = square_2.left
        #     square_1.update_real_x()

        # if square_1.colliderect(wall):
        #     collisions += 1
        #     square_1.velocity *= -1
        #     square_1.left = wall.right
        #     square_1.update_real_x()

        # if square_2.x < square_1.width + wall.width:
        #     square_2.x = square_1.width + wall.width
        #     square_2.update_real_x()
        
        print(collisions) 
        print(not (square_1.velocity > 0 and square_1.velocity < square_2.velocity))
        pg.draw.rect(screen, (255,0,0), wall)
        pg.draw.rect(screen, SQUARE_COLOR_2, square_2)
        pg.draw.rect(screen, SQUARE_COLOR, square_1)

        pg.display.set_caption(f"fps: {round(clock.get_fps(), 2)}")
        pg.display.flip()
        

    pg.quit()





if __name__ == "__main__":
    main()
