from tkinter import *


class GadgetApp(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)

        # Freddy: added the open door check to the init variables. I think since doorOpen was defined 
        # inside a method/function, every time that method finished executing, the doorOpen variable was destroyed.
        # also changed to boolean values because it makes my brain understand better what's going on.

        self.doorOpen = 0
        self.bananaEat = 0
        self.roomID = 1
        self.HP = 10

        self.go_N = "You walked to the North."
        self.go_S = "You walked to the South."
        self.go_E = "You walked to the East."
        self.go_W = "You walked to the West."
        self.doorString = "You walked straight into the door, you stupid clutz."
        self.doorString_L = "The door is locked. You need a key to open."

        self.keyGet = 0
        self.bananaGet = 1

        self.master.title("Welcome to the Shadowgate-like game. Or something.")
        self.grid()
        self.create_widgets()   

    ########################################################### Widget Creator ################################################################

    def create_widgets(self):

        #Creates the text window that all all the messages gets displayed in (see #30)
        self.text = Text(width = 93, height = 3, wrap = WORD)
        self.text.grid(row = 1, ipady = 10, sticky = W)

        #This is the image widget. The if condition here determines whether I've opened the door (see #34) or not.
        #In order to make the if condition work I have to declare the doorOpen variable (delete #19 and see what I mean).
        #If I could figure out a way to switch images when it loops, I could continue on with my awesome Shadowgate rip-off.

        ## Freddy: made the picture switch into a method instead so I could call the code at #72
        self.changeImage()
        
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
    
    ########################################################### Image Creator ##################################################################

    def changeImage(self):
        if self.doorOpen == 1 and self.roomID == 1:
            self.photo1 = PhotoImage(file = "freddyroom1door.png")
        elif self.doorOpen == 0 and self.roomID == 1:
                #To display an image you first need to create an object and store the PhotImage inside it. 
            #Since Tkinter can't display images just like that, you need to make ANOTHER object, set it as a label and store the last object inside it.
            #Anything else would just be too simple, right?
            self.photo1 = PhotoImage(file = "freddyroom1.png")
        elif self.roomID == 2:
            self.photo1 = PhotoImage(file = "hallway1.png")
        elif self.roomID == 3:
            self.photo1 = PhotoImage(file = "dinoroom.png")

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
        
        #################################################### ROOM 1 ( First Room ) ##############################################################

        if content == "open door" and self.roomID == 1:
            if self.doorOpen == 1:
                message = "The door is already open, you dimwit. Geez."
            else:
                message = "You have opened the door."
                #If you type "open door", it changes the value on doorOpen to 1. It's supposed to change images, but whenever the code loops back
                # to a certain point (see #19) it puts the value back to 0.
            
                # changing the variable to True, and then executes openTheDoor.
                # the doorOpen variable is now outside of the loop, so it will stay at the value we want it to.
                self.doorOpen = 1
                self.changeImage()

        elif content == "look around" and self.roomID == 1:
            message = "You are in a empty, smelly room. There is a door at the end of the room."
        elif content == "go north" and self.roomID == 1 and self.doorOpen == 1:
            message = "" + str(self.go_N) + ""
            self.roomID = 2
            self.changeImage()
        elif content == "go north" and self.roomID == 1 and self.doorOpen == 0:
            self.HP -= 1
            message = "" + str(self.doorString) + " You lost 1 hitpoint."

        #################################################### ROOM 2 ( Hallway with Painting ) ####################################################

        elif content == "go south" and self.roomID == 2:
            message = "" + str(self.go_S) + ""
            self.roomID = 1
            self.changeImage()
        elif content == "go north" and self.roomID == 2:
            self.HP -= 1
            message = "" + str(self.doorString) + " You lost 1 hitpoint."
        elif content == "go west" and self.roomID == 2:
            message = "" + str(self.go_W) + ""
            self.roomID = 3
            self.changeImage()
        elif content == "open door" and self.roomID == 2 and self.keyGet == 0:
            message = "" + str(self.doorString_L) + ""
        elif content == "open door" and self.roomID == 2 and self.keyGet == 1:
            message = "You have opened the door."
            self.keyGet -= 1

        #################################################### Bathing Dino Room ###################################################################   
        
        elif content == "go south" and self.roomID == 3:
            message = "" + str(self.go_S) + ""
            self.roomID = 2
            self.changeImage()


        #################################################### Misc. ###############################################################################
        
        elif content == "help":
            message = "Commands = open [...], use [...], hit [...], go [north, east, south, or west], take [...], look [...]."
        elif content == "use banana" and self.bananaGet == 1:
            if self.bananaEat == 1:
                message = "You have already eaten the banana, you shmuck. Gosh."
            else:
                message = "You ate the banana. You have recovered 1 HP!"
                self.HP += 1
                self.bananaEat = 1
        elif content == "":
            message = ""
            self.text.delete(0.0, END)
        elif content == "hp":
            message = "Hitpoints = " + str(self.HP) + ""
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