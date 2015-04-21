class State:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_children(self, children):
        self.children = children

    def go(self, direction):
        nextState = self.children[direction]
        if nextState is not None:
            return nextState
        else:
            raise Exception("No " + direction + " child...")
