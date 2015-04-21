from game_over import GameOver

class State:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_children(self, children):
        self.children = children
    
    def go(self, direction):
        if direction == 'backwards':
            raise GameOver("You got eaten by the Grue!")

        nextState = self.children[direction]
        if nextState is not None:
            return nextState
        else:
            raise Exception("No " + direction + " child...")


class MagicTreeState(State):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def yell(self, target):
        if target == "What am I?":
            print "Victory!"
        else:
            print "The tree yells " + target + " back"

        return self
