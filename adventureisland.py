import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_SPACE = 277

class Hero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def render_hero(self,screen):
        hero_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/maincharacter.png').convert_alpha()
        screen.blit(hero_image, (self.x, self.y))
    
    def limits(self, width, height):
        # Disables the heros ability to move past the trees
        if self.x > width - 180:
            self.x -=2
        if self.y > height - 435:
            self.y -=2
        if self.x < 10:
            self.x +=2
        if self.y < 0:
            self.y +=10
    
    def hero_jump(self):
        self.speed_y = -10
        
        

class Treasure(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render_treasure(self, screen):
        treasure_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/treasure.png').convert_alpha()
        screen.blit(treasure_image, (self.x, self.y))

class Goblin(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def render_goblin(self,screen):
        #goblin_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/goblin.png').convert_alpha()
        screen.blit(goblin_image, (self.x, self.y))       
       

def main():
    #declare size of the canvas
    width = 1366
    height = 769
    blue_color = (97, 159, 182)  
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen_floor = height - 435
    pygame.display.set_caption('Island Adventure')
    clock = pygame.time.Clock()

    # Game initialization
    hero = Hero(10,334)
    treasure = Treasure(1255,334)
    #goblin = Goblin(400,400)
    background_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/island_background.png').convert_alpha()
    
    

    stop_game = False
    jump_available = True
    physics = {'gravity' : 2}
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                # Activate the corrosponding keys when arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                    # Move down
                elif event.key == KEY_UP:
                    if hero.y < 334:
                        jump_available = False
                    if hero.y >= 334:
                        jump_available = True
                        hero.hero_jump()
                    #if hero.y <()
                    # Move up
                elif event.key == KEY_LEFT:
                    hero.speed_x = -2
                    # Move left
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 2
                    # Move right
            if event.type == pygame.KEYUP:
                # Deactivate the corrosponding keys when arrow key is released
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = physics['gravity']
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True
            


        # Game logic
        hero.update()
        hero.limits(width,height)

        # Draw background
        screen.fill(blue_color)
    
        # Game display
        screen.blit(background_image, (0, 0))
        treasure.render_treasure(screen)
        hero.render_hero(screen)
        #goblin.render_goblin(screen)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
