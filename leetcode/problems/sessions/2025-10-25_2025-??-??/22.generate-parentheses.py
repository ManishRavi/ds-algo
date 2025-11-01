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

        def helper(open, close, stack):
            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                helper(open + 1, close, stack)
                stack.pop()

            if close < open:
                stack.append(")")
                helper(open, close + 1, stack)
                stack.pop()

        helper(0, 0, [])
        return res


# @lc code=end
