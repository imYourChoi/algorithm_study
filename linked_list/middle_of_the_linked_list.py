# https://leetcode.com/problems/middle-of-the-linked-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        mid = head
        while head.next:
            head = head.next
            i += 1
            if i % 2 == 0:
                mid = mid.next

        return mid
