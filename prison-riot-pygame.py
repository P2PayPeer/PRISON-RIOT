# PRISON-RIOT
# TODO: Implement more complex prison layout
# TODO: Create more character classes with health, behavior
# TODO: Add escape mechanics
# TODO: Develop riot and emergency mechanics
# TODO: Enhance combat system
# TODO: Integrate graphics and animations
# TODO: Improve User Interface
# TODO: Add sound effects and music
# TODO: Optimize and refine game loop
# TODO: Regular testing and debugging

import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
FONT_FILE = 'font.ttf'  # Path to your custom font file

# Initialize Pygame
pygame.init()

# Load custom font
font = pygame.font.Font(FONT_FILE, 36)

WALL_COLOR = (0, 0, 255)  # Blue color for the walls, similar to the original game
KEY_COLOR = (255, 255, 0)  # Color for keys
DOOR_COLOR = (139, 69, 19)  # Color for doors


# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.Surface((50, 50))  # Placeholder for player image
        self.image.fill((0, 255, 0))  # Green square as a placeholder

    def move(self, dx, dy, walls, interactive_objects):
        # Attempt to move in the X direction
        self.x += dx * self.speed
        self.rect.x = self.x
        if self.check_collision(walls, interactive_objects):
            self.x -= dx * self.speed  # Move back if collision detected
        self.rect.x = self.x

        # Attempt to move in the Y direction
        self.y += dy * self.speed
        self.rect.y = self.y
        if self.check_collision(walls, interactive_objects):
            self.y -= dy * self.speed  # Move back if collision detected
        self.rect.y = self.y

    def check_collision(self, walls, interactive_objects):
        for wall in walls:
            if self.rect.colliderect(wall):
                return True
        for obj in interactive_objects:
            if self.rect.colliderect(obj.rect):
                self.interact_with(obj)
                return True
        return False

    def interact_with(self, obj):
        # Define interactions with objects
        print("Interacted with an object!")  # Placeholder for interaction logic

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# InteractiveObject class
class InteractiveObject:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


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


# NPC class
class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((50, 50))  # Placeholder for NPC image
        self.image.fill((255, 255, 0))  # Yellow square as a placeholder

    def update(self, walls):
        # Add basic movement or behavior patterns
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# HUD function
def draw_hud(screen):
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
    return dx, dy


def render_text(screen, text, x, y, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


# Game loop
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Prison Riot")
    clock = pygame.time.Clock()
    running = True

    # Initialize game elements
    player = Player(100, 100)
    room = Room()
    keys = [InteractiveObject(300, 300, 20, 20, KEY_COLOR)]  # Example key object
    doors = [InteractiveObject(500, 200, 20, 50, DOOR_COLOR)]  # Example door
    npcs = [NPC(200, 200)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input
        dx, dy = handle_input(player)
        player.move(dx, dy, room.walls, keys + doors)

        # Update NPCs
        for npc in npcs:
            npc.update(room.walls)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw game elements
        room.draw(screen)
        for key in keys:
            key.draw(screen)
        for door in doors:
            door.draw(screen)
        for npc in npcs:
            npc.draw(screen)
        player.draw(screen)
        draw_hud(screen)

        # Render any text or game-related information
        render_text(screen, "PRISON RIOT", 10, 10)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)


# Start the game loop
if __name__ == '__main__':
    game_loop()
