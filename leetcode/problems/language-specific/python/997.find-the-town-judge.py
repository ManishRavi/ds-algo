#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start

# * Counting Solution | O(n) Time | O(n) Space
# * n -> The given input


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        person_counts = [0] * (n + 1)
        for a, b in trust:
            person_counts[a] -= 1
            person_counts[b] += 1

        for i in range(1, n + 1):
            if person_counts[i] == n - 1:
                return i

        return -1


# @lc code=end
