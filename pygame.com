import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
WALL_COLOR = (0, 0, 255)  # Blue color for the walls, similar to the original game

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.Surface((50, 50))  # Placeholder for player image
        self.image.fill((0, 255, 0))  # Green square as a placeholder

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def update(self, walls):
        # Movement code with collision detection (to be refined)
        for wall in walls:
            if self.x < wall.right and self.x + 50 > wall.left:
                if self.y < wall.bottom and self.y + 50 > wall.top:
                    # Collision occurred, handle it
                    return

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Room class
class Room:
    def __init__(self):
        self.walls = [
            pygame.Rect(0, 0, SCREEN_WIDTH, 10),
            pygame.Rect(0, 0, 10, SCREEN_HEIGHT),
            pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10),
            pygame.Rect(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT)
        ]

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, WALL_COLOR, wall)

# HUD function
def draw_hud(screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render('Score: 000000', True, (255, 255, 255))
    time_text = font.render('Time Left: 15:00', True, (255, 255, 255))
    screen.blit(score_text, (10, SCREEN_HEIGHT - 30))
    screen.blit(time_text, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 30))

# Game logic functions
def handle_input(player):
    dx, dy = 0, 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dy = -1
    elif keys[pygame.K_DOWN]:
        dy = 1
    if keys[pygame.K_LEFT]:
        dx = -1
    elif keys[pygame.K_RIGHT]:
        dx = 1
    player.move(dx, dy)

# Main game loop
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Prison Riot")
    clock = pygame.time.Clock()
    running = True

    player = Player(100, 100)
    room = Room()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input(player)
        player.update(room.walls)
        screen.fill((0, 0, 0))  # Clear screen

        room.draw(screen)
        player.draw(screen)
        draw_hud(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
