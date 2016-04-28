from tkinter import Tk, Label, Button, filedialog

# So here's a simple GUI Class I made by looking at some tutorials
# Your thorough comments helped me make more sense of tkinter, so figured I'd try the same.

class TheGUI:

	# the __init__ method makes it possible to make objects of the same class have different
	# attributes/values. the argument self will be the name of the object - in this case myGui -
	# and master will be the first argument passed when creating the object; here it's root (line39).
	def __init__(self, master):

		# stores the value passed to the master parameter in self.master. 
		# in the created object (line 39), this part actually says 'myGui.root = root'
		self.master = master
		master.title('This is Suhvaage')

		# created a button that, when pressed, calls the openMp3 function/method defined below 
		self.openButton = Button(master, text='Choose mp3', command=self.openMp3)
		self.openButton.pack()

	# when you initialize an object, all of its code is defined at that moment.
	# even though the openMp3 function/method is called in self.openButton above,
	# before it has been 'defined', it still works. WOWWOWOWOOWOWOWOOWOWOWOWW cool I guess?
	def openMp3(self):

		# opens 'choose file' window, and... stores some reference to the chosen file in filename.
		# something like that? I guess?
		filename = filedialog.askopenfilename()

		# Just wanted to see that it actually picked the file.
		# what could be here instead is a method from another class that actually plays the mp3.
		print('You have chosen {}'.format(filename))
		
root = Tk()

# This creates an object - named myGui - from the class 'TheGUI'. in the __init__ method,
# the name of the object is automatically cast as the first argument 'self'.
myGui = TheGUI(root)

root.mainloop()



