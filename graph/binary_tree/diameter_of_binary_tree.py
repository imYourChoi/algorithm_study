# https://leetcode.com/problems/diameter-of-binary-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root):
    if not root:
        return (-1, -1)

    leftSingle, leftSum = helper(root.left)
    rightSingle, rightSum = helper(root.right)
    leftSingle += 1
    rightSingle += 1

    add = leftSingle + rightSingle
    largest = max(leftSum, rightSum, add)
    return max(leftSingle, rightSingle), largest


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return helper(root)[1]
