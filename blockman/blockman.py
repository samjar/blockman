import pygame
import math
from color import *
from levels import *

# - imports the pygame module into the "pygame" namespace.
from pygame import *

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
mixer.music.load("mathgrant_Space_Blocks.mp3")

""" starts main function """
def main():
	
	gameDisplay = display.set_mode(DISPLAY, FLAGS, DEPTH)
	display.set_caption("The Incredible Block Man!")
	clock = time.Clock()

	mixer.music.play(1)

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

	level = [
	"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
	"P P                          P",
	"P P    PPP          P      P P",
	"P P P       P    P     P   P P",
	"P P              P     P   P P",
	"P P      D                 P P",
	"P P    PPPPPP             PP P",
	"P P   PPPPPPP  PPP    DP   P P",
	"P P   PPPPPPP  PPP PPPPPPPPP P",
	"P P PPPPPPPPP  PPP P         P",
	"P P      PPPP  PPP P         P",
	"P P      PPPP  PPP P         P",
	"P P         P  PPP P         P",
	"P P         P      PP    PPPDP",
	"P PJPPPP    P  PPPPPPP  PPPPPP",
	"P PPPPP    PP  PPP       P   P",
	"P           P  PPP    PPPP   P",
	"P       P   P  PPP  D        P",
	"P     PPPD     PPP         E P",
	"PPPPPPPPPPPPPPJPPPPPPPPPPPPPPP"]


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
			if col == "D":
				d = DeathBlock(x, y)
				platforms.append(d)
				entities.add(d)
			if col == "J":
				j = JumpBlock(x, y)
				platforms.append(j)
				entities.add(j)
			x += 32
		y += 32
		x = 0

	total_level_width  = len(level)*25
	total_level_height = len(level)*30
	camera = Camera(simple_camera, total_level_width, total_level_height)
	entities.add(player)

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
		for y in range(20):
			for x in range(30):
				gameDisplay.blit(bg, (x * 32, y *32))

		camera.update(player)

		# - updates player, then draws everything
		player.update(up, down, left, right, platforms)
		for e in entities:
			gameDisplay.blit(e.image, camera.apply(e))

		#entities.draw(gameDisplay)
		pygame.display.flip()

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

""" the complex camera is supposed to adjust itself if you're at a wall, ceiling, floor, etc 
but doesn't work properly at the moment """
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)


""" create the Entity Class that all platforms/blocks will inherit from """
class Entity(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

""" create the Player class """
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

	def update(self, up, down, left, right, platforms):
		if up:
			# - only jump if on the ground
			if self.onGround == True:
				mixer.Sound.play(soundJump)
				jump_func(self, 7)
		if down:
			# - pressing down doesn't do anything yet
			pass
		if left:
			self.speed_x = -5
		if right:
			self.speed_x = 5
		if not self.onGround:
			# - if player is in air, add gravity
			self.speed_y += 0.3
			# - set the max falling speed
			if self.speed_y > 30:
				self.speed_y = 0
		if not(left or right):
			self.speed_x = 0
		# - increase in x direction
		self.rect.left += self.speed_x
		# - do x-axis collisions
		self.collide(self.speed_x, 0, platforms)
		# - increase in y direction
		self.rect.top += self.speed_y
		# - assuming we're in the air
		self.onGround = False
		# - do  y-axis collisions
		self.collide(0, self.speed_y, platforms)

	""" the collision function """
	def collide(self, speed_x, speed_y, platforms):
		for p in platforms:
			# - check every collision between player and platforms
			if sprite.collide_rect(self, p):
				# - I don't really understand isistance. Yeaaaaah
				if isinstance(p, ExitBlock):
					event.post(event.Event(QUIT))
				elif isinstance(p, DeathBlock):
					mixer.Sound.play(soundHurt)
					time.delay(300)
					self.rect.left = 32
					self.rect.top = 32
				elif isinstance(p, JumpBlock):
					if speed_y > 0:
						# - calls the jump function (doesn't work properly atm)
						# - if you walk on it, it runs twice.
						print("weeeeee")
						mixer.Sound.play(soundJumpBlock)
						jump_func(self, 15)
					else:
						pass


				# re-locates player to the outside of platform x, y 
				# coords if player passes its boundaries
				elif speed_x > 0:
					self.rect.right = p.rect.left
				elif speed_x < 0:
					self.rect.left = p.rect.right
				elif speed_y > 0:
					self.rect.bottom = p.rect.top
					self.onGround = True
					self.speed_y = 0
				elif speed_y < 0:
					self.rect.top = p.rect.bottom
					# - add the code in the comment below to disable "ceiling gliding"
					# - thus making the game much harder.
					#self.speed_y = 0

def jump_func(self, jump_height):
	#sets the jump height to whatever was passed into the argument
	self.jump_height = jump_height
	self.speed_y -= jump_height


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

""" creates the DeathBlock """
class DeathBlock(Platform):
	def __init__(self, x, y):
		Platform.__init__(self, x, y)
		self.image.fill(GREEN)

class JumpBlock(Platform):
	def __init__(self, x, y):
		Platform.__init__(self, x, y)
		self.image.fill(PINK)


# - runs the main function
if(__name__ == "__main__"):
	main()