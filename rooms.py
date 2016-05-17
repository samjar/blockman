class Room(object):

	# When creating a new room, you type in what rooms, in what direction, they're adjacent to.
	# *args take any number of arguments
	def __init__(self, *args):
		#Lots of init variables to store adjacent rooms in. If there's no adjacent room in
		# a particular direction, just pass False in its argument.
		# when initializing, type the arguments in this order:
		# north, east, south, west, up, down.
		self.north = args[0]
		self.east = args[1]
		self.south = args[2]
		self.west = args[3]
		self.up = args[4]
		self.down = args[5]

	def roomLook(inputText):
		# 

class RoomAwesome(Room):
	def __init__(self, *args):
		super(RoomAwesome, self).__init__(*args)



if __name__ == '__main__':
	
	poopyTest = RoomAwesome('north', 'east', 'south', 'west', 'up', 'down')
	print(poopyTest.down)


		