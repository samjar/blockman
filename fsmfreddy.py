import pygame
import time 


from statemachine import StateMachine

leftClick = False

# So this class is essentially the GUI function you made. I needed objects
# with the code for.. reasons? Something to do with the statemachine.
class GUIButtons():

	def __init__(self, x, w, y, h, hLightButton, newCursor, button):
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.hLightButton = hLightButton
		self.button = button
		self.cursor = newCursor

		self.cursorWidth = newCursor.get_width()
		self.cursorHeight = newCursor.get_height()
		self.cursorCenter = (self.cursorWidth/2, self.cursorHeight/2)

	def blitButton(self, mouseXY):
		mouseX = mouseXY[0]
		mouseY = mouseXY[1]
		# if (self.x < mouseX < (self.x+self.width)
		# and self.y < mouseY):
		# 	gameDisplay.blit(self.hLightButton, (self.x, self.y))
		# else:
		# 	gameDisplay.blit(self.button, (self.x, self.y))
		gameDisplay.blit(self.hLightButton, (self.x, self.y))

	def blitCursor(self, cursor, curcenter, mouseXY):
		x = mouseXY[0] - curcenter[0]
		y = mouseXY[1] - curcenter[1]
		gameDisplay.blit(cursor, (x, y))

# === STATES === #

def stateDefault(isClick, *mouseXY):
	# First we check if a transition should be made.
	# Click and y-axis checked first, since y is the same for all buttons.
	if isClick == True and mouseXY[1] > 500:
		for coord, button in buttonDict.iteritems():
			# Checks this condition for every button in the dictionary.
			# A dictionary consists of pairs of keys and values, and here
			# a for loop is used to go through all of the pairs.
			# the current iterations key value is stored in coord; the 
			# value it's linked to is stored in button.
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				# "If the coordinates of the mouse click were inside the
				# buttons edges, then make the state linked to this button
				# the next state."
				buttonStateMachine.nextState = buttonStateMachine.states[button]
				break

	pygame.mouse.set_visible(True)
	if mouseXY[1] > 500:
		for coord, button in objButtonDict.iteritems():
			if coord[0] < mouseXY[0] < coord[0] + coord[1]:
				button.blitButton(mouseXY)

def stateLook(isClick, *mouseXY):
	if isClick == True:

		# As it is, the default state is the only state that 
		# has to switch to multiple different states. 
		# The others only go back to stateDefault.
		buttonStateMachine.nextState = buttonStateMachine.states['default']		

	pygame.mouse.set_visible(False)
	lookButton.blitButton(mouseXY)
	lookButton.blitCursor(lookButton.cursor, lookButton.cursorCenter, mouseXY)	
	
def stateOpen(isClick, *mouseXY):
	if isClick == True:
		buttonStateMachine.nextState = buttonStateMachine.states['default']

	pygame.mouse.set_visible(False)
	openButton.blitButton(mouseXY)
	openButton.blitCursor(openButton.cursor, 
							openButton.cursorCenter, mouseXY)

def stateUse(isClick, *mouseXY):
	if isClick == True:
		buttonStateMachine.nextState = buttonStateMachine.states['default']

	pygame.mouse.set_visible(False)
	useButton.blitButton(mouseXY)
	useButton.blitCursor(useButton.cursor, 
							useButton.cursorCenter, mouseXY)

def stateGo(isClick, *mouseXY):
	if isClick == True:
		buttonStateMachine.nextState = buttonStateMachine.states['default']

	pygame.mouse.set_visible(False)
	goButton.blitButton(mouseXY)
	goButton.blitCursor(goButton.cursor, 
							goButton.cursorCenter, mouseXY)

pygame.mixer.pre_init()
pygame.init() #initializes pygame. A must for every pygame program.

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#defining the colors ahead of time so I can easily call them when needed.

# === Init Stuff === #

# Here the statemachine object is created. 
# stateDefault is set to be run as the first state.
buttonStateMachine = StateMachine()
buttonStateMachine.activeState = stateDefault
buttonStateMachine.nextState = stateDefault
# The different state functions are added to the states dictionary.
# the left part is the key, the right part the value
buttonStateMachine.states = {
	'default': stateDefault,
    'lookButton': stateLook,
    'openButton': stateOpen,
    'useButton': stateUse,
    'goButton': stateGo
    }

buttonDict = {	
	(0, 111, 500, 50): 'lookButton',
	(113, 111, 500, 50): 'openButton',
	(226, 111, 500, 50): 'useButton',
	(338, 111, 500, 50): 'goButton'  
	}

# === Room Image === #

backgroundImage = "room_pictures/1firstroom.png"

room1_img = pygame.image.load(backgroundImage)

# === GUI Images === #

hotkey_bar = "GUI_images/hotkey_bar.png" #the entire hotkey bar. Gonna split all the buttons up individually, but for now it's all one big image.
heart_image = "GUI_images/heart.png" #HP bar image of a heart. Will sit in the upper-left corner.

button_look = "GUI_images/button_look.png" #image that will show when button is inactive.
button_open = "GUI_images/button_open.png"
button_use = "GUI_images/button_use.png"
button_go = "GUI_images/button_go.png"

hover_button_look = "GUI_images/hover_button_look.png" #image shown when button is hovered over.
hover_button_open = "GUI_images/hover_button_open.png"
hover_button_use = "GUI_images/hover_button_use.png"
hover_button_go = "GUI_images/hover_button_go.png"


hot_img = pygame.image.load(hotkey_bar)
h_img = pygame.image.load(heart_image) 

lookB = pygame.image.load(button_look)
openB = pygame.image.load(button_open)
useB = pygame.image.load(button_use)
goB = pygame.image.load(button_go)

h_lookB = pygame.image.load(hover_button_look)
h_openB = pygame.image.load(hover_button_open)
h_useB = pygame.image.load(hover_button_use)
h_goB = pygame.image.load(hover_button_go)

# === Mouse Cursors === #

eyeball_cursor = "mouse_cursors/eyeball.png" #cursor for when "Look" is selected.
open_cursor = "mouse_cursors/open.png"
cogwheel_cursor = "mouse_cursors/cogwheel.png"
#TAKE cursor
arrow_cursor = "mouse_cursors/arrow.png"
#HIT cursor

eC = pygame.image.load(eyeball_cursor)
oC = pygame.image.load(open_cursor)
cC = pygame.image.load(cogwheel_cursor)
# tC = pygame.image.load(take_cursor)
gC = pygame.image.load(arrow_cursor)
# hC = pygame.image.load(hit_cursor)

# === BUTTON OBJECTS === #
# made a class out the button elements, because I wanted to access
# its values outside of the function.
lookButton = GUIButtons(0, 111, 500, 50, h_lookB, eC, lookB) 
openButton = GUIButtons(113, 111, 500, 50, h_openB, oC, openB)
useButton = GUIButtons(226, 111, 500, 50, h_useB, cC, useB)
goButton = GUIButtons(338, 111, 500, 50, h_goB, gC, goB)
objButtonDict = {
	(0, 111, 500, 50): lookButton,
	(113, 111, 500, 50): openButton,
	(226, 111, 500, 50): useButton,
	(338, 111, 500, 50): goButton
	}
# === Create Window === #

display_width = 900
display_height = 550 
#write the size of the height and width over here so you don't have to keep defining the size in the code after that 
# - especially if you end up changing it further down the line. 

pygame.display.set_caption("Freddy's House of Horrors")
gameDisplay = pygame.display.set_mode((display_width, display_height))
#gameDisplay is our Surface, or window/screen. We're calling pygame and the display functions from it, and setting the width and height to 
# whatever the display_height&width were set to earlier. You can also enter numbers here ((900, 550)). The double parenthesis (or tubal)
# are required for the width and height. There are two more parameters if we want them, anti-aliasing and bit color. For example:
# ((900, 550), 0, 32). 0 means no anti-aliasing and 32 bit color.

# # === SOUNDS === #
pygame.mixer.init()
pygame.mixer.music.load("music/Chippin.mp3")

# === Clock/FPS === #
clock = pygame.time.Clock() #puts the pygame clock/fps function into a variable called clock. We'll call it later in the loop function.

FPS = 60 #Sets the Frames Per Second. It's super high by default, and you don't want to waste CPU on a simple so a low number will do. If I understand
# it right, it uses the clock function to determine how many times the loop (see below) is displayed on the screen per second. 

# === Font/Text === #

font = pygame.font.SysFont(None, 25) #defines the font used in text for our game. SysFont is one of the default system fonts. Parameters = (name, size, bold = false, italic = false)

#######################################################################################################################################################################################


def message_to_screen(msg, color): # example when calling function: ("This is a message in red", red)

	screen_text = font.render(msg, True, color) 
	#So above this function we defined which font we want to use and put it in the variable "font", and now we have to render it. This creates a new Surface with the specified text rendered 
	#on it. Pygame provides no way to directly draw text on an existing Surface (gameDisplay being our surface/window): instead you must use Font.render() to create an image (Surface) of the text, 
	#then blit (explained below) this image onto another Surface.
	gameDisplay.blit(screen_text, [display_width/2, display_height/2])
	#basically blit means to draw a Surface over another surface. In this case we're taking screen_text (from above) and placing it on gameDisplay (our main window/screen).
	#You have to define the location of the text, so I put it in the middle of the screen by dividing both the screen display variables in half.

	#It's worth noting that even after all this, nothing will show up on the screen. NOW you have to type pygame.display.update(), but we do that further below. 

def main():
	gameExit = False #Lets you exit the loop if you press the X.
	gameOver = False #the game over screen. False by default until certain criteria is met (hp < 0, etc). From the gameover screen you can decide if you want to play again.
	pygame.mixer.music.play(-1)
	while not gameExit: #while gameExit is False (which it is until you press the right buttons) run the loop above instead of going to the pygame.quit() code further below.
		
		# Some variables that we want to be updated with every iteration.
		# These are then passed as arguments on line 294.
		leftClick = False
		mouseX, mouseY = pygame.mouse.get_pos()

		while gameOver == True:
			gameDisplay.fill(WHITE) #tells the code to fill the gameDisplay (screen) with the colors assigned to the variable "WHITE".
			message_to_screen("Game Over. c = Replay, q = Quit", RED) #calls the message function. Parameters = ("This is a RED text", RED)
			pygame.display.update() #You have to type this to get all the changes to actually show up on the screen. In this case, the new changes (WHITE screen, RED message)

			for event in pygame.event.get(): #loops the next bit of code until you press one of the keys.
				if event.type == pygame.KEYDOWN: #if a key - any key - is pressed down on your keyboard, go to next line.
					if event.key == pygame.K_q: #if that key happens to be "q" then:
						gameExit = True 
						gameOver = False 
						#stops the gameOver loop and the gameExit loop so the game can quit.

					if event.key == pygame.K_c: #if the key that is pressed down happens to be "c", then:
						main() # goes back to the beginning of main() so the game restarts.

						#We'll need to turn off a lot of variables here so when the game restarts, doors will be closed, bananas will be uneaten... err, naked, bathing dinosaurs will
						# be proudly naked once more. 

						#Also we'll need a better game over screen.

		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: #if the X is press it exits the game.
				gameExit = True
			# Checks when the left mouse button is released, but could use
			# MOUSEBUTTONDOWN to check when it is pressed down as well.
			elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				leftClick = True 

		

		# === Display room, GUI, button, etc images === #

		gameDisplay.fill(WHITE) 
		#Makes the changes to gameDisplay (the window/screen) actually show up. Without this, it would just stay BLACK.
		#We will also use this to clear the screen of the previous screens. Basically it makes the screen a blank sheet.

		gameDisplay.blit(room1_img, (0, 0)) #blits the room image on top of the blank screen 
		gameDisplay.blit(hot_img, (0, 500)) #blits the hotkey bar under the room image
		gameDisplay.blit(h_img, (10, 10)) #blits the heart/hp bar to the upper-left corner
		
		# Run the state function that is at the moment stored in activeState.
		# We also pass the leftClick, mouseX, mouseY values into the function.
		# If we start using more than left click, we'd pass variables that store
		# those button presses or whatever into the function as well.
		runState = buttonStateMachine.activeState(leftClick, mouseX, mouseY)		
		
		buttonStateMachine.switchState() # SWITCH STATE YEAAAAAAAAH
		pygame.display.update() #updates all the new changes to the screen
		clock.tick(FPS) #number of loop iterations/second

	
	pygame.quit() 
	quit() #the quit function


main()

