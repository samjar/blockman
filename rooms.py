import os
import pygame
# roomStateMachine = StateMachine()


''' 
room class?

roomImg = "path/image"
eventDict = {key is event coordinates: value is event function}


ROOM METHODS:
Check if something should happen at xy click, and if so, execute code.

example:
method openDoor(buttonUsed, clickCoordinates):
	for every eventSpot in room: 
		if mouseCoordinates is in range of event coordinates:
			if buttonUsed is correct for this event:
				return event
'''

class room():

	imgDict = {}

	def __init__(self, imgFolder):
		# the os module gives you ways to interact with file/directory structure
		# of different OS's using code that works for different systems.

		# os.getcwd() gives you, surprise, the current working directory,
		# in other words the folder the executed py-file is in.
		currentDir = os.getcwd()
		# A bit of nested functions here. os.path.join takes strings as
		# arguments and joins them together with the correct / or \ for your os.
		# os.listdir returns a tuple (a list basically) of all files inside the 
		# folder you specify, which we then store in imageList
		imageList = os.listdir(os.path.join(currentDir, imgFolder))

		# Adds a key-value pair to imgDict for every image in
		# specified folder. the key is the images name, and the value
		# is the image loaded into a variable pygame can handle.
		for image in imageList:
			imgPath = os.path.join(currentDir, imgFolder, image)
			# The syntax for adding a key-value pair to a dictionary.
			# The part in [] is the key, right side is the value.
 			self.imgDict[image] = pygame.image.load(imgPath)



if __name__ == '__main__':
	
	testRoom = room('testDir')
	print(testRoom.imgDict)

	print(testRoom.imgDict['4paintingafter.png'])
