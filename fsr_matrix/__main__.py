"""
Visualizer for the data coming out of the FSR matrix
"""
from fsr_matrix.classifier.deprecated import ObjectClassifier
from fsr_matrix.map_raw_output import open_serial_connection, collect_reading
import numpy as np
import pygame

fsr_size = (11, 7)
tile_size = 40
window_size = (fsr_size[0] * tile_size, (fsr_size[1] + 1) * tile_size)

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Visualizer")

# Loop carries on until the user exits the visualizer
carryOn = True

# Clock controls refresh rate
clock = pygame.time.Clock()

ser = open_serial_connection()
classifier = ObjectClassifier(mode="load")
font = pygame.font.SysFont("arial", 15)


def render_text(text, x, y):
    t = font.render(text, True, WHITE, BLACK)
    text_rect = t.get_rect()
    text_rect.center = (x, y)
    screen.blit(t, text_rect)


def update_screen(reading, shape):
    screen.fill(BLACK)
    print(len(reading))
    for y in range(len(reading)):

        for x in range(len(reading[y])):
            col = reading[y][x]
            col = 255 if col > 255 else col
            pygame.draw.rect(screen, (col, col, col), [x * tile_size, y * tile_size, tile_size, tile_size], 0)
        render_text(str(chr(65 + y)), tile_size // 3, (tile_size // 2 + tile_size * y))  # column labels

    for x in range(len(reading[0])):
        render_text(str(x + 1), 2 + tile_size // 2 + x * tile_size, tile_size // 2)  # row labels

    render_text("Prediction: " + shape, window_size[0] // 2, 420)
    # update screen
    pygame.display.flip()


# -------- Main Loop -----------
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False  # Closes visualizer

    current_reading = collect_reading(ser)
    if current_reading:
        prediction = classifier.classify_object(current_reading)
        shaped_reading = np.reshape(current_reading, (-1, fsr_size[0]))
        update_screen(shaped_reading, prediction)

    # --- Limit to 60 frames per second
    clock.tick(60)
    pygame.display.update()

pygame.quit()
