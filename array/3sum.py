# https://leetcode.com/problems/3sum/description/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg, zero, pos = [], [], []

        for num in nums:
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)
            else:
                zero.append(num)

        answer = set()

        nSet, pSet = set(neg), set(pos)
        if zero:
            for num in pos:
                if -num in nSet:
                    answer.add((-num, 0, num))
            if len(zero) > 2:
                answer.add((0, 0, 0))

        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                com = -(neg[i] + neg[j])
                if com in pSet:
                    answer.add(tuple(sorted([com, neg[i], neg[j]])))

        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                com = -(pos[i] + pos[j])
                if com in nSet:
                    answer.add(tuple(sorted([com, pos[i], pos[j]])))

        return [list(x) for x in answer]
