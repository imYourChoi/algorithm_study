# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root):
    if not root:
        return 0

    leftH = helper(root.left)
    rightH = helper(root.right)

    if leftH == -1 or rightH == -1 or abs(leftH - rightH) > 1:
        return -1

    return max(leftH, rightH) + 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return helper(root) != -1
