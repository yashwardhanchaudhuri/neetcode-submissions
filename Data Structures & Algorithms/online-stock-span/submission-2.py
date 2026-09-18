class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        dist = 1
        if not self.stack:
            self.stack.append([price, 1])
        else:
            counter = len(self.stack) - 1
            while (counter >= 0) and (self.stack[counter][0] <= price):
                dist += self.stack[counter][1]
                counter -= 1
                self.stack.pop()
            self.stack.append([price, dist])
        return dist
        


            
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)