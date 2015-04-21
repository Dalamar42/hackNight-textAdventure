from state import *

class StateManager:
    def __init__(self):
        baseState = State('base')
        successState = State('win!!!1111!!!')
        
        baseState.set_children({"forward": successState})

        self.current = baseState

    def do_the_thing(self, action, target):
        self.current = self.current.go(target)
        print "Moved to " + self.current.name


manager = StateManager()
manager.do_the_thing("go", "forward")
