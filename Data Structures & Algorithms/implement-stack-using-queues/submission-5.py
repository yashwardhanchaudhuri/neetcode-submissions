from collections import deque
class MyStack:

    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        return self.dq.pop()
        

    def top(self) -> int:
        t = self.dq.pop()
        self.dq.append(t)
        return t

    def empty(self) -> bool:
        return True if len(self.dq) == 0  else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()