from Utils import Utilities
from abc import ABC, abstractmethod
import pygame
import random
import math
PI=3.14

from sys import exit
screen_size_x=800
screen_size_y=1000

pygame.init()


pygame.init()
class ScoreManager:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.value_increment=10
        
    def update_score(self):
        self.score=self.score+self.value_increment
    def display_score(self, screen):
        # Render the score text
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        # Display the score text on the screen
        screen.blit(score_text, (10, 10))
score_manager = ScoreManager()


class GameObject:
    def draw_throttle_gauge(delta_mass):
        # Determine the position of the throttle gauge on the screen
        throttle_gauge_x = 10
        throttle_gauge_y = 150
        throttle_gauge_width = 20
        throttle_gauge_height = 200
        
        # Calculate the size of the throttle gauge indicator based on delta_mass
        throttle_indicator_height = delta_mass * (throttle_gauge_height / artemis.delta_mass_max)
        
        # Draw the throttle gauge background
        pygame.draw.rect(screen, (100, 100, 100), (throttle_gauge_x, throttle_gauge_y, throttle_gauge_width, throttle_gauge_height))
        
        # Draw the throttle gauge indicator
        pygame.draw.rect(screen, (255, 0, 0), (throttle_gauge_x, throttle_gauge_y + throttle_gauge_height - throttle_indicator_height, throttle_gauge_width, throttle_indicator_height))

    def vector_to_coordinates(vector_length, angle):
        # Convert angle to radians
        angle_rad = math.radians(angle)
        
        # Calculate cosine and sine
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)

        # Determine x and y based on quadrant (using absolute values for cosine and sine)
        y = vector_length * abs(cos_theta)  
        x = vector_length * abs(sin_theta)  
        
        while angle > 360:
            angle = angle - 360
        
        if angle >= 90 and angle < 180:
            x *= 1  # Quadrant II
            y *= -1
        elif angle >= 180 and angle < 270:
            y *= -1  # Quadrant III
            x *= -1
        elif angle >= 270 and angle < 360 or angle < 0:  # Modified condition for 4th quadrant
            x *= -1  # Quadrant IV
        
        return x, y


    def coordinates_to_vector(x, y):
        vector=math.sqrt(x*x+y*y)
        angle=math.asin(y/vector)
        angle=angle*57.29578
        print(f"vector ={vector}, angle = {angle}")
        return(vector, angle)
    
class GameObjectFactory(ABC):
    @abstractmethod
    def create_game_object(self, *args, **kwargs):
        pass

    
class Meteor(GameObject):
    def __init__(self, side, image_path):
        super().__init__()
        self.side = side  # Side of the screen to spawn (0 for left, 1 for right)
        if side == 0:  # Left side
            self.position = [0, random.randint(0, screen_size_y - 50)]  # Random Y position
            self.velocity = [1, 0]  # Moves to the right
        else:  # Right side
            self.position = [screen_size_x - 50, random.randint(0, screen_size_y - 50)]  # Random Y position
            self.velocity = [-1, 0]  # Moves to the left
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Scale the image to 50x50 pixels.convert_alpha()

        # Add any other attributes or behavior specific to meteors

    def update_pos(self):
        # Update meteor position based on velocity
        self.position[0] += self.velocity[0]
        
        # Check if meteor is off the screen
        if self.position[0] < -50 or self.position[0] > screen_size_x:
            # Destroy the meteor instance
            self.destroy()
    def destroy(self):
        # Remove the meteor instance from the game
        # You can perform any cleanup here if needed
        meteors.remove(self)


class MeteorFactory(GameObjectFactory):
    def __init__(self):
        super().__init__()
        self.last_meteor_time = pygame.time.get_ticks()
        self.initial_spawn_interval = 3000  # Initial spawn interval
        self.spawn_interval_reduction_rate = 50  # Rate at which the spawn interval reduces
        self.meteor_spawn_interval = self.initial_spawn_interval  # Current spawn interval
    
    def create_game_object(self, side, image_path):
        if self.check_meteor_timing():
            # Adjust the spawn interval based on game progress
            self.adjust_spawn_interval()
            return Meteor(side, image_path)
        return None
    
    def adjust_spawn_interval(self):
        # Reduce the spawn interval over time
        self.meteor_spawn_interval -= self.spawn_interval_reduction_rate
        if self.meteor_spawn_interval < 500:  # Ensure the spawn interval doesn't become too small
            self.meteor_spawn_interval = 500
    
    def check_meteor_timing(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_meteor_time > self.meteor_spawn_interval:
            # Update the time when the last meteor was created
            self.last_meteor_time = current_time
            return True
        return False



meteor_factory = MeteorFactory()
side = random.randint(0, 1)  # Randomly choose side (0 for left, 1 for right)
meteor = meteor_factory.create_game_object(side, "visuals_test/meteorite.png")  
meteors=[]
meteors.append(meteor)  # Add the meteor to the list of active meteors

class GameOverScreen:
    def __init__(self, screen, font, utilities):
        self.screen = screen
        self.font = font
        self.utilities = utilities

    def display_game_over_screen(self, current_score):
        self.screen.fill((0, 0, 0))  # Fill the screen with black color

        # Render the "Game Over" text
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        game_over_text_rect = game_over_text.get_rect(center=(screen_size_x // 2, screen_size_y // 2 - 50))
        self.screen.blit(game_over_text, game_over_text_rect)

        # Render the current score
        current_score_text = self.font.render(f"Your Score: {current_score}", True, (255, 255, 255))
        current_score_text_rect = current_score_text.get_rect(center=(screen_size_x // 2, screen_size_y // 2))
        self.screen.blit(current_score_text, current_score_text_rect)

        # Render the button text
        button_text = self.font.render("Quit", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=(screen_size_x // 2, screen_size_y // 2 + 100))
        self.screen.blit(button_text, button_text_rect)

        pygame.display.flip()  



        # Wait for the user to click the "Quit" button
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mouse click is within the button rectangle
                    if button_text_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()






class Rocket(GameObject):
    _instance = None #singleton thing
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, mass, delta_mass_max) -> None:
        if not hasattr(self, '_initialized'):
            self.mass=mass
            self.delta_mass_max=delta_mass_max
            self.delta_mass_increment=self.delta_mass_max/50
            self.delta_mass=0
            self.speed_coordintates=[0, 0] #x and y coordinates for speed
            self.acceleration_vector=[0, 0] # vector length and angle(in degrees) from oy axis
            self.acceleration_coordinates=[0, 0] # x and y coordinates
            self.throttle_coordinates=[0, 0]
            self.throttle_vector=[0.1, 0] 
            self.coordinates=[200, 200, 0] # x and y coordinates + angle of the sprite of the rocket
            self._initialized = True # singleton thing
    def draw_rocket(self):
        rocket = rocket_initial
        self.coordinates[2] = self.throttle_vector[1]
        rotated_rocket = pygame.transform.rotate(rocket, self.coordinates[2])
        rotated_rect = rotated_rocket.get_rect()
        blit_position = (self.coordinates[0] - rotated_rect.width / 2, self.coordinates[1] - rotated_rect.height / 2)
        screen.blit(rotated_rocket, blit_position)
        
    def check_out_of_bounds(self, screen_width, screen_height):
        rocket_width = 50  
        rocket_height = 100  
        #lsits of 2 variables, x and y coordinates


        if self.coordinates[0] < rocket_width/2: #check x coortinate colistion
           game_over_screen.display_game_over_screen(score_manager.score)
        elif self.coordinates[0] > screen_width - rocket_width:
            game_over_screen.display_game_over_screen(score_manager.score)

        if self.coordinates[1] < rocket_height/2: # check y coordinate colission
            game_over_screen.display_game_over_screen(score_manager.score)
        elif self.coordinates[1] > screen_height - rocket_height:
            game_over_screen.display_game_over_screen(score_manager.score)
    def display_info(self):
        # commented out, was used to debug 
        aceleration_text = font.render(f"aceleration : {artemis.acceleration_coordinates[1]}", True, (255, 0, 0))  # Red text
        speedx = font.render(f"speed x: {artemis.speed_coordintates[0]}", True, (0, 255, 0))  # Green text
        speedy = font.render(f"speed y: {artemis.speed_coordintates[1]}", True, (0, 255, 0))  # Green text
        text_x = font.render(f"coorinate x: {artemis.coordinates[0]}", True, (0, 255, 0))  # Green text
        text_y = font.render(f"coorinate y: {artemis.coordinates[1]}", True, (0, 255, 0))  # Green text
        screen.blit(aceleration_text, (0,0))
        screen.blit(speedx, (0, 100))
        screen.blit(speedy, (0, 75))
        screen.blit(text_x, (0, 25))
        screen.blit(text_y, (0, 50))
    def calculate_gravity(self, gravity):
        gravity_y=self.mass*gravity
        return gravity_y
    def possition_update(self):
        # list of 2 ints (due to math floats, but blit renders in ints), x and y coordinates respectivly
        self.throttle_coordinates[0], self.throttle_coordinates[1]=GameObject.vector_to_coordinates((-self.throttle_vector[0]*self.delta_mass), self.throttle_vector[1])
        self.acceleration_coordinates[0] = self.throttle_coordinates[0]
        self.acceleration_coordinates[1] = self.calculate_gravity(gravity_coordinates[1]) + self.throttle_coordinates[1]
        self.speed_coordintates[0] = self.speed_coordintates[0] + self.acceleration_coordinates[0]
        self.speed_coordintates[1] = self.speed_coordintates[1] + self.acceleration_coordinates[1]
        self.coordinates[0] = self.coordinates[0] + self.speed_coordintates[0]
        self.coordinates[1] = self.coordinates[1] + self.speed_coordintates[1]
    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            # Increase delta_mass
            if self.delta_mass < self.delta_mass_max:
                self.delta_mass += self.delta_mass_increment
                if self.delta_mass > self.delta_mass_max:
                    self.delta_mass = self.delta_mass_max
            print("w")
        if keys_pressed[pygame.K_s]:
            # Decrease delta_mass
            if self.delta_mass > 0:
                self.delta_mass -= self.delta_mass_increment
                if self.delta_mass < 0:
                    self.delta_mass = 0
            print("s")
        if keys_pressed[pygame.K_d]:
            # Adjust throttle_vector
            self.throttle_vector[1] -= 1
            print("d")
        if keys_pressed[pygame.K_a]:
            # Adjust throttle_vector
            self.throttle_vector[1] += 1
            print("a")
        if keys_pressed[pygame.K_z]:
            # Adjust throttle_vector
            self.delta_mass = self.delta_mass_max
            print("z")
        if keys_pressed[pygame.K_x]:
            # Adjust throttle_vector
            self.delta_mass = 0
            print("x")
    def get_rotated_rect(self):
        # Get the rotated rectangle surrounding the rocket sprite
        rotated_rocket = pygame.transform.rotate(rocket_initial, self.coordinates[2])
        rotated_rect = rotated_rocket.get_rect(center=(self.coordinates[0], self.coordinates[1]))
        return rotated_rect





if __name__ == "__main__":
    # Code to launch the game
    pygame.init()
    screen = pygame.display.set_mode((800, 1000))
    clock = pygame.time.Clock()
    utilities = Utilities()


    user_data = utilities.read_json('user_data.json')
    utilities.run()
    mass = user_data.get('mass', 10)  # Defaulting to 10 if not present in JSON
    delta_mass_max = user_data.get('delta_mass_max', 8)  # Defaulting to 8 if not present in JSON
    artemis=Rocket(mass, delta_mass_max)
    artemis.acceleration_coordinates[0], artemis.acceleration_coordinates[1]=GameObject.vector_to_coordinates(artemis.acceleration_vector[0], artemis.acceleration_vector[1])
    last_meteor_time = pygame.time.get_ticks()
    meteor_spawn_interval = 3000
    screen = pygame.display.set_mode((screen_size_x, screen_size_y))
    pygame.display.set_caption('Delta_orbit')
    clock=pygame.time.Clock()
    space_background=pygame.image.load('visuals_test/Background3.png')
    rocket_full=pygame.image.load('visuals_test/rocket.png')
    trottle_gage1=pygame.image.load('visuals_test/Trottle_gage.png')
    trottle_gage=pygame.transform.scale(trottle_gage1, (20,5))
    rocket=pygame.transform.scale(rocket_full, (50, 100))
    rocket_initial=rocket
    font = pygame.font.SysFont("Times New Roman", 32)
    game_over_screen = GameOverScreen(screen, font, utilities)

    



    gravity_coordinates=[0, 0.05]

    while True:
        current_time = pygame.time.get_ticks()

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit() 
        meteor = meteor_factory.create_game_object(random.randint(0, 1), "visuals_test/meteorite.png")
        if meteor:
            meteors.append(meteor)

        
        artemis.handle_input()
        artemis.possition_update()
        screen.blit(space_background,(0, 0))
        for meteor_instance in meteors:
            if meteor_instance:
                meteor_instance.update_pos()
                screen.blit(meteor_instance.image, (meteor_instance.position))
        # collision detection
        rocket_rotated_rect = artemis.get_rotated_rect()
        score_manager.update_score()


        for meteor_instance in meteors:
            if meteor_instance:
                meteor_rect = pygame.Rect(meteor_instance.position[0], meteor_instance.position[1], 50, 50)  # Meteor rectangle
                if rocket_rotated_rect.colliderect(meteor_rect):
                    # Collision detected, stop the game
                    print("Rocket collided with a meteor!")
                    game_over_screen.display_game_over_screen(score_manager.score)

                meteor_instance.update_pos()
                screen.blit(meteor_instance.image, (meteor_instance.position))

            
        artemis.check_out_of_bounds(screen_size_x+25, screen_size_y+50)
        #artemis.display_info() #commented out, was used for debuging
        artemis.draw_rocket()
        GameObject.draw_throttle_gauge(artemis.delta_mass)
        score_manager.display_score(screen)


        pygame.display.update()
        clock.tick(60)