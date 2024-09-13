
import pygame


pygame.init()

# Constants
WIDTH, HEIGHT = 300, 500  

# Loading the images
CAR1 = pygame.image.load('car1.gif')
CAR2 = pygame.image.load('car2.gif')
BACK = pygame.image.load('road.png')

# Sound effects
point_sound = pygame.mixer.Sound('point.wav')
crash_sound = pygame.mixer.Sound('carcrash.wav')
hit_sound = pygame.mixer.Sound('die.wav')
