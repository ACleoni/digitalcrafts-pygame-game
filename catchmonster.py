import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Hero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
    
    def render_hero(self,screen):
        hero_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/hero.png').convert_alpha()
        screen.blit(hero_image, (self.x, self.y))
    
    def limits(self,width, height):
        if self.x > width:
            self.x -=5
        if self.y > height:
            self.y -=5
        if self.x < 0:
            self.x = 5

class Monster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def render_monster(self, screen):
        monster_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/monster.png').convert_alpha()
        screen.blit(monster_image, (self.x, self.y))

class Goblin(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def render_goblin(self,screen):
        goblin_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/goblin.png').convert_alpha()
        screen.blit(goblin_image, (self.x, self.y))
        
        

def main():
    #declare size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    hero = Hero(240,220)
    monster = Monster(120,400)
    goblin = Goblin(400,400)
    background_image = pygame.image.load('/Users/alexandercleoni/pygame-project/images/background.png').convert_alpha()
    
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero.y += 5
                    print "move down"
                elif event.key == KEY_UP:
                    hero.y -= 5
                    print "move up"
                elif event.key == KEY_LEFT:
                    hero.x -= 5
                    print "move left"
                elif event.key == KEY_RIGHT:
                    hero.x += 5
                    print "move right"
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        hero.limits(width, height)
        # Draw background
        screen.fill(blue_color)
    
        # Game display
        screen.blit(background_image, (0, 0))
        hero.render_hero(screen)
        monster.render_monster(screen)
        goblin.render_goblin(screen)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
