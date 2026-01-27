# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))

        if self.min == None or self.min > val:
            self.min = val

    def pop(self) -> None:
        val, tmin = self.stack.pop()
        if tmin == None or val < tmin:
            self.min = tmin

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
