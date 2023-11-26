import sys

import pygame

import random

class StarGrid:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Star Grid")
        self.bg_color = (255, 255, 255)

        original_star_image = pygame.image.load("./image/star.png")
        self.star_size = random.randint(20, 50)
        self.star_image = pygame.transform.scale(original_star_image, (self.star_size, self.star_size))

        self.star_positions = self.generate_star_positions()

        self.change_interval = 1000  # Change every 1000 milliseconds (1 second)
        self.last_change_time = pygame.time.get_ticks()

    def generate_star_positions(self):
        num_star_image = 30
        positions = []
        for _ in range(num_star_image):
            x = random.randint(0, self.screen.get_width() - self.star_size)
            y = random.randint(0, self.screen.get_height() - self.star_size)
            positions.append((x, y))
        return positions

    def run_game(self):
        while True:
            self.handle_events()
            self.screen.fill(self.bg_color)
            self.update_stars()
            self.draw_stars()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_stars(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_time > self.change_interval:
            self.last_change_time = current_time

            # Change star positions gradually
            for i in range(len(self.star_positions)):
                x, y = self.star_positions[i]
                new_x = x + random.randint(-20, 20)
                new_y = y + random.randint(-20, 20)
                self.star_positions[i] = (new_x, new_y)

    def draw_stars(self):
        for position in self.star_positions:
            self.screen.blit(self.star_image, position)

if __name__ == "__main__":
    star_grid = StarGrid()
    star_grid.run_game()