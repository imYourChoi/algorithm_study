# https://leetcode.com/problems/lru-cache/description/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        self.remove(self.dict[key])
        self.add(self.dict[key])

        return self.dict[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])

        node = Node(key, value)

        self.add(node)
        self.dict[key] = node

        if len(self.dict) > self.capacity:
            del self.dict[self.head.next.key]
            self.remove(self.head.next)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
