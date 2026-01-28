# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def helper(node):
            if not node:
                return None

            leftVal = helper(node.left)

            if leftVal != None:
                return leftVal

            nonlocal count
            count += 1

            if count == k:
                return node.val

            rightVal = helper(node.right)

            if rightVal != None:
                return rightVal

        return helper(root)
