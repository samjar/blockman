class StateMachine():

    states = {}
    activeState = None
    nextState = None

    def addState(self, *args):
        for state in args:
            self.states.append(state)

    def switchState(self):
        if self.nextState != self.activeState:
            self.activeState = self.nextState







if __name__=="__main__":



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






