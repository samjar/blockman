# A simple inventory test for the freddy game. inventory is a dictionary
# The line before every : is the KEY, which we use to access the VALUE
inventory = {'banana': 1, 'apple': 2, 'rat on a stick': 3}

#
 def eatBanana(input):
	if input == 'eat banana' and inventory['banana'] > 0:
		print('You ate the banana!')
		inventory['banana'] -= 1
	else:
		print("You don't have a banana. You are having an existential crisis.")





def printInventory(dictionary):
	for k, v in inventory.items():
		print('{}: {}'.format(k, v))


# Just lines testing to see that it works as planned
userInput = 'eat banana'
eatBanana(userInput)
eatBanana(userInput)
printInventory(inventory)


