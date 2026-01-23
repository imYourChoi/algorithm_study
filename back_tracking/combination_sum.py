# https://leetcode.com/problems/combination-sum/description/?source=submission-ac

from typing import List


def helper(curCands, curNum, target, index, candidates, answer):
    if curNum == target:
        answer.append(list(curCands))
        return
    if curNum > target:
        return

    for i in range(index, len(candidates)):
        num = candidates[i]
        curCands.append(num)
        helper(curCands, curNum + num, target, i, candidates, answer)
        curCands.pop(-1)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        helper([], 0, target, 0, candidates, answer)
        return answer
