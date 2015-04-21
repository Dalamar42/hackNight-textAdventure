class State:
    def __init__(self, children):
        self.children = children
    
    def go(self, direction):
        nextState = children[direction]
        if nextState is not None:
            return nextState
        else:
            raise Exception("No " + direction + " child...")
