# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root, order, level):
    if not root:
        return order

    if len(order) <= level:
        order.append([])

    order[level].append(root.val)

    helper(root.left, order, level + 1)
    helper(root.right, order, level + 1)

    return order


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        return helper(root, [], 0)
