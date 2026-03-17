# https://leetcode.com/problems/path-sum-ii/description/


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(node, value):
            if not node:
                return

            path.append(node.val)
            added = value + node.val

            if not node.left and not node.right:
                if added == targetSum:
                    result.append(list(path))
            else:
                dfs(node.left, added)
                dfs(node.right, added)

            path.pop()

        dfs(root, 0)

        return result
