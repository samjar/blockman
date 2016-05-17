class Player():

	def __init__(self):
		self.inventory = {'Banana': 1, 'Lint': 5, 'Self-loathing': 'Unlimited'}

	# Create the funtions for interacting with the game world.
	def chooseAction(inputText):
		if 'look' in inputText:
			look(inputText)

		elif 'use' in inputText:
			use(inputText)

		elif 'go' in inputText:
			go(inputText)

		elif 'open' in inputText:
			openThing(inputText)

		elif 'inventory' in inputText:
			checkInventory(inputText)

		else:
			print you can't do that

	def look(inputText):

	def use(inputText):
		if item is in inventory:
			call current room's roomUse()

	def go(inputText):
		call current room object's 

	def openThing(inputText):

	def checkInventory(self, inventory):
		for k, v in self.inventory.items():
			# print inventory content to screen
			print("{}: {}".format(k, v))

if __name__ == "__main__":

	freddy = Player()
	freddy.checkInventory(freddy.inventory)

