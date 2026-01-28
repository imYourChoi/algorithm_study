# https://leetcode.com/problems/accounts-merge/

from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountMap = {}
        visited = [False] * len(accounts)

        for i in range(len(accounts)):
            account = accounts[i]
            for j in range(1, len(account)):
                email = account[j]
                if email not in accountMap:
                    accountMap[email] = []
                accountMap[email].append(i)

        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in accountMap[email]:
                    dfs(neighbor, emails)

        answer = []

        for i in range(len(accounts)):
            account = accounts[i]
            if visited[i]:
                continue
            emails = set()
            dfs(i, emails)
            answer.append([account[0]] + sorted(emails))

        return answer
