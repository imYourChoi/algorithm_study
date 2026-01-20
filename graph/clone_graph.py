# https://leetcode.com/problems/clone-graph/description/

from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        queue = deque([node])
        clone = {node.val: Node(node.val)}

        while queue:
            cur = queue.popleft()

            for adj in cur.neighbors:
                if adj.val not in clone:
                    clone[adj.val] = Node(adj.val)
                    queue.append(adj)

                clone[cur.val].neighbors.append(clone[adj.val])

        return clone[node.val]
