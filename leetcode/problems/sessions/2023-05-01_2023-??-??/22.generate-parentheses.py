#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start

# * Backtracking Solution | O((4^n)/√n) Time | O((4^n)/√n) Space
# * n -> The given input


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, stack):
            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                dfs(open + 1, close, stack + ["("])

            if close < open:
                dfs(open, close + 1, stack + [")"])

        dfs(0, 0, [])
        return res


# @lc code=end
