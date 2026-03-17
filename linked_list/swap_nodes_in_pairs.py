# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = recent = ListNode(0, head)

        while recent.next and recent.next.next:
            first = recent.next
            second = recent.next.next
            after = recent.next.next.next

            first.next = after
            second.next = first
            recent.next = second

            recent = first

        return root.next
