# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            toPush = heapq.heappushpop(self.right, num)
            heapq.heappush(self.left, -toPush)
        else:
            toPush = heapq.heappushpop(self.left, -num)
            heapq.heappush(self.right, -toPush)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
