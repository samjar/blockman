import pygame as pg
import sys
from color import *
from statemachine import StateMachine

pg.init()

WIN_WIDTH = 1200
WIN_HEIGHT = 720

TILESIZE = 16

TILE_WIDTH = 800
TILE_HEIGHT = 720

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
font = pg.font.Font(None, 25)

currentBlock = WHITE

def stateDefault(leftClick, rightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		pass

def stateWhiteBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		print("StateWhiteBlock")
		"""
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
		"""
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]	

def stateBackgroundBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		print("StateBackGroundBlock")
		"""
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
		"""
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def statePlayerBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def stateFinishBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def stateDeathBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def stateJumpBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def stateHiddenBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def stateFakeBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def stateStartBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

def stateWarpBlock(leftClick, RightClick, *mouseXY):
	if leftClick is True:
		for coord, button in buttonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break
	elif rightClick is True:
		buttonStateMachine.nextState = buttonStateMachine.states[default]

buttonStateMachine = StateMachine()
buttonStateMachine.activeState = stateDefault
buttonStateMachine.nextState = stateDefault

buttonStateMachine.states = {
	'default': stateDefault,
    'whiteButton': stateWhiteBlock,
    'blackButton': stateBackgroundBlock,
    'redButton': statePlayerBlock,
    'orangeButton': stateFinishBlock,
    'greenButton': stateDeathBlock,
    'jumpWhiteButton': stateJumpBlock,
    'hiddenButton': stateHiddenBlock,
    'fakeButton': stateFakeBlock,
	'yellowButton': stateStartBlock,
    'pinkButton': stateWarpBlock
    }

buttonDict = {
	(820, 80, 70, 30): 'whiteButton',
	(820, 120, 70, 30): 'blackButton',
	(820, 160, 70, 30): 'redButton',
	(820, 200, 70, 30): 'orangeButton',
	(820, 240, 70, 30): 'greenButton',
	(820, 280, 70, 30): 'jumpWhiteButton',
	(820, 320, 70, 30): 'hiddenButton',
	(820, 360, 70, 30): 'fakeButton',
	(820, 400, 70, 30): 'yellowButton',
	(820, 440, 70, 30): 'pinkButton'
	}

def stateDefault(isClick, *mouseXY):

	if isClick is True:
		pass



def text(text, textpos, color):

	text = font.render(text, 1, color)
	screen.blit(text, textpos)

def big_button(x, y):

	pg.draw.rect(screen, WHITE, (x, y, 70, 30), 2)

def small_button(x, y, color, fill):

	pg.draw.rect(screen, color, (x, y, 30, 30), fill)

def draw_menu():
	pg.draw.rect(screen, WHITE, (800, 0, 400, 720), 5)

	big_button(820, 20)
	big_button(910, 20)
	big_button(1000, 20)

	text("Clear", (830, 27), WHITE)
	text("Save", (924, 27), WHITE)
	text("...", (1010, 27), WHITE)

	small_button(820, 80, WHITE, 0)
	small_button(820, 120, WHITE, 1)
	small_button(820, 160, ORANGE, 0)
	small_button(820, 200, RED, 0)
	small_button(820, 240, GREEN, 0)
	small_button(820, 280, JUMPWHITE, 0)
	small_button(820, 320, WHITE, 1)
	small_button(820, 360, WHITE, 0)
	small_button(820, 400, PINK, 0)
	small_button(820, 440, YELLOW, 0)

	text("F", (829, 367), BLACK)
	text("H", (829, 327), WHITE)

def draw_grid():

	for x in range(0, TILE_WIDTH, TILESIZE):
	    pg.draw.line(screen, JUMPWHITE, (x, 0), (x, TILE_HEIGHT))
	for y in range(0, TILE_HEIGHT, TILESIZE):
	    pg.draw.line(screen, JUMPWHITE, (0, y), (TILE_WIDTH, y))	

def main():

	rectangle = pg.Rect(0, 0, 8, 8)

	leftClick = False
	rightClick = False
	mouseX, mouseY = pygame.mouse.get_pos()

	while 1:

		clock.tick(30)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					pg.quit()
					sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
				print("You have pressed the left mouse button!")
				leftClick = True
			if event.type == pg.MOUSEBUTTONUP and event.button == 1:
				print("You have released the left mouse button!")


		screen.fill(BLACK)
		draw_grid()
		draw_menu()

		runState = buttonStateMachine.activeState(leftClick, rightClick, mouseX, mouseY)		
		buttonStateMachine.switchState() # SWITCH STATE YEAAAAAAAAH

		rectangle.center = pygame.mouse.get_pos()
		pygame.draw.rect(screen, currentBlock, rectangle)

		pg.display.update()




if(__name__ == "__main__"):
	screen = pg.display.set_mode(DISPLAY)
	pg.display.set_caption("Blockman Level Editor")
	clock = pg.time.Clock()
	main()