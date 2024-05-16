import pygame
import random
import sys

class APIProxy:
    import requests

class APIProxy:
    """Class representing the API proxy for generating random values."""

    def get_random_value(self):
        """Get a random value from an external API."""
        # 예를 들어, 외부 API의 엔드포인트 URL
        api_url = "https://example.com/api/random"
        
        try:
            # 외부 API에 GET 요청을 보냄
            response = requests.get(api_url)
            # 응답에서 무작위 값을 가져옴
            random_value = response.json()['random_value']
            return random_value
        except Exception as e:
            print("Error fetching random value from API:", e)
            # 에러 발생 시 기본값 반환
            return None


class GameIntro:
    """Class responsible for displaying the game's introduction screens."""

    def __init__(self, screen, WIDTH, HEIGHT, BLACK, RED, WHITE, YELLOW, BLUE):
        """Constructor for the GameIntro class.

        Args:
            screen: Pygame surface object representing the game screen.
            WIDTH: Width of the game screen.
            HEIGHT: Height of the game screen.
            BLACK: RGB value representing black color.
            RED: RGB value representing red color.
            WHITE: RGB value representing white color.
            YELLOW: RGB value representing yellow color.
            BLUE: RGB value representing blue color.
        """
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.BLACK = BLACK
        self.RED = RED
        self.WHITE = WHITE
        self.YELLOW = YELLOW
        self.BLUE = BLUE

    def show_start_screen(self):
        """Display the game's start screen and handle user input.

        Returns:
            tuple: Tuple containing rect objects for the start button and how to play button.
        """
        self.screen.fill(self.BLACK) 
        font = pygame.font.Font(None, 72)
        title_text = font.render("METEOR PROTECTOR", True, self.WHITE)
        title_rect = title_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 3))

        font = pygame.font.Font(None, 48)
        start_text = font.render("START", True, self.WHITE)
        start_rect = start_text.get_rect(center=(self.WIDTH // 2 + 150, self.HEIGHT * 2 // 3))

        how_to_play_text = font.render("How to Play?", True, self.WHITE)
        how_to_play_rect = how_to_play_text.get_rect(center=(self.WIDTH // 2 - 150, self.HEIGHT * 2 // 3))

        self.screen.blit(title_text, title_rect)
        pygame.draw.rect(self.screen, self.RED, start_rect)
        pygame.draw.rect(self.screen, self.RED, how_to_play_rect)
        self.screen.blit(start_text, start_rect)
        self.screen.blit(how_to_play_text, how_to_play_rect)
        pygame.display.flip()

        return start_rect, how_to_play_rect

    def show_story_screen(self):
        """Display the game's story screen.

        Returns:
            pygame.Rect: Rect object for the start button.
        """
        self.screen.fill(self.BLACK)  
        story_text = [
            "One day, astronomers observed a strange phenomenon.",
            "It was a rain of countless meteorites pouring down towards Earth.",
            "That phenomenon would occur within five years at the latest.",
            "Meanwhile, the people of Earth have mobilized all their technological capabilities to develop",
            "a high-performance cannon that can push down a meteorite.",
            "And you are the one manning the cannon to protect the Earth.",
            "Good luck! Please protect the Earth!"
        ]

        font = pygame.font.Font(None, 36)
        text_height = font.size("Test")[1]  

        for i, line in enumerate(story_text):
            text = font.render(line, True, self.WHITE)
            text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 3 + i * text_height))
            self.screen.blit(text, text_rect)

        pygame.draw.rect(self.screen, self.BLACK, (self.WIDTH - 100, self.HEIGHT - 50, 80, 30))
        start_text = font.render("Start!", True, self.WHITE)
        start_rect = start_text.get_rect(bottomright=(self.WIDTH - 20, self.HEIGHT - 20))
        self.screen.blit(start_text, start_rect)

        pygame.display.flip()

        return start_rect

    def show_how_to_play_screen(self):
        """Display the screen explaining how to play the game.

        Returns:
            pygame.Rect: Rect object for the start button.
        """
        self.screen.fill(self.BLACK)  
        font = pygame.font.Font(None, 24)
        
        pygame.draw.circle(self.screen, self.RED, (self.WIDTH // 6, self.HEIGHT // 6), 30)

        red_text_1 = font.render("A basic Meteor. As it falls, it gets much bigger.", True, self.WHITE)
        red_text_2 = font.render("Click them to push before they collide", True, self.WHITE)
        self.screen.blit(red_text_1, (self.WIDTH // 3, self.HEIGHT // 6 - 50))
        self.screen.blit(red_text_2, (self.WIDTH // 3, self.HEIGHT // 6 - 20))

        pygame.draw.circle(self.screen, self.YELLOW, (self.WIDTH // 6, self.HEIGHT // 2-30), 5)

        yellow_text_1 = font.render("A high-tech bomb. It will terminate every meteors.", True, self.WHITE)
        yellow_text_2 = font.render("However, since this exists for a very short period of time, you need to check it carefully.", True, self.WHITE)
        self.screen.blit(yellow_text_1, (self.WIDTH // 3, self.HEIGHT // 2 - 50))
        self.screen.blit(yellow_text_2, (self.WIDTH // 3, self.HEIGHT // 2 - 20))

        pygame.draw.rect(self.screen, self.BLUE, (self.WIDTH // 6-100, self.HEIGHT * 5 // 6 - 50, 175, 100))

        blue_text_1 = font.render("Your cannon need a time for cooldown and being cleaned.", True, self.WHITE)
        blue_text_2 = font.render("DO NOT FIRE IT WHEN IT IS BEING CLEANED!!", True, self.WHITE)
        self.screen.blit(blue_text_1, (self.WIDTH // 3, self.HEIGHT * 5 // 6 - 50))
        self.screen.blit(blue_text_2, (self.WIDTH // 3, self.HEIGHT * 5 // 6 - 20))

        start_rect = pygame.Rect(self.WIDTH - 100, self.HEIGHT - 50, 80, 30)
        pygame.draw.rect(self.screen, self.BLACK, start_rect)
        start_text = font.render("Start!", True, self.WHITE)
        start_text_rect = start_text.get_rect(bottomright=(self.WIDTH - 20, self.HEIGHT - 20))
        self.screen.blit(start_text, start_text_rect)

        pygame.display.flip()

        return start_rect

   
class MeteorProtector:
    """Class representing the main game logic and mechanics."""

    def __init__(self, width, height):
        """Constructor for the MeteorProtector class.

        Args:
            width: Width of the game screen.
            height: Height of the game screen.
        """
        self.circles = []
        self.WIDTH = width
        self.HEIGHT = height

        self.START_SCREEN = 0
        self.GAME_SCREEN = 1
        self.HOW_TO_PLAY_SCREEN = 2
        self.STORY_SCREEN = 3  
        self.current_screen = self.START_SCREEN

        self.MARGIN = 100

        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)

        self.INITIAL_RADIUS = 10
        self.MAX_RADIUS = 200
        self.RADIUS_LIMIT = 300
        self.RADIUS_DECREASE_AMOUNT = 100

        self.YELLOW_RADIUS = 5
        self.YELLOW_DURATION = 2000
        self.YELLOW_CIRCLE_COUNT = 0

        self.BLUE_SCREEN_PERIOD_MIN = 15000
        self.BLUE_SCREEN_PERIOD_MAX = 30000
        self.BLUE_SCREEN_DURATION = 2000

        self.time_elapsed_1 = 0
        self.time_elapsed_2 = 0
        self.radius_increase_speed = 0.1

        self.score = 0
        self.level = 1
        self.SCORE_INCREASE_INTERVAL = 10
        self.LEVEL_INCREASE_INTERVAL = 10000

        self.SIZE_INCREASE_INTERVAL = 0

        self.circle_spawn_times = [random.randint(1000, 2000) for _ in range(5)]
        self.time_since_last_circle_spawn = [0] * len(self.circle_spawn_times)

        self.blue_screen_active = False
        self.blue_screen_start_time = 0
        self.blue_screen_period = random.randint(self.BLUE_SCREEN_PERIOD_MIN, self.BLUE_SCREEN_PERIOD_MAX)

        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Meteor Protector")
        self.clock = pygame.time.Clock()

    def generate_random_position(self):
        """Generate a random position within the game screen.

        Returns:
            tuple: Tuple containing random x and y coordinates.
        """
        x = random.randint(self.MARGIN, self.WIDTH - self.MARGIN)
        y = random.randint(self.MARGIN, self.HEIGHT - self.MARGIN)
        return (x, y)

    def create_yellow_circle(self):
        """Create a yellow circle object.

        Returns:
            pygame.Rect: Rect object representing the yellow circle.
        """
        x, y = self.generate_random_position()
        return pygame.draw.circle(self.screen, self.YELLOW, (x, y), self.YELLOW_RADIUS)

    def activate_blue_screen(self):
        """Activate the blue screen effect."""
        if pygame.time.get_ticks() - self.blue_screen_time >= self.blue_screen_period and pygame.time.get_ticks() >= 20000:
            self.blue_screen_active = True
            self.blue_screen_time = pygame.time.get_ticks()
            self.blue_screen_start_time = self.blue_screen_time


    def game_over(self):
        """Handle the game over state."""
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, self.YELLOW)
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text, text_rect)

        score_text = font.render("Score: " + str(self.score), True, self.YELLOW)
        score_rect = score_text.get_rect(top=text_rect.bottom + 20, center=(self.WIDTH // 2, text_rect.bottom + 20))
        self.screen.blit(score_text, score_rect)
        level_text = font.render("Level: " + str(self.level), True, self.YELLOW)
        level_rect = level_text.get_rect(top=score_rect.bottom + 10, center=(self.WIDTH // 2, score_rect.bottom + 10))
        self.screen.blit(level_text, level_rect)

        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    def process_events(self):
        """Process pygame events.

        Returns:
            bool: True if the game is still running, False otherwise.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)
        return True

    def handle_mouse_click(self, pos):
        """Handle mouse click events.

        Args:
            pos: Tuple containing the x and y coordinates of the mouse click.
        """
        if self.yellow_circle and self.yellow_circle.collidepoint(pos):
            self.circles.clear()
            self.yellow_circle = None
        else:
            for circle in self.circles:
                if circle.collidepoint(pos):
                    self.shrink_circle(circle)
                    break

    def shrink_circle(self, circle):
        """Shrink a circle object.

        Args:
            circle: Rect object representing the circle to shrink.
        """
        circle.width -= self.RADIUS_DECREASE_AMOUNT
        circle.height -= self.RADIUS_DECREASE_AMOUNT
        if circle.width <= 0 or circle.height <= 0:
            self.circles.remove(circle)
            self.score += 50 * self.level
            self.YELLOW_CIRCLE_COUNT += 1

    def update_time_elapsed(self):
        """Update the time elapsed since the game started."""
        self.time_elapsed_1 += self.clock.get_rawtime() / 10
        self.time_elapsed_2 += self.clock.get_rawtime()
        for i in range(len(self.circle_spawn_times)):
            self.time_since_last_circle_spawn[i] += self.clock.get_rawtime()
        self.clock.tick(60)

    def update_score_and_level(self):
        """Update the game score and level."""
        if self.time_elapsed_1 >= self.SCORE_INCREASE_INTERVAL:
            self.score += self.level
            self.time_elapsed_1 = 0
        if self.time_elapsed_2 >= self.LEVEL_INCREASE_INTERVAL:
            self.level += 1
            self.radius_increase_speed += 0.1
            self.INITIAL_RADIUS += 5
            self.RADIUS_DECREASE_AMOUNT -= 5
            self.time_elapsed_2 = 0

    def spawn_circles(self):
        """Spawn meteor circles."""
        for i, spawn_time in enumerate(self.circle_spawn_times):
            if self.time_since_last_circle_spawn[i] >= spawn_time:
                x, y = self.generate_random_position()
                radius = self.INITIAL_RADIUS
                circle_rect = pygame.draw.circle(self.screen, self.RED, (x, y), radius)
                self.circles.append(circle_rect)
                self.time_since_last_circle_spawn[i] = 0

    def grow_circles(self):
        """Grow meteor circles."""
        for circle_rect in self.circles[:]:
            pygame.draw.circle(self.screen, self.RED, circle_rect.center, circle_rect.width // 2)
            for i, spawn_time in enumerate(self.circle_spawn_times):
                self.time_since_last_circle_spawn[i] %= spawn_time
            if self.time_elapsed_1 >= self.SIZE_INCREASE_INTERVAL:
                circle_rect.width += 1
                circle_rect.height += 1
                if circle_rect.width >= self.RADIUS_LIMIT:
                    self.game_over()

    def spawn_yellow_circle(self):
        """Spawn a yellow circle."""
        if self.YELLOW_CIRCLE_COUNT == 20 and not self.yellow_circle:
            self.yellow_circle = self.create_yellow_circle()
            self.yellow_circle_creation_time = pygame.time.get_ticks()
            self.YELLOW_CIRCLE_COUNT = 0

    def update_yellow_circle(self):
        """Update the yellow circle."""
        if self.yellow_circle:
            pygame.draw.circle(self.screen, self.YELLOW, self.yellow_circle.center, self.yellow_circle.width // 2)
            if pygame.time.get_ticks() - self.yellow_circle_creation_time >= self.YELLOW_DURATION:
                self.yellow_circle = None

    def show_blue_screen(self):
        """Display the blue screen effect."""
        while self.blue_screen_active and pygame.time.get_ticks() - self.blue_screen_start_time < self.BLUE_SCREEN_DURATION:
            self.screen.fill(self.BLUE)
            font = pygame.font.Font(None, 36)
            text = font.render("CLEANING! PLEASE DON'T FIRE!!", True, self.WHITE)
            text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()

            if pygame.time.get_ticks() - self.blue_screen_start_time >= 500:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.blue_screen_active = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.previous_click_event is None:
                            self.previous_click_event = event
                        else:
                            self.game_over()

    def update_blue_screen_period(self):
        """Update the blue screen period."""
        if not self.blue_screen_active:
            self.blue_screen_period = random.randint(self.BLUE_SCREEN_PERIOD_MIN, self.BLUE_SCREEN_PERIOD_MAX)

    def display_score_and_level(self):
        """Display the game score and level."""
        font = pygame.font.Font(None, 24)
        score_text = font.render("Score: " + str(self.score), True, self.WHITE)
        score_rect = score_text.get_rect(top=10, right=self.WIDTH - 10)
        self.screen.blit(score_text, score_rect)
        level_text = font.render("Level: " + str(self.level), True, self.WHITE)
        level_rect = level_text.get_rect(top=score_rect.bottom + 10, right=self.WIDTH - 10)
        self.screen.blit(level_text, level_rect)

    def main_game_loop(self):
        """Main game loop."""
        yellow_circle = None
        blue_screen_time = 20000
        previous_click_event = None
        self.running = True

        while self.running:

            self.screen.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if yellow_circle and yellow_circle.collidepoint(pos):
                        self.circles.clear()
                        yellow_circle = None
                    else:
                        for circle in self.circles:
                            if circle.collidepoint(pos):
                                circle.width -= self.RADIUS_DECREASE_AMOUNT
                                circle.height -= self.RADIUS_DECREASE_AMOUNT
                                if circle.width <= 0 or circle.height <= 0:
                                    self.circles.remove(circle)
                                    self.score += 100 * self.level
                                    self.YELLOW_CIRCLE_COUNT += 1

            self.time_elapsed_1 += self.clock.get_rawtime() / 10
            self.time_elapsed_2 += self.clock.get_rawtime()
            for i in range(len(self.circle_spawn_times)):
                self.time_since_last_circle_spawn[i] += self.clock.get_rawtime()
            self.clock.tick(60)

            if self.time_elapsed_1 >= self.SCORE_INCREASE_INTERVAL:
                self.score += self.level
                self.time_elapsed_1 = 0
            if self.time_elapsed_2 >= self.LEVEL_INCREASE_INTERVAL:
                self.level += 1
                self.radius_increase_speed += 0.1
                self.INITIAL_RADIUS += 5
                self.RADIUS_DECREASE_AMOUNT -= 5
                self.time_elapsed_2 = 0

            for i, spawn_time in enumerate(self.circle_spawn_times):
                if self.time_since_last_circle_spawn[i] >= spawn_time:
                    x, y = self.generate_random_position()
                    radius = self.INITIAL_RADIUS
                    circle_rect = pygame.draw.circle(self.screen, self.RED, (x, y), radius)
                    self.circles.append(circle_rect)
                    self.time_since_last_circle_spawn[i] = 0

            for circle_rect in self.circles[:]:
                pygame.draw.circle(self.screen, self.RED, circle_rect.center, circle_rect.width // 2)
                for i, spawn_time in enumerate(self.circle_spawn_times):
                    self.time_since_last_circle_spawn[i] %= spawn_time
                if self.time_elapsed_1 >= self.SIZE_INCREASE_INTERVAL:
                    circle_rect.width += 1
                    circle_rect.height += 1
                    if circle_rect.width >= self.RADIUS_LIMIT:
                        self.game_over()

            if self.YELLOW_CIRCLE_COUNT == 15 and not yellow_circle:
                yellow_circle = self.create_yellow_circle()
                yellow_circle_creation_time = pygame.time.get_ticks()
                self.YELLOW_CIRCLE_COUNT = 0

            if yellow_circle:
                pygame.draw.circle(self.screen, self.YELLOW, yellow_circle.center, yellow_circle.width // 2)
                if pygame.time.get_ticks() - yellow_circle_creation_time >= self.YELLOW_DURATION:
                    yellow_circle = None

            if pygame.time.get_ticks() - blue_screen_time >= self.blue_screen_period:
                self.blue_screen_active = True
                blue_screen_time = pygame.time.get_ticks()
                self.blue_screen_start_time = blue_screen_time

            previous_click_event = None

            while self.blue_screen_active and pygame.time.get_ticks() - self.blue_screen_start_time < self.BLUE_SCREEN_DURATION:
                self.screen.fill(self.BLUE)
                font = pygame.font.Font(None, 36)
                text = font.render("CLEANING! PLEASE DON'T FIRE!!", True, self.WHITE)
                text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
                self.screen.blit(text, text_rect)
                pygame.display.flip()

                if pygame.time.get_ticks() - self.blue_screen_start_time >= 1000:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.blue_screen_active = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if previous_click_event is None:
                                previous_click_event = event
                            else:
                                self.game_over()

            previous_click_event = None

            if not self.blue_screen_active:
                self.blue_screen_period = random.randint(self.BLUE_SCREEN_PERIOD_MIN, self.BLUE_SCREEN_PERIOD_MAX)

            font = pygame.font.Font(None, 24)
            score_text = font.render("Score: " + str(self.score), True, self.WHITE)
            score_rect = score_text.get_rect(top=10, right=self.WIDTH - 10)
            self.screen.blit(score_text, score_rect)
            level_text = font.render("Level: " + str(self.level), True, self.WHITE)
            level_rect = level_text.get_rect(top=score_rect.bottom + 10, right=self.WIDTH - 10)
            self.screen.blit(level_text, level_rect)

            pygame.display.flip()


    def main(self):
        """Main function to run the game."""
        intro = GameIntro(self.screen, self.WIDTH, self.HEIGHT, self.BLACK, self.RED, self.WHITE, self.YELLOW, self.BLUE)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.current_screen == self.START_SCREEN:
                        if start_rect.collidepoint(event.pos):
                            self.current_screen = self.STORY_SCREEN  
                        elif how_to_play_rect.collidepoint(event.pos):
                            self.current_screen = self.HOW_TO_PLAY_SCREEN
                    elif self.current_screen == self.HOW_TO_PLAY_SCREEN:
                        if how_to_play_start_rect.collidepoint(event.pos): 
                            self.current_screen = self.STORY_SCREEN
                    elif self.current_screen == self.STORY_SCREEN:
                        if story_start_rect.collidepoint(event.pos):
                            self.current_screen = self.GAME_SCREEN  
            
            if self.current_screen == self.START_SCREEN:
                start_rect, how_to_play_rect = intro.show_start_screen()
            elif self.current_screen == self.GAME_SCREEN:
                self.main_game_loop()
            elif self.current_screen == self.HOW_TO_PLAY_SCREEN:
                how_to_play_start_rect = intro.show_how_to_play_screen() 
            elif self.current_screen == self.STORY_SCREEN:
                story_start_rect = intro.show_story_screen()

            pygame.display.flip()

if __name__ == "__main__":
    game = MeteorProtector(1400, 800)
    game.main()