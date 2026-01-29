# https://leetcode.com/problems/binary-tree-right-side-view/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def helper(node, h):
            if not node:
                return

            if len(answer) < h:
                answer.append(node.val)

            helper(node.right, h + 1)
            helper(node.left, h + 1)

        helper(root, 1)

        return answer
