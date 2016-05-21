import pygame
import time 

pygame.init() #initializes pygame. A must for every pygame program.

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
#defining the colors ahead of time so I can easily call them when needed.

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

# === Clock/FPS === #
clock = pygame.time.Clock() #puts the pygame clock/fps function into a variable called clock. We'll call it later in the loop function.

FPS = 50 #Sets the Frames Per Second. It's super high by default, and you don't want to waste CPU on a simple so a low number will do. If I understand
# it right, it uses the clock function to determine how many times the loop (see below) is displayed on the screen per second. 

# === Font/Text === #

font = pygame.font.SysFont(None, 25) #defines the font used in text for our game. SysFont is one of the default system fonts. Parameters = (name, size, bold = false, italic = false)


regMouseOff = 0
#######################################################################################################################################################################################

def GUI_buttons(x, w, y, h, button, new_cursor, button2):

	#I wanted the mouse cursor to stay the same after you stop holding the button down. So I made the else condition at the end only turn the mouse cursor back to visible
	# if regMouseOff was set to 0. The plan was that once you actually click the button, regMouseOff gets set to 1, thus skipping the else condition.
	#BUT.... if I do that it gives me crap about how "refMouseOff is referenced before assignement" no matter what I do. The only solution I've found to this is 
	# to define regMouseOff = 0 at the beginning of the function... but then the else condition is always running, therefor once you stop holding the mouse-button
	# down, the new mouse cursor disappears and gets replaced with the default one. Uggggggghhhhh!
	global regMouseOff

	click = pygame.mouse.get_pressed() #stores the mouse buttons being pressed into click.
	mouseBar = pygame.mouse.get_pos() #stores the current mouse position into mouseBar.
	mx, my = pygame.mouse.get_pos() #stores the current mouse position into mx, and my.
	mx -= new_cursor.get_width()/2 
	my -= new_cursor.get_height()/2 
	#Gets the center of the new cursor image.
	if x + w > mouseBar[0] > x and y + h > mouseBar[1] > y: # FREDDY EDIT (from now on.... Freddit.): if mouse coordinates is inside the box, then:
	#Kinda hard to explain. Basically, if the button's x coord and width is larger than the mouse's current x coord and if THAT is larger than the x coord of the button
	# AAAAND the button's y coord and height is larger than the mouse coord and if THAT is larger than the y coord of the button, THEN:
		gameDisplay.blit(button, (x, y))
		#places the highlighted button image at the x, y location specified in the main() loop below when GUI_buttons is called.
		if click[0] == 1: #[0] is the left-clicker, [1] the middle, [2] the right-clicker.
			pygame.mouse.set_visible(False) #makes the default mouse cursor invisible (DOESN'T WORK AT THE MOMENT)       	
			gameDisplay.blit(new_cursor,(mx, my))
			regMouseOff = 1
	#Swiched around some statements, and added this so regMouseOff can be turned back to 0

	if click[0] == 0:
		pygame.mouse.set_visible(True)
		regMouseOff = 0

	if regMouseOff == 0:
			gameDisplay.blit(button2, (x, y))

	

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

	while not gameExit: #while gameExit is False (which it is until you press the right buttons) run the loop above instead of going to the pygame.quit() code further below.

		while gameOver == True:
			gameDisplay.fill(white) #tells the code to fill the gameDisplay (screen) with the colors assigned to the variable "white".
			message_to_screen("Game Over. c = Replay, q = Quit", red) #calls the message function. Parameters = ("This is a red text", red)
			pygame.display.update() #You have to type this to get all the changes to actually show up on the screen. In this case, the new changes (white screen, red message)

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

		# === Display room, GUI, button, etc images === #

		gameDisplay.fill(white) 
		#Makes the changes to gameDisplay (the window/screen) actually show up. Without this, it would just stay black.
		#We will also use this to clear the screen of the previous screens. Basically it makes the screen a blank sheet.

		gameDisplay.blit(room1_img, (0, 0)) #blits the room image on top of the blank screen 
		gameDisplay.blit(hot_img, (0, 500)) #blits the hotkey bar under the room image
		gameDisplay.blit(h_img, (10, 10)) #blits the heart/hp bar to the upper-left corner
		
		# === Mouse on hotkey GUI === #

		GUI_buttons(0, 111, 500, 50, h_lookB, eC, lookB) 
		GUI_buttons(113, 111, 500, 50, h_openB, oC, openB)
		GUI_buttons(226, 111, 500, 50, h_useB, cC, useB)
		GUI_buttons(338, 111, 500, 50, h_goB, gC, goB)
		#Calls the GUI_buttons function. The numbers are the coordinates, height and width for each of the hotkey buttons.
		#The h_lookB stuff is the highlighted button that gets drawn if the mouse is within the coords of the button,
		# and then lookB is the regular colored button that the code draws on the screen if the the mouse.
		# the eC is the icon the mouse cursor transforms into if you click on each respective button
		# (Doesn't work properly at the moment! You have to hold the mouse button down and you can't move it out 
		# of the box. Working on a solution for this.)

		

	
		pygame.display.update() #updates all the new changes to the screen
		clock.tick(FPS) #Checks the variable further up the code for how many times the loop will cycle each second. 

	
	pygame.quit() 
	quit() #the quit function


main()

