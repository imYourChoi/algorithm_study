# https://leetcode.com/problems/validate-binary-search-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


inf = float("inf")


def helper(node, floor, ceil):
    if not node:
        return True

    if not floor < node.val < ceil:
        return False

    return helper(node.left, floor, node.val) and helper(node.right, node.val, ceil)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return helper(root, -inf, inf)
