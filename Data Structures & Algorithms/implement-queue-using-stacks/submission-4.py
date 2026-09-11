class MyQueue:

    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        return self.dq.popleft()
        

    def peek(self) -> int:
        t = self.dq.popleft()
        self.dq.appendleft(t)
        return t

    def empty(self) -> bool:
        return True if len(self.dq) == 0  else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()