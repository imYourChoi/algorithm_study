# https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(left, right):
            if not left and not right:
                return True
            if bool(left) ^ bool(right):
                return False
            if left.val != right.val:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)

        if not root:
            return True

        return helper(root.left, root.right)
