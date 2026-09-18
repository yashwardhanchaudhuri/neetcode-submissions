class MinStack:

    def __init__(self):
        self.mini = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini) == 0:
            self.mini.append(val)
        elif self.mini[-1] >= val:
            self.mini.append(val)

    def pop(self) -> None:
       outs = self.stack.pop()
       if self.mini[-1] == outs:
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
