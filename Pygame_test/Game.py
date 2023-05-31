# Im just testing some pygame stuff


import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

square_size = 50
square_pos = [(WIDTH - square_size) // 2, (HEIGHT - square_size) // 2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_pos[1] -= 0.5
    if keys[pygame.K_s]:
        square_pos[1] += 0.5
    if keys[pygame.K_a]:
        square_pos[0] -= 0.5
    if keys[pygame.K_d]:
        square_pos[0] += 0.5

    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, (square_pos[0], square_pos[1], square_size, square_size))
    pygame.display.update()

pygame.quit()


