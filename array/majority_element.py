# https://leetcode.com/problems/majority-element/description/

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]
