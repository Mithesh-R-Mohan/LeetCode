class MyQueue:

    def __init__(self):
        self.istack = []
        self.ostack = []

    def push(self, x):
        self.istack.append(x)

    def pop(self):
        self.peek()
        return self.ostack.pop()

    def peek(self):
        if not self.ostack:
            while self.istack:
                self.ostack.append(self.istack.pop())
        return self.ostack[-1]

    def empty(self):
        return not self.istack and not self.ostack