# Last updated: 7/20/2025, 6:37:45 PM
from queue import LifoQueue
class MyQueue:

    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()

    def push(self, x: int) -> None:
        while not self.input.empty():
            self.output.put(self.input.get())
        
        self.input.put(x)
        # Pop out elements from the stack output and push them into the stack input
        while not self.output.empty():
            self.input.put(self.output.get())
        
        

    def pop(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        val = self.input.get()
        return val
        

    def peek(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        return self.input.queue[-1]
        

    def empty(self) -> bool:
        s1 = self.input.qsize()
        if s1 == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()