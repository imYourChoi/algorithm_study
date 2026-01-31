# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderHash = {}
        for i in range(len(inorder)):
            inOrderHash[inorder[i]] = i

        preorderIndex = [0]

        def helper(l, r):
            if l >= r:
                return

            curVal = preorder[preorderIndex[0]]
            inorderIndex = inOrderHash[curVal]

            preorderIndex[0] += 1

            node = TreeNode(curVal)
            node.left = helper(l, inorderIndex)
            node.right = helper(inorderIndex + 1, r)

            return node

        return helper(0, len(inorder))

        # indexHash = {}
        # for i in range(len(inorder)):
        #     indexHash[inorder[i]] = i

        # def helper(pi, parent):
        #     node = TreeNode(preorder[pi])
        #     left, right = pi + 1, pi + 1
        #     lSize, rSize = 0, 0

        #     if left == len(preorder):
        #         return node, 1

        #     if indexHash[preorder[left]] < indexHash[preorder[pi]]:
        #         node.left, lSize = helper(left, indexHash[preorder[pi]])
        #         right += lSize

        #     if right == len(preorder):
        #         return node, lSize + 1

        #     if indexHash[preorder[pi]] < indexHash[preorder[right]] < parent:
        #         node.right, rSize = helper(right, parent)

        #     return node, lSize + 1 + rSize

        # return helper(0, 3000)[0]
