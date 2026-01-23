# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        next = (p.val < root.val > q.val and root.left) or (
            p.val > root.val < q.val and root.right)
        return self.lowestCommonAncestor(next, p, q) if next else root
