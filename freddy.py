from tkinter import *

class GadgetApp(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)

        # Freddy: added the open door check to the init variables. I think since doorOpen was defined 
        # inside a method/function, every time that method finished executing, the doorOpen variable was destroyed.
        # also changed to boolean values because it makes my brain understand better what's going on. 
        self.doorOpen = False


        self.master.title("Welcome to the Shadowgate-like game. Or something.")
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        #Creates the text window that all all the messages gets displayed in (see #30)
        self.text = Text(width = 93, height = 3, wrap = WORD)
        self.text.grid(row = 1, ipady = 10, sticky = W)

        #This is the image widget. The if condition here determines whether I've opened the door (see #34) or not.
        #In order to make the if condition work I have to declare the doorOpen variable (delete #19 and see what I mean).
        #If I could figure out a way to switch images when it loops, I could continue on with my awesome Shadowgate rip-off.

        ## Freddy: made the picture switch into a method instead so I could call the code at #72
        self.openTheDoor()
        
        #The only reason I have a submit button is because I haven't figured out how to just type something in the entry field and press enter.
        #To make it work I made a button that you have to click instead of enter whenever you write something in the entry field.
        ##Actually, I found it, although I can't get it to work yet. It's a binding function of some sorts.
        self.submitButton = Button(self, text ="Submit", command = self.textReturn)
        self.submitButton.grid(row = 3, column = 0, sticky = W)

        #This is the entry field. Whatever you have typed in the field will be stored into submitEntry. 
        self.submitEntry = Entry(width = 50)
        self.submitEntry.grid(row = 2, column = 0, sticky = W)

    # the new method! Hurraaaay. Dunno what to say about it. Was it necessary? 
    # It's been like 20 minutes since i wrote all this, and I've already forgotten.
    def openTheDoor(self):
        if self.doorOpen == 1:
            self.photo1 = PhotoImage(file = "freddyroom1door.png")
        else:
                #To display an image you first need to create an object and store the PhotImage inside it. 
            #Since Tkinter can't display images just like that, you need to make ANOTHER object, set it as a label and store the last object inside it.
            #Anything else would just be too simple, right?
            self.photo1 = PhotoImage(file = "freddyroom1.png")

        # put this outside of the else statement. While trying stuff, I hypothesized another reason the picture wasn't changing:
        # even though the self.photo1 variable was changed, the labelPhoto1 didn't change with it. It was referencing what was stored 'inside'
        # self.photo1 at the point in time, not the variable itself. So, putting outside the if/else statements makes it take the latest value every time the method is run.
        labelPhoto1 = Label(self, image = self.photo1)
        labelPhoto1.grid(row = 0, sticky = W)

    #Defining the textReturn function, that display text in the text widget (see #13) whenever you type something and press the Submit button.
    def textReturn(self):
        #Whatever you have typed in SubmitEntry (see #37) will get stored in the "content" object.
        content = self.submitEntry.get()

        #Here it checks the "content" object for strings that you've entered into the entry field. Whenever you get a correct string, it stores
        # a new string into the "message" object.
        if content == "open door":
            if self.doorOpen == 1:
                message = "The door is already open, you dimwit. Geez."
            else:
                message = "You have opened the door."
                #If you type "open door", it changes the value on doorOpen to 1. It's supposed to change images, but whenever the code loops back
                # to a certain point (see #19) it puts the value back to 0.
            
                # changing the variable to True, and then executes openTheDoor.
                # the doorOpen variable is now outside of the loop, so it will stay at the value we want it to.
                self.doorOpen = 1
                self.openTheDoor()

        elif content == "look around":
            message = "You are in a empty, smelly room. There is a door at the end of the room"
        elif content == "help":
            message = "Commands = open door, look around, eat banana"
        elif content == "eat banana":
                message = "You ate the banana. You feel much better now."
        elif content == "":
            message = ""
            self.text.delete(0.0, END)
        else:
            message = "Invalid Action."
            self.bell()

        #This line deletes any previous strings from the text widgets (see #13)
        self.text.delete(0.0, END)
        #And this line takes the string we've got stored in the "message" object, and inserts it into the text widget (see #13)
        self.text.insert(0.0, message)


root = Tk()
gApp = GadgetApp(root)
root.geometry("905x630")
root.mainloop()