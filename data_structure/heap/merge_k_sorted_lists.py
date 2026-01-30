# https://leetcode.com/problems/merge-k-sorted-lists/description/

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(heap, (node.val, i))

        if not heap:
            return None

        head = ListNode()
        cur = head

        while heap:
            popVal, popIndex = heapq.heappop(heap)

            cur.next = lists[popIndex]
            cur = cur.next
            lists[popIndex] = lists[popIndex].next

            if lists[popIndex]:
                heapq.heappush(heap, (lists[popIndex].val, popIndex))

        return head.next

        print(heap)
