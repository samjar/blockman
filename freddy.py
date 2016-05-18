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
look_button = "GUI_images/button_look.png"


hot_img = pygame.image.load(hotkey_bar)
h_img = pygame.image.load(heart_image) 
lookB = pygame.image.load(look_button)

# === Mouse Cursors === #

eyeball_cursor = "mouse_cursors/eyeball.png" #cursor for when "Look" is selected.
#OPEN cursor
#USE cursor
#TAKE cursor
#GO cursor
#HIT cursor

eC = pygame.image.load(eyeball_cursor)
# oC = pygame.image.load(open_cursor)
# uC = pygame.image.load(use_cursor)
# tC = pygame.image.load(take_cursor)
# gC = pygame.image.load(go_cursor)
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

FPS = 30 #Sets the Frames Per Second. It's super high by default, and you don't want to waste CPU on a simple so a low number will do. If I understand
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
		gameDisplay.blit(lookB, (0, 500)) #blits the look button on top of the hotkey bar (hotkey image will be replaced entirely by buttons eventually)

		# === Mouse Icon Change === #

		pygame.mouse.set_visible(False) #set the regular mouse cursor to invisible, so we don't see them both 
		mx, my = pygame.mouse.get_pos() #gets the current position of the mouse cursor and stores the coords in mx and my
		mx -= eC.get_width()/2 
		my -= eC.get_height()/2 
		#this centers the mouse cursor on the new mouse image
		gameDisplay.blit(eC,(mx, my)) #blits the new mouse image on the screen at the current mouse coords


		
		pygame.display.update() #updates all the new changes to the screen
		clock.tick(FPS) #Checks the variable further up the code for how many times the loop will cycle each second. 

	
	pygame.quit() 
	quit() #the quit function


main()

