# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head
        before = None

        for i in range(n-1):
            front = front.next

        while front.next:
            front = front.next
            before = back
            back = back.next

        if before:
            before.next = back.next
        else:
            head = head.next

        return head
