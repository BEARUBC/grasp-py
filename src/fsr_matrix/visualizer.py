import pygame
import numpy as np

from src.definitions import SETTINGS
from src.fsr_matrix.classifier.matrix_classifier import MatrixClassifier
from src.fsr_matrix.data_processing.reader import DataReader

_BLACK = (0, 0, 0)
_WHITE = (255, 255, 255)


class MatrixVisualizer:
    """
    Visualizer for data gathered from the FSR matrix
    """
    def __init__(self):
        pygame.init()

        self.settings = SETTINGS["fsr_matrix"]["visualizer"]
        self.fsr_dims = SETTINGS["fsr_matrix"]["dims"]
        self.tile_size = self.settings["tile_size"]
        window_size = (self.fsr_dims[0] * self.tile_size,
                       (self.fsr_dims[1] + 1) * self.tile_size)
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Visualizer")
        self.font = pygame.font.SysFont("arial", 15)
        # Loop carries on until the user exits the visualizer
        self.carryOn = True
        # Clock controls refresh rate
        self.clock = pygame.time.Clock()

    def render_text(self, text, x, y):
        t = self.font.render(text, True, _WHITE, _BLACK)
        text_rect = t.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(t, text_rect)

    def update_screen(self, reading, shape):
        self.screen.fill(_BLACK)
        for y in range(len(reading)):

            for x in range(len(reading[y])):
                col = reading[y][x]
                col = 255 if col > 255 else col
                pygame.draw.rect(self.screen, (col, col, col),
                                 [x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size], 0)
            self.render_text(str(chr(65 + y)), self.tile_size // 3,
                             (self.tile_size // 2 + self.tile_size * y))  # column labels

        for x in range(len(reading[0])):
            self.render_text(str(x + 1), 2 + self.tile_size // 2 + x * self.tile_size,
                             self.tile_size // 2)  # row labels

        self.render_text("Prediction: " + shape, self.window_size[0] // 2, 420)
        # update screen
        pygame.display.flip()

    def start(self, reader: DataReader, classifier: MatrixClassifier):
        # -------- Main Loop -----------
        while self.carryOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.carryOn = False  # Closes visualizer

            current_reading = reader.get_frame()
            if current_reading:
                prediction = classifier.classify(current_reading)
                shaped_reading = np.reshape(current_reading, (-1, self.fsr_dims[0]))
                self.update_screen(shaped_reading, prediction)

            # --- Limit to 60 frames per second
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()
