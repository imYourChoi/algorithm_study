# https://leetcode.com/problems/subtree-of-another-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = []

        def finSubRootInRoot(node):
            if not node:
                return None
            if node.val == subRoot.val:
                nodes.append(node)

            finSubRootInRoot(node.left)
            finSubRootInRoot(node.right)

        finSubRootInRoot(root)

        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False

            if x.val != y.val:
                return False

            return isSame(x.left, y.left) and isSame(x.right, y.right)

        for node in nodes:
            if isSame(node, subRoot):
                return True

        return False
