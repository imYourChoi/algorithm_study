# https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]

        left, right = 0, len(arr)
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid
            else:
                right = mid

        return arr[left][1] if arr[left][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
