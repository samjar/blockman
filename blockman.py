import pygame
import math
import random
import sys
from color import *

# - imports the pygame module into the "pygame" namespace.
from pygame import *

from blockmanlevels import BlockManLevels

WIN_WIDTH = 960
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

# - number of bits to use for color
DEPTH = 32
# - which display modes you want to use
FLAGS = 0
#FLAGS = FULLSCREEN, RESIZEABLE

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
soundJump = mixer.Sound("jump.wav")
soundFall = mixer.Sound("fall.wav")
soundHurt = mixer.Sound("hurt.wav")
soundItem = mixer.Sound("item.wav")
soundJumpBlock = mixer.Sound("jumpblock.wav")
soundStompCharge = mixer.Sound("stompcharge.wav")
soundStomp = mixer.Sound("stomp.wav")
soundGravityJump = mixer.Sound("bigjump.wav")
soundBoop1 = mixer.Sound("boop1.wav")
soundBoop2 = mixer.Sound("boop2.wav")
soundBoop3 = mixer.Sound("boop3.wav")
soundBoop4 = mixer.Sound("boop4.wav")
soundBoop5 = mixer.Sound("boop5.wav")
mixer.music.load("mathgrant_Space_Blocks.mp3")

blockLevels = BlockManLevels()

class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=WHITE, (pos_x, pos_y)=(0, 0)):
 
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
 
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
 
class GameMenu():
    def __init__(self, screen, items, funcs, bg_color=BLACK, font=None, font_size=30,
                 font_color=WHITE):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.funcs = funcs
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)
 
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            # This line includes a bug fix by Ariel (Thanks!)
            # Please check the comments section of pt. 2 for an explanation
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)

            menu_item.set_position(pos_x, 
                pos_y)
            self.items.append(menu_item)
 
        self.mouse_is_visible = True
        self.cur_item = None
 
    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)
 
    def set_keyboard_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)
 
        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0
 
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(RED)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()
 
    def set_mouse_selection(self, item, mpos):
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            item.set_font_color(RED)
            item.set_italic(True)
        else:
            item.set_font_color(WHITE)
            item.set_italic(False)
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            mpos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            self.funcs[item.text]()
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for item in self.items:
                if self.mouse_is_visible:
                    self.set_mouse_selection(item, mpos)
                self.screen.blit(item.label, item.position)
 
            pygame.display.flip()

""" starts main function """
def main():
    
    gameDisplay = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("The Incredible Block Man!")
    clock = time.Clock()

    mixer.music.set_volume(0.5)
    mixer.music.play(1)

    soundJump.set_volume(0.3)
    soundFall.set_volume(0.3)
    soundHurt.set_volume(0.3)
    soundItem.set_volume(0.3)
    soundJumpBlock.set_volume(0.3)
    soundStompCharge.set_volume(0.3)
    soundStomp.set_volume(0.3)
    soundGravityJump.set_volume(0.3)
    soundBoop1.set_volume(0.3)
    soundBoop2.set_volume(0.3)
    soundBoop3.set_volume(0.3)
    soundBoop4.set_volume(0.3)
    soundBoop5.set_volume(0.3)

    # - sets arrow keys being pressed to OFF
    up = down = left = right = False

    # - creates the background
    bg = Surface((32, 32))
    bg.convert()
    bg.fill(BLACK)

    # - make "entities" a sprite group
    entities = pygame.sprite.Group()

    # - creates player
    player = Player(32, 32)
    entities.add(player)

    platforms = []

    # - defines x, y
    x = y = 0

    current_level = blockLevels.current_level
    level = blockLevels.levels[current_level]

    def build_level(x, y, levelPoop = False):

        x = y = 0

        entities.add(player)

        current_level = blockLevels.current_level
        level = blockLevels.levels[current_level]

        """ build the level """
        # - checks each row and column
        for row in level:
            for col in row:
                # - turn letters into Platforms, add to list and sprite group
                if col == "P":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if col == "E":
                    e = ExitBlock(x, y)
                    platforms.append(e)
                    entities.add(e)
                if col == "C":
                    c = ClearStageBlock(x, y)
                    platforms.append(c)
                    entities.add(c)
                if col == "D":
                    d = DeathBlock(x, y)
                    platforms.append(d)
                    entities.add(d)
                if col == "J":
                    j = JumpBlock(x, y)
                    platforms.append(j)
                    entities.add(j)
                if col == "H":
                    h = HiddenBlock(x, y)
                    platforms.append(h)
                    entities.add(h)
                if col == "F":
                    f = FakeBlock(x, y)
                    platforms.append(f)
                    entities.add(f)
                if col == "S" and levelPoop == False:
                    player.rect.left = x
                    player.rect.top = y
                if col == "L":
                    l = LevelWarp(x, y)
                    platforms.append(l)
                    entities.add(l)
                if col == "W":
                    w = WarpBlock(x, y)
                    platforms.append(w)
                    entities.add(w)

                x += 32
            y += 32
            x = 0

    total_level_width  = len(level)*25
    total_level_height = len(level)*30
    camera = Camera(simple_camera, total_level_width, total_level_height)

    build_level(x, y)

    # - create the game loop

    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT: 
                raise SystemExit, "QUIT"
            if event.type == KEYDOWN and event.key == K_ESCAPE: 
                raise SystemExit, "ESCAPE"
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
            if event.type == KEYDOWN and event.key == K_DOWN:
                down = True
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYUP and event.key == K_DOWN:
                down = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False


        # - draws background
        for y in range(60):
            for x in range(60):
                gameDisplay.blit(bg, (x * 32, y *32))


        camera.update(player)

        if player.endStage == True:
            blockLevels.level_spex()
            entities.empty()
            platforms = []
            build_level(x, y)
            player.endStage = False

        if player.endStage2 == True:
            blockLevels.level_spex()
            entities.empty()
            platforms = []
            build_level(x, y, True)
            player.endStage = False

        # - updates player, then draws everything
        player.update(up, down, left, right, platforms)
        for e in entities:
            gameDisplay.blit(e.image, camera.apply(e))

        #entities.draw(gameDisplay)
        pygame.display.update()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

""" the simple camera follows the player around, with it centered on the screen always """
def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)


""" create the Entity Class that all platforms/blocks will inherit from """
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):

    def __init__(self, x, y):
        Entity.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        # - player starts out not on the ground
        self.onGround = False
        self.image = Surface((32, 32))
        # - converts image to same pixel format as gameDisplay
        self.image.convert()
        self.image.fill(RED)
        self.rect = Rect(x, y, 32, 32)

        self.endStage = False
        self.endStage2 = False
        self.glideOn = False
        self.stompCharge = False

        self.stupidOnGround = False

    # TODO: create code to easier change gravity, player movement
    # and also easier to implement new 'physics'.
    def update(self, up, down, left, right, platforms):
        if up:
            # - only jump if on the ground
            #print self.onGround
            if self.onGround:
                self.stupidOnGround = False
                if blockLevels.current_level == 8:
                    mixer.Sound.play(soundGravityJump)
                else:
                    mixer.Sound.play(soundJump)
                self.jump_func(7, blockLevels.gravityDirection)

                if blockLevels.current_level > 8:
                    blockLevels.current_level += 1
                    if blockLevels.current_level > 13:
                        blockLevels.current_level = 9
                    self.endStage2 = True
        if down:
            if self.stompCharge is True:
                pass
            else:
                if not self.onGround:
                    self.stomp_func(10, blockLevels.gravityDirection)
                # - pressing down doesn't do anything yet
                #pass
        if left:
            if self.stompCharge is True:
                self.speed_x = 0
            else:
                self.move_left(blockLevels.gravityDirection)
        if right:
            if self.stompCharge is True:
                self.speed_x = 0
            else:
                self.move_right(blockLevels.gravityDirection)
        if not self.onGround:
            # function defined at line 292
            self.apply_gravity(blockLevels.gravity, blockLevels.gravityDirection)
            # # - if player is in air, add gravity
        if not(left or right):
            self.stop_moving(blockLevels.gravityDirection)
        # - increase in x direction
        self.rect.left += self.speed_x
        # - do x-axis
        self.collide(self.speed_x, 0, platforms)
        # - increase in y direction
        self.rect.top += self.speed_y
        # - assuming we're in the air
        if self.stupidOnGround is True:
            self.onGround = True
        else:
            self.onGround = False
        # - do  y-axis collisions
        self.collide(0, self.speed_y, platforms)

        #print("stompCharge = " + str(self.stompCharge))
        #print("onGround = " + str(self.onGround))

    """ the collision function """
    def collide(self, speed_x, speed_y, platforms):
        for p in platforms:
            # - check every collision between player and platforms
            if sprite.collide_rect(self, p):
                if self.stompCharge is True:
                    mixer.Sound.play(soundStomp)
                    time.delay(50)
                    self.stompCharge = False            
                # - I don't really understand isistance. Yeaaaaah
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                elif isinstance(p, ClearStageBlock):
                    self.endStage = True
                    blockLevels.current_level += 1                    
                    print blockLevels.current_level
                elif isinstance(p, DeathBlock):
                    mixer.Sound.play(soundHurt)
                    self.endStage = True
                    time.delay(300)
                    self.speed_y = 0
                    self.speed_x = 0
                elif isinstance(p, JumpBlock):
                    if speed_y > 0:
                        # - calls the jump function (doesn't work properly atm)
                        # - if you walk on it, it runs twice.
                        print("weeeeee")
                        mixer.Sound.play(soundJumpBlock)
                        self.jump_func(15, blockLevels.gravityDirection)
                    else:
                        pass
                elif isinstance(p, FakeBlock):
                    #boop = random.randint(1, 5)
                    """ sound is supposed to play when you destroy a FakeBlock,
                    but the sound plays even after the block is gone """
                    #if boop == 1:
                    #    mixer.Sound.play(soundBoop1)
                    #elif boop == 2:
                    #    mixer.Sound.play(soundBoop2)
                    #elif boop == 3:
                    #    mixer.Sound.play(soundBoop3)
                    #elif boop == 4:
                    #    mixer.Sound.play(soundBoop4)
                    #elif boop == 5:
                    #    mixer.Sound.play(soundBoop5)
                    p.kill()
                elif isinstance(p, LevelWarp):
                    blockLevels.little_warp()
                elif isinstance(p, WarpBlock):
                    blockLevels.warp_instance()
                    self.endStage = True

                # re-locates player to the outside of platform x, y
                # coords if player passes its boundaries
                # TODO: add onGround() to elif statements
                elif speed_x > 0:
                    self.rect.right = p.rect.left
                    # self.onGround = self.isOnGround(
                    #                 p, blockLevels.gravityDirection)
                elif speed_x < 0:
                    self.rect.left = p.rect.right
                    self.onGround = self.isOnGround(
                                     p, blockLevels.gravityDirection)
                elif speed_y > 0:
                    self.rect.bottom = p.rect.top
                    # self.onGround = self.isOnGround(
                    #                 p, blockLevels.gravityDirection)
                    self.speed_y = 0
                elif speed_y < 0:
                    self.rect.top = p.rect.bottom
                    # self.onGround = self.isOnGround(
                    #                 p, blockLevels.gravityDirection)
                self.onGround = self.isOnGround(p, blockLevels.gravityDirection)
                    # - add the code in the comment below to disable "ceiling gliding"
                    # - thus making the game much harder.
                    # self.speed_y = 0
                self.glideOn = False

    # First checks gravity direction, then applies gravity in that direction.
    def apply_gravity(self, gravity, direction):
        if direction == 'down':
            self.speed_y += gravity
            if self.speed_y > 30:
                self.speed_y = 0
        elif direction == 'up':
            self.speed_y -= gravity
            if self.speed_y < -30:
                self.speed_y = 0
        elif direction == 'left':
            self.speed_x -= gravity
            if self.speed_x < -30:
                self.speed_x = 0
            # self.speed_y = 0
        elif direction == 'right':
            self.speed_x += gravity
            if self.speed_x > 30:
                self.speed_x = 0
            # self.speed_y = 0

    # Gets called when there's no left/right input
    def stop_moving(self, direction):
        if direction == 'down' or direction == 'up':
            self.speed_x = 0
        else:
            self.speed_y = 0

    # Gets called at left input, acts differently depending on gravity direction
    def move_left(self, direction):
        if direction == 'down' or direction == 'up':
            self.speed_x = -5
        elif direction == 'left':
            self.speed_y = -5
        elif direction == 'right':
            self.speed_y = 5

    def move_right(self, direction):
        if direction == 'down' or direction == 'up':
            self.speed_x = 5
        elif direction == 'left':
            self.speed_y = 5
        elif direction == 'right':
            self.speed_y = -5

    def jump_func(self, jump_height, direction):
        # sets the jump height to whatever was passed into the argument
        self.jump_height = jump_height
        if direction == 'down':
            self.speed_y -= jump_height
        elif direction == 'up':
            self.speed_y += jump_height
        elif direction == 'left':
            self.speed_x = jump_height
        elif direction == 'right':
            self.speed_x -= jump_height

    def stomp_func(self, fall_speed, direction):
        self.stompCharge = True
        self.fall_speed = fall_speed
        mixer.Sound.play(soundStompCharge)
        time.delay(350)
        if direction == 'down':
            self.speed_y += fall_speed
        elif direction == 'up':
            self.speed_y -= fall_speed
        elif direction == 'left':
            self.speed_x -= fall_speed
        elif direction == 'right':
            self.speed_x += fall_speed

    # Check if player is on ground. Ground changes depending on
    # current gravity direction.
    def isOnGround(self, p, direction):
        # If gravity direction is 'down', the function will check
        # collision of players bottom border and platforms top border
        # and return True if collision is detected
        if direction == 'down':
            if self.rect.bottom == p.rect.top:
                return True
        elif direction == 'up':
            if self.rect.top == p.rect.bottom:
                self.stupidOnGround = True
                return True
        elif direction == 'left':
            if self.rect.left == p.rect.right:
                self.stupidOnGround = True
                return True
        elif direction == 'right':
            if self.rect.right == p.rect.left:
                self.stupidOnGround = True
                return True
        return False

        """ prefered function for the FakeBlock isinstance,
        except it's not working properly at the moment """
        #def boop_sound(self):
        #    boop = randrange(1, 5)
        #    self.boop_function(boop)

        #def boop_function(self, number):
        #    mixer.Sound.play(soundBoop(number))


""" creates the platform class, inherit the Entity class """
class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(WHITE)
        self.rect = Rect(x, y, 32, 32)

""" creates the ExitBlock, inherit the platform class """
class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(BLUE)

class ClearStageBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(ORANGE)

""" creates the DeathBlock """
class DeathBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(GREEN)

class JumpBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(JUMPWHITE)

class HiddenBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(BLACK)

class FakeBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(WHITE)

class LevelWarp(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(YELLOW)

class WarpBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(PINK)

class CrackBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(JUMPWHITE)

# - runs the main function
if(__name__ == "__main__"):
    def start_game():
        main()

    def load_game():
        pass
 
    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)
 
    menu_items = ('Start', 'Load Game', 'Quit')
    funcs = {'Start': start_game,
             'Load Game': load_game,
             'Quit': sys.exit}
 
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()
    #main()