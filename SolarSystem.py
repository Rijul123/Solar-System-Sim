import pygame
from CelestialBody import CelestialBody

# Constants




def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Planet Simulation")
    FONT = pygame.font.SysFont("comicsans", 16)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    DARK_GREY = (80, 78, 81)
    LIGHT_ORANGE = (254, 216, 177)
    BACKGROUND_COLOR = (0, 0, 40)
    clock = pygame.time.Clock()
    run = True

    sun = CelestialBody(0, 0, 30, YELLOW, 1.98892 * 10**30, sun=True)
    earth = CelestialBody(-1 * CelestialBody.AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000
    mars = CelestialBody(-1.524 * CelestialBody.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    mercury = CelestialBody(0.387 * CelestialBody.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    venus = CelestialBody(0.723 * CelestialBody.AU, 0, 14, LIGHT_ORANGE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    celestial_bodies = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(BACKGROUND_COLOR)

        for body in celestial_bodies:
            body.update_position(celestial_bodies)
            body.draw(WIN, FONT)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()