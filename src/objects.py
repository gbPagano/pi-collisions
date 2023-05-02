import pygame as pg


class Square(pg.Rect):
    def __init__(self, position, dimension, mass):
        if isinstance(dimension, tuple):
            super().__init__(position, dimension)
        else:
            super().__init__(position, (dimension, dimension))
        self.mass = mass
        self.velocity = 0.0
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

        mass_sum = self.mass + obj.mass

        vel_self = (((self.mass - obj.mass) / (mass_sum)) * self.velocity) + (
            (2 * obj.mass / (mass_sum)) * obj.velocity
        )
        vel_obj = (((obj.mass - self.mass) / (mass_sum)) * obj.velocity) + (
            (2 * self.mass / (mass_sum)) * self.velocity
        )

        self.velocity = round(vel_self, 4)
        obj.velocity = round(vel_obj, 4)

