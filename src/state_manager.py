from state import *

class StateManager:
    def __init__(self):
        baseState = State('base', "You've just started the amazing the adventure!")
        successState = State('win!!!1111!!!', "Congratulations, you won! As if it was that hard...")
        
        baseState.set_children({"forward": successState})

        self.current = baseState
        print self.current.description

    def do_the_thing(self, action, target):
        self.current = self.current.go(target)
        print "Moved to " + self.current.name
        print self.current.description


manager = StateManager()
manager.do_the_thing("go", "forward")
