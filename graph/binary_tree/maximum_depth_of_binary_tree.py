# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = [0]

        def helper(node, i):
            if not node:
                return

            answer[0] = max(answer[0], i)

            helper(node.left, i + 1)
            helper(node.right, i + 1)

        helper(root, 1)

        return answer[0]
