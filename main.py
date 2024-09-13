# main.py
import pygame
import random
from constants import WIDTH, HEIGHT, BACK, point_sound, crash_sound
from cars import Car
from audio3d import Audio3D

def game_loop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Car Race Game")
    running = True
    clock = pygame.time.Clock()
    player_car = Car(is_player=True)
    player_car.position = 2  
    enemy_cars = []
    last_spawn_time = pygame.time.get_ticks()  
    spawn_delay = 8000  
    background_y = 0
    background_speed = 3
    audio_system = Audio3D()

    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_car.position > 1:
                    player_car.position -= 1 
                elif event.key == pygame.K_RIGHT and player_car.position < 3:
                    player_car.position += 1  

        
        background_y = (background_y + background_speed) % BACK.get_height()

       
        if current_time - last_spawn_time >= spawn_delay:
            enemy_position = random.randint(1, 3)  
            enemy_car = Car(is_player=False)
            enemy_car.position = enemy_position
            enemy_cars.append(enemy_car)
            last_spawn_time = current_time  

        screen.fill((0, 0, 0))
        for y_offset in range(-BACK.get_height(), HEIGHT, BACK.get_height()):
            screen.blit(BACK, (0, background_y + y_offset))

        player_car.draw_car(screen)
        for car in enemy_cars:
            car.move_car()
            car.draw_car(screen)
            if car.check_collision(player_car):
                crash_sound.play()
                running = False
            if abs(car.y - player_car.y) < 100:  
       
                lateral_difference = car.position - player_car.position
        
                vertical_proximity = (HEIGHT - car.y) / HEIGHT  
                azimuth = lateral_difference * 30 * vertical_proximity  
                audio_system.play_3d_sound(azimuth)
            # if abs(car.y - player_car.y) < 100:  # Close proximity for audio effect
            #     azimuth = (car.position - player_car.position) * 30
            #     audio_system.play_3d_sound(azimuth)

        
        enemy_cars = [car for car in enemy_cars if car.y < HEIGHT]

        pygame.display.flip()
        clock.tick(30)

    audio_system.close_audio()
    pygame.quit()

game_loop()
