import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Password Hero")

# Fonts and colors
FONT = pygame.font.SysFont('Arial', 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 80, 80)
GREEN = (100, 255, 100)

# Sample passwords
strong_passwords = ["V4$kL9@1", "S3cur3P@ss", "L!onT1gr#2"]
weak_passwords = ["123456", "password", "qwerty", "abc123"]

passwords = []

score = 0
clock = pygame.time.Clock()

class FallingPassword:
    def __init__(self, text, is_strong):
        self.text = text
        self.is_strong = is_strong
        self.x = random.randint(50, WIDTH - 150)
        self.y = -50
        self.speed = random.randint(2, 5)

    def draw(self):
        color = GREEN if self.is_strong else RED
        label = FONT.render(self.text, True, color)
        win.blit(label, (self.x, self.y))

    def move(self):
        self.y += self.speed

# Game loop
running = True
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 2000)

while running:
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == spawn_event:
            if random.choice([True, False]):
                text = random.choice(strong_passwords)
                passwords.append(FallingPassword(text, True))
            else:
                text = random.choice(weak_passwords)
                passwords.append(FallingPassword(text, False))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and passwords:
                current = passwords.pop(0)
                if current.is_strong:
                    score += 1
                else:
                    score -= 1

    # Update and draw
    for pw in passwords:
        pw.move()
        pw.draw()

    # Show score
    score_label = FONT.render(f"Score: {score}", True, WHITE)
    win.blit(score_label, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
