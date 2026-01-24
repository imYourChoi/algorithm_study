# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        self.left.append(x)

    def pop(self) -> int:
        while self.left:
            self.right.append(self.left.pop())
        result = self.right.pop()
        while self.right:
            self.left.append(self.right.pop())
        return result

    def peek(self) -> int:
        while self.left:
            self.right.append(self.left.pop())
        result = self.right[-1]
        while self.right:
            self.left.append(self.right.pop())
        return result

    def empty(self) -> bool:
        return not bool(self.left)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
