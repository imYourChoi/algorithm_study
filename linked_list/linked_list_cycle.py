# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False

        # if not head:
        #     return False

        # s = set()

        # while head.next:
        #     if head.next in s:
        #         return True

        #     s.add(head.next)
        #     head = head.next
