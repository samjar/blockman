# The class whose purpose is to 'catalogue' the different possible states
# and switch between them
class StateMachine():

    # dictionary list of states. in fsmfreddy.py I add keys/values
    # to it on line 112
    states = {}
    activeState = None
    nextState = None

    def addState(self, *args):
        for state in args:
            self.states.append(state)

    # at the end of the main game loop (#293), this is used to change the
    # active state for the next iteration of the loop.
    def switchState(self):
        if self.nextState != self.activeState:
            self.activeState = self.nextState







if __name__=="__main__":


    # This was just some early test code.
    def printShit():
        print("Shit")

    def printPoop():
        print("poop")

    def printFart():
        print("Fart")

    testMachine = StateMachine()
    testMachine.addState(printShit, printPoop, printFart)
    testMachine.states[0]

    print("activeState: {}".format(testMachine.activeState))
    testMachine.nextState = 'poopystate'
    testMachine.setState()
    print("activeState: {}".format(testMachine.activeState))






