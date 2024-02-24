import pygame
import math

class CelestialBody:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24

    def __init__(self, x, y, radius, color, mass, sun=False):
        self.x, self.y = x, y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.sun = sun
        self.distance_to_sun = 0
        self.x_vel, self.y_vel = 0, 0
        self.orbit = []

    def draw(self, win, font):
        WIDTH, HEIGHT = pygame.display.get_surface().get_size()
        x, y = self.x * self.SCALE + WIDTH / 2, self.y * self.SCALE + HEIGHT / 2
        if len(self.orbit) > 2:
            updated_points = [(p[0] * self.SCALE + WIDTH / 2, p[1] * self.SCALE + HEIGHT / 2) for p in self.orbit]
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)
        if not self.sun:
            distance_text = font.render(f"{round(self.distance_to_sun / CelestialBody.AU, 1)} AU", 1, (255, 255, 255))
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

    def attraction(self, other):
        distance_x, distance_y = other.x - self.x, other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if other.sun:
            self.distance_to_sun = distance
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x, force_y = math.cos(theta) * force, math.sin(theta) * force
        return force_x, force_y

    def update_position(self, celestial_bodies):
        total_fx, total_fy = 0, 0
        for body in celestial_bodies:
            if self != body:
                fx, fy = self.attraction(body)
                total_fx += fx
                total_fy += fy
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))