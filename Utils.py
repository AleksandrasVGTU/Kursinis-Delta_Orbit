import pygame
import json

class Utilities:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.screen_width = 800
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pygame JSON Input")

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Fonts
        self.font = pygame.font.Font(None, 36)

        # Load button images
        arrow_right1 = pygame.image.load("visuals_test/arrow_key1.png").convert_alpha()
        arrow_left1 = pygame.image.load("visuals_test/arrow_key2.png").convert_alpha()
        submit1 = pygame.image.load('visuals_test/Submit.png')
        load1 = pygame.image.load('visuals_test/load.png')
        self.arrow_left = pygame.transform.scale(arrow_left1, (50, 50))
        self.arrow_right = pygame.transform.scale(arrow_right1, (50, 50))
        self.submit = pygame.transform.scale(submit1, (100, 30))
        self.load = pygame.transform.scale(load1, (100, 30))

        # Initial values
        self.mass = 0
        self.delta_mass = 0

    def read_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

    def write_json(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def create_button(self, x, y, width, height, image=None):
        button_rect = pygame.Rect(x, y, width, height)
        button_data = {"rect": button_rect, "image": image}
        return button_data

    def draw_button(self, button_data):
        pygame.draw.rect(self.screen, self.BLACK, button_data["rect"])
        if button_data["image"]:
            self.screen.blit(button_data["image"], button_data["rect"].topleft)

    def run(self):
        mass_increase_button = self.create_button(350, 50, 50, 50, self.arrow_right)
        delta_mass_increase_button = self.create_button(350, 120, 50, 50, self.arrow_right)
        mass_decrease_button = self.create_button(50, 50, 50, 50, self.arrow_left)
        delta_mass_decrease_button = self.create_button(50, 120, 50, 50, self.arrow_left)
        submit_button = self.create_button(150, 200, 100, 30, self.submit)
        load_button = self.create_button(300, 200, 100, 30, self.load)

        # Main loop
        running = True
        while running:
            self.screen.fill(self.WHITE)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if buttons are clicked
                    if mass_increase_button["rect"].collidepoint(event.pos):
                        self.mass += 0.25
                    elif mass_decrease_button["rect"].collidepoint(event.pos):
                        if (self.mass-0.25 > 0):
                            self.mass = max(0.25, self.mass - 0.25)
                    elif delta_mass_increase_button["rect"].collidepoint(event.pos):
                        self.delta_mass += 0.25
                    elif delta_mass_decrease_button["rect"].collidepoint(event.pos):
                        if (self.delta_mass-0.25 > 0):
                            self.delta_mass = max(0.25, self.delta_mass - 0.25)
                    elif submit_button["rect"].collidepoint(event.pos):
                        if self.mass != 0 and self.delta_mass != 0:
                            user_data = {
                                "mass": self.mass,
                                "delta_mass_max": self.delta_mass
                            }
                            self.write_json(user_data, 'user_data.json')
                            print("Data has been written to user_data.json")
                            running = False
                    elif load_button["rect"].collidepoint(event.pos):
                        # Load data from JSON
                        saved_data = self.read_json('user_data.json')
                        self.mass = saved_data.get("mass", 0)
                        self.delta_mass = saved_data.get("delta_mass_max", 0)

            # Draw buttons
            self.draw_button(mass_increase_button)
            self.draw_button(mass_decrease_button)
            self.draw_button(delta_mass_increase_button)
            self.draw_button(delta_mass_decrease_button)
            self.draw_button(submit_button)
            self.draw_button(load_button)

            # Render text
            text_surface_mass = self.font.render("Mass: " + str(self.mass), True, self.BLACK)
            self.screen.blit(text_surface_mass, (130, 60))
            text_surface_delta_mass = self.font.render("Delta Mass Max: " + str(self.delta_mass), True, self.BLACK)
            self.screen.blit(text_surface_delta_mass, (130, 130))

            pygame.display.flip()

        #pygame.quit()

if __name__ == "__main__":
    utilities = Utilities()
    utilities.run()
