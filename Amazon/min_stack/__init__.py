class MinStack(object):
    min_stack = list()
    min_val = list()

    def __init__(self):
        self.min_stack = []
        self.min_val = []

    def push(self, x):
        self.min_stack.append(x)
        if not self.min_val:
            self.min_val.append(x)
        else:
            self.min_val.append(min(x, self.min_val[len(self.min_val) - 1]))

    def pop(self):
        if self.min_stack:
            self.min_stack = self.min_stack[:-1]
            self.min_val = self.min_val[:-1]

    def top(self):
        if not self.min_stack:
            return None
        else:
            return self.min_stack[len(self.min_stack) - 1]

    def getMin(self):
        if not self.min_val:
            return None
        else:
            return self.min_val[len(self.min_val) - 1]
