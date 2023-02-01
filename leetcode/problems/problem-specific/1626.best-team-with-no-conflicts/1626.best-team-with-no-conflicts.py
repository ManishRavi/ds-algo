#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start

# * Sorting Solution | O(n^2) Time | O(n) Space
# * n -> The length of scores or ages array


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [player for player in zip(scores, ages)]
        players.sort()
        dp = [score for score, _ in players]

        for i in range(len(players)):
            max_score, max_age = players[i]
            for j in range(i):
                _, cur_age = players[j]
                if max_age >= cur_age:
                    dp[i] = max(dp[i], max_score + dp[j])

        return max(dp)


# @lc code=end
