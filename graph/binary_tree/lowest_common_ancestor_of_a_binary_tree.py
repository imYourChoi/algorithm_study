# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(root, p, q):
    if not root:
        return (False, False, None)

    hasP, hasQ = root.val == p.val, root.val == q.val

    left = helper(root.left, p, q)
    right = helper(root.right, p, q)

    if left[2] or right[2]:
        return (True, True, left[2] or right[2])

    hasP = hasP or left[0] or right[0]
    hasQ = hasQ or left[1] or right[1]

    return (hasP, hasQ, root if hasP and hasQ else None)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return helper(root, p, q)[2]
