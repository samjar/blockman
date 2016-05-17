from tkinter import *


class GadgetApp(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)

        # Freddy: added the open door check to the init variables. I think since doorOpen was defined 
        # inside a method/function, every time that method finished executing, the doorOpen variable was destroyed.
        # also changed to boolean values because it makes my brain understand better what's going on.

        # === general switches/variables === #

        self.doorOpen = 0 #checks whether the door in the first room is open or not.
        self.pLadder = 0 #checks whether the painting in 3 has been changed or not.
        self.roomID = 1 #checks which room (image) you're currently in. 
        self.HP = 10 #your hitpoints.

        # === called phrases === #

        self.go_N = "You walked to the North."
        self.go_S = "You walked to the South."
        self.go_E = "You walked to the East."
        self.go_W = "You walked to the West."
        self.doorString = "You walked straight into the door, you stupid clutz."
        self.doorString_L = "The door is locked. You need a key to open."

        # === inventory === #

        self.keyGet = 0 #checks if you have a key in your inventory.
        self.bananaGet = 1 #checks if you have a banana in your inventory.
        self.bananaEat = 0 #checks if you have eaten the banana.

        # === starts the create_widgets() === #

        self.master.title("Welcome to the Shadowgate-like game. Or something.")
        self.grid()
        self.create_widgets()   
        
    ########################################################### Widget Creator ################################################################

    def create_widgets(self):


        #Creates the text window that all all the messages gets displayed in (see #30)
        self.text = Text(width = 110, height = 3, wrap = WORD)
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
        self.master.bind('<Return>', self.textReturn)




    # the new method! Hurraaaay. Dunno what to say about it. Was it necessary? 
    # It's been like 20 minutes since i wrote all this, and I've already forgotten.
    
    ########################################################### Image Creator ##################################################################

    def changeImage(self):

        # === Room 1 ( First Room ) === #

        if self.doorOpen == 1 and self.roomID == 1:
            self.photo1 = PhotoImage(file = "1firstroomdoor.png")
        elif self.doorOpen == 0 and self.roomID == 1:
                #To display an image you first need to create an object and store the PhotImage inside it. 
            #Since Tkinter can't display images just like that, you need to make ANOTHER object, set it as a label and store the last object inside it.
            #Anything else would just be too simple, right?
            self.photo1 = PhotoImage(file = "1firstroom.png")

        # === Room 2 ( Hallway ) === #

        elif self.roomID == 2:
            self.photo1 = PhotoImage(file = "2hallway.png")

        # === Room 3 ( Dino Room ) === #

        elif self.roomID == 3:
            self.photo1 = PhotoImage(file = "3dinoroom.png")

        # === Room 4 ( Looking at Painting ) === #

        elif self.roomID == 4 and self.pLadder == 1:
            self.photo1 = PhotoImage(file = "4paintingafter.png")        
        elif self.roomID == 4 and self.pLadder == 0:
            self.photo1 = PhotoImage(file = "4painting.png")

        # === Room 5 ( Inside the Painting ) === #

        elif self.roomID == 5:
            self.photo1 = PhotoImage(file = "5paintingchest.png")

        # put this outside of the else statement. While trying stuff, I hypothesized another reason the picture wasn't changing:
        # even though the self.photo1 variable was changed, the labelPhoto1 didn't change with it. It was referencing what was stored 'inside'
        # self.photo1 at the point in time, not the variable itself. So, putting outside the if/else statements makes it take the latest value every time the method is run.
        labelPhoto1 = Label(self, image = self.photo1)
        labelPhoto1.grid(row = 0, sticky = W)

    #Defining the textReturn function, that display text in the text widget (see #13) whenever you type something and press the Submit button.
    def textReturn(self, poop):
        #Whatever you have typed in SubmitEntry (see #37) will get stored in the "content" object.
        content = self.submitEntry.get()
        print(self, poop)
        #Here it checks the "content" object for strings that you've entered into the entry field. Whenever you get a correct string, it stores
        # a new string into the "message" object.
        
        #################################################### 1. First Room #######################################################################

        # === Go Commands === #

        if content == "go north" and self.roomID == 1 and self.doorOpen == 1: #if you go north AFTER opening the door.
            message = "" + str(self.go_N) + ""
            self.roomID = 2
            self.changeImage()
        elif content == "go north" and self.roomID == 1 and self.doorOpen == 0: #if you try to go north before opening the door first.
            self.HP -= 1
            message = "" + str(self.doorString) + " You lost 1 hitpoint." #displays the doorString when you run into a door.

        # === Open Commands === #

        elif content == "open door" and self.roomID == 1:
            if self.doorOpen == 1:
                message = "The door is already open, you dimwit. Geez."
            else:
                message = "You have opened the door."
            
                # changing the variable to True, and then executes openTheDoor.
                # the doorOpen variable is now outside of the loop, so it will stay at the value we want it to.
                self.doorOpen = 1
                self.changeImage()

        # === Look Commands === #

        elif content == "look around" and self.roomID == 1:
            message = "You are in a empty, smelly room. There is a door at the end of the room."
        elif content == "look at door" and self.roomID == 1 and self.doorOpen == 0:
            message = "You see a wooden door. It's closed, but not locked as far as you can tell."
        elif content == "look at door" and self.roomID == 1 and self.doorOpen == 1:
            message = "You see an open door. It leads into the hallway. Try walking through it, you bloody moron."
        

        #################################################### 2. Hallway ##########################################################################

        # === Go Commands === #

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

        # === Open Commands === #

        elif content == "open door" and self.roomID == 2 and self.keyGet == 0:
            message = "" + str(self.doorString_L) + ""
        elif content == "open door" and self.roomID == 2 and self.keyGet == 1:
            message = "You have opened the door."
            self.keyGet -= 1
        
        # === Look Commands === #

        elif content == "look around" and self.roomID == 2:
            message = ("You're in a hallway with a large painting hanging on the wall, and an odd, purple gadget of some sorts hanging on the "
                "the opposite wall. There's a locked door to the north, an open passage to the west and another passage to the south.")
        elif content == "look at painting" and self.roomID == 2:
            if self.pLadder == 1:
                message = "You see a house and a tree. You can barely make out the chest behind the house."
                self.roomID = 4
                self.changeImage()
            else:
                message = ("You see a house, a tree and ... strange, sinister-looking creature. Its featureless face makes you "
                    "feel extremely uncomfortable, and even though it seems to have no eyes, it feels like it's staring straight into your soul."
                    "You notice something partially hidden next to the house, but you can't tell what it is. If only you could 'walk around the house'"
                    " to get a better look (type 'leave' to stop looking at the picture).")
                self.roomID = 4
                self.changeImage()

        #################################################### 3. Bathing Dino #####################################################################  
        
        # === Go Commands === #

        elif content == "go south" and self.roomID == 3:
            message = "" + str(self.go_S) + ""
            self.roomID = 2
            self.changeImage()

        #go west
        #climb ladder (same as go west)
        #go north
        #go east
        #go south (back to roomID 2)

        # === Look Commands === #
        
        #look at dino (new image = closeup of dino)
        #look at bathtub
        #look at ladder
        #look at north door
        #look at east door

        # === Talk Commands === # 


        # === 

        #################################################### 4. Painting #########################################################################

        # === Go Commands === #      

        elif content == "leave" and self.roomID == 4:
            message = ""
            self.roomID = 2
            self.changeImage()
        elif content == "walk around the house" and self.roomID == 4:
            message = "You walked around the house. Well, look at that! You found a treasure chest!"
            self.roomID = 5
            self.changeImage()

        # === Look Commands === #



        #################################################### 5. Painting Chest ###################################################################

        # === Go Commands === #

        elif content == "leave" and self.roomID == 5:
            self.pLadder = 1 #leaving the picture makes it so the next time you look at it, the painting will be different
            message = "You left the painting."
            self.roomID = 2
            self.changeImage()
        elif content == "go north" and self.roomID == 5:
            self.pLadder = 1 #leaving the picture makes it so the next time you look at it, the painting will be different
            message = "You left the painting."
            self.roomID = 2
            self.changeImage()
        elif content == "walk around the house" and self.roomID == 5: #takes you to the front of the house, outside the door.
            message = "You walked around the house again. (still working on image)"
        elif content == "go east" and self.roomID == 5:
            message = "" + str(self.go_E) + " (still working on image)" #takes you face-to-face with the creature, who kills you.

        # === Open Commands === #

        elif content == "open chest" and self.roomID == 5:
            message = "The chest is locked."

        # === Look Commands === #

        #look around
        #chest
        #house
        #creature ("You remember the creature being to the east of you, but the idea of going there makes you nervous for some reason.")
        

        #################################################### Cheats ##############################################################################

        # === added some cheat commands for various purposes, like teleporting to any room, check the values of variables, etc === #

        elif content == "cheat go 1": #takes you to the first room.
            message = "" #teleporting erases current text.
            self.roomID = 1
            self.changeImage()
        elif content == "cheat go 1b": #if you wanted to go back to the first room BEFORE the door was opened.
            message = ""
            self.doorOpen = 0  
            self.roomID = 1
            self.changeImage()
        elif content == "cheat go 2": #takes you to the hallway.
            message = ""
            self.roomID = 2
            self.changeImage()
        elif content == "cheat go 3": #takes you to the bathing dino.
            message = ""
            self.roomID = 3
            self.changeImage()
        elif content == "cheat go 4": #takes you to the looking at the painting.
            message = ""
            self.roomID = 4
            self.changeImage()
        elif content == "cheat go 4b": #supposed to take you back to the painting before it changes, but it's not working.
            message = ""
            self.roomID = 4
            self.pLadder = 0
            self.changeImage()
        elif content == "cheat go 5": #takes you to inside of the painting, behind the house.
            message = ""
            self.roomID = 5
            self.changeImage()
        elif content == "cheat check var": #command to check the values of different variables. 
            message = "openDoor = " + str(self.doorOpen) + ", pLadder = " + str(self.pLadder) + ", roomID = " + str(self.roomID) + ", bananaEat = " + str(self.bananaEat) + ""

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
            message = "You can't do that."
            self.bell()

        self.submitEntry.delete(0, END)    
        #This line deletes any previous strings from the text widgets (see #13)
        self.text.delete(0.0, END)
        #And this line takes the string we've got stored in the "message" object, and inserts it into the text widget (see #13)
        self.text.insert(0.0, message)


root = Tk()
gApp = GadgetApp(root)
root.geometry("905x630")
root.mainloop()