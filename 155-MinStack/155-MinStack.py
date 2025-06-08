# Last updated: 6/8/2025, 11:54:55 AM
class MinStack:

    def __init__(self):
        self.stc = []        
        self.minstc = []

    def push(self, val: int) -> None:
        self.stc.append(val)
        if not self.minstc or self.minstc[-1] >= val:
            self.minstc.append(val) 

    def pop(self) -> None:
        if self.stc[-1] == self.minstc[-1]:
            self.minstc.pop()
        self.stc.pop()

    def top(self) -> int:
        return self.stc[-1]
        

    def getMin(self) -> int:
        return self.minstc[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()