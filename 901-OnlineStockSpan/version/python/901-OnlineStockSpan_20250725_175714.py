# Last updated: 7/25/2025, 5:57:14 PM
class StockSpanner:

    def __init__(self):
        self.stc = []
        self.index = 1
        

    def next(self, price: int) -> int:
        self.index += 1
        while self.stc and self.stc[-1][0] <= price:
            self.stc.pop()
        a = 1 if not self.stc else self.stc[-1][1]
        ans = self.index - a 
        self.stc.append([price,self.index])
        return ans




        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)