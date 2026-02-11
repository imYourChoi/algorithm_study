# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            if left == right:
                return TreeNode(nums[left])

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            if mid - 1 >= 0:
                node.left = helper(left, mid - 1)
            if mid + 1 < len(nums):
                node.right = helper(mid + 1, right)

            return node

        return helper(0, len(nums))
