
from constants import WIDTH, HEIGHT, CAR1, CAR2
import pygame
import random

class Car:
    def __init__(self, is_player=False):
        self.is_player = is_player
        self.height = 60
        self.width = 60
        self.y = HEIGHT - self.height if self.is_player else -50
        self.speed = 1.5
        self.position = 2 if self.is_player else random.randint(1, 4)

    def draw_car(self, screen):
        lane_width = WIDTH / 3
        x = (self.position - 1) * lane_width + (lane_width - self.width) / 2
        image = CAR2 if self.is_player else CAR1  
        screen.blit(image, (x, self.y))

    def move_car(self):
        if not self.is_player:
            self.y += self.speed

    def check_collision(self, other_car):
        if self.position == other_car.position and abs(self.y - other_car.y) < self.height:
            return True
        return False
