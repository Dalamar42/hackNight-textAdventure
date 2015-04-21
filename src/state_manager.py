from state import *

class StateManager:
    def __init__(self):
        baseState = State('base', "You've just started the amazing the adventure!")
        successState = State('win!!!1111!!!', "Congratulations, you won! As if it was that hard...")
        tree = MagicTreeState('tree', "There is a talking tree. Deal with it")
        
        baseState.set_children({"forward": successState})
        successState.set_children({"up": tree})

        self.current = baseState
        print "You are in " + self.current.name
        print self.current.description

    def do_the_thing(self, action, target):
        action_method = getattr(self.current, action)
        self.current = action_method(target)
        print "You are in " + self.current.name
        print self.current.description


if __name__ == '__main__':
    manager = StateManager()
    manager.do_the_thing("go", "forward")
    manager.do_the_thing("go", "up")
    manager.do_the_thing("yell", "Hi?")
    manager.do_the_thing("yell", "What am I?")
