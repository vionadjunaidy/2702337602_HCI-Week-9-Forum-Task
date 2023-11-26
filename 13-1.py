import sys
import pygame

class StarGrid:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Star Grid")
        self.bg_color = (255, 255, 255)

        original_star_image = pygame.image.load("./image/star.png")
        self.star_width, self.star_height = 50, 50
        self.star_image = pygame.transform.scale(original_star_image, (self.star_width, self.star_height))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_color)

            self.draw_edge_stars()

            pygame.display.flip()
            self.clock.tick(60)

    def draw_edge_stars(self):
        #Place stars at the top edge of the screen.
        for col in range(self.screen.get_width() // (self.star_width + 5)):
            x = col * (self.star_width + 5) + 5
            y = 5
            self.screen.blit(self.star_image, (x, y))

        #Place stars at the bottom edge of the screen.
        for col in range(self.screen.get_width() // (self.star_width + 5)):
            x = col * (self.star_width + 5) + 5
            y = self.screen.get_height() - self.star_height - 5
            self.screen.blit(self.star_image, (x, y))

        #Place stars at the left edge of the screen.
        for row in range(1, (self.screen.get_height()) // (self.star_height + 5)):
            x = 5
            y = row * (self.star_height + 5) + 5
            self.screen.blit(self.star_image, (x, y))

        #Place stars at the right edge of the screen.
        for row in range(1, (self.screen.get_height()) // (self.star_height + 5)):
            x = self.screen.get_width() - self.star_width - 5
            y = row * (self.star_height + 5) + 5
            self.screen.blit(self.star_image, (x, y))

if __name__ == "__main__":
    star_grid = StarGrid()
    star_grid.run_game()