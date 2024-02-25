class MinStack:

    def __init__(self):
        self.stac=[]
        self.min=[]
        

    def push(self, val: int) -> None:
        self.stac.append(val)
        if self.min and self.min[-1]<val:
            return
        self.min.append(val)
        

    def pop(self) -> None:
        if self.min[-1]==self.stac[-1]:
            self.min.pop()
        self.stac.pop()
        

    def top(self) -> int:
        return self.stac[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
