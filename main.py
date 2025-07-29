
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
BLUE = (100, 100, 255)

# Sample passwords 
strong_passwords = [
    "Tr0ub4dor&3", "MyDog$N4me1s", "P@ssw0rd123!", "B1ueOc3an#77",
    "C0ff33L0v3r!", "R4nd0m$tr1ng", "S3cur3P@ss99", "M0rn1ng$un22",
    "D4nc3M0v3s!", "F1r3w0rk$23", "Th3Qu1ckF0x!", "N1ght0wl#88",
    "J0urn3y2024!", "Spark1e&Sh1ne", "Adv3ntur3$77", "Br1ght$t4r9"
]
weak_passwords = [
    "123456", "password", "qwerty", "abc123", "admin", "letmein",
    "welcome", "monkey", "dragon", "sunshine", "iloveyou", "princess",
    "football", "charlie", "aa123456", "donald", "password1", "qwerty123",
    "login", "guest", "user", "test", "master", "shadow"
]

passwords = []

score = 0
clock = pygame.time.Clock()
last_spawn_time = 0
spawn_interval = 2000  # 2 seconds

class FallingPassword:
    def __init__(self, text, is_strong):
        self.text = text
        self.is_strong = is_strong
        self.x = random.randint(50, WIDTH - 150)
        self.y = -50
        self.speed = random.randint(2, 4)  # More consistent speed

    def draw(self):
        color = GREEN if self.is_strong else RED
        label = FONT.render(self.text, True, color)
        win.blit(label, (self.x, self.y))

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > HEIGHT

# Game loop
running = True

while running:
    current_time = pygame.time.get_ticks()
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and passwords:
                # Find the password that's closest to the bottom (highest y value)
                closest_password = max(passwords, key=lambda pw: pw.y)
                passwords.remove(closest_password)
                
                if closest_password.is_strong:
                    score += 1
                else:
                    score -= 1

    # Spawn new passwords with better timing control
    if current_time - last_spawn_time > spawn_interval:
        if random.choice([True, False]):
            text = random.choice(strong_passwords)
            passwords.append(FallingPassword(text, True))
        else:
            text = random.choice(weak_passwords)
            passwords.append(FallingPassword(text, False))
        last_spawn_time = current_time

    # Update and draw passwords
    passwords_to_remove = []
    for pw in passwords:
        pw.move()
        pw.draw()
        
        # Remove passwords that have fallen off screen
        if pw.is_off_screen():
            passwords_to_remove.append(pw)
    
    # Remove off-screen passwords
    for pw in passwords_to_remove:
        passwords.remove(pw)

    # Show score
    score_label = FONT.render(f"Score: {score}", True, WHITE)
    win.blit(score_label, (10, 10))
    
    # Show instructions
    instruction_label = FONT.render("SPACE: Accept green passwords, reject red ones", True, BLUE)
    win.blit(instruction_label, (10, HEIGHT - 30))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
