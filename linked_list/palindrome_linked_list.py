# https://leetcode.com/problems/palindrome-linked-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        reverse = None

        while fast and fast.next:
            fast = fast.next.next

            # reverse, reverse.next, slow = slow, reverse, slow.next
            temp = slow.next
            slow.next = reverse
            reverse = slow
            slow = temp

        if fast:
            slow = slow.next

        while slow and slow.val == reverse.val:
            slow = slow.next
            reverse = reverse.next

        return not reverse
