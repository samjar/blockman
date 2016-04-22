from tkinter import * # Imports the windows GUI package

def doNothing ():
  print("Hello, I am a function that does nothing") 
# None of the buttons can do anything yet, so it will just call this 
# empty function that prints a simple message in the python shell.

root = Tk() # To initialize Tkinter, we have to create a Tk root widget. 
            # This is an ordinary window, with a title bar and other 
            # decoration provided by your window manager. You should only 
            # create one root widget for each program, and it must be created 
            # before any other widgets.

# ***** MAIN MENU ***** #

rMenu = Menu(root) # Puts the first menu type under root, our window.
                   # This is the menu that runs horizontally at the top of 
                   # on the window. All other menus from here out will run down
                   # vertically on the main root menu (file, edit, format, view, etc)
root.config(menu = rMenu) # Can't remember what this does.

fileMenu = Menu(rMenu) # Lets the code know that we're gonna place a drop-down menu on the root menu.
rMenu.add_cascade(label = "File", menu = fileMenu) # Adds the "File" drop-down menu to the root menu.
fileMenu.add_command(label = "New Project...", command = doNothing) # Places a label (button) on the drop-down menu, "File", that calls the doNothing function
fileMenu.add_command(label = "Save", command = doNothing)
fileMenu.add_separator() # Adds a separator in between the first 2 labels and 
                         # the last one below. For aesthetic purposes only.
fileMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(rMenu) # Letting the code know that we're placing another drop-down menu next to the first one.
rMenu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Undo", command = doNothing)
editMenu.add_command(label = "Redo", command = doNothing)

root.title("Spooky Drop-Down Menus")
root.geometry('300x250')
root.mainloop() # Loops the widget. This way it doesn't disappear after a millisecond.
