#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start

# * Recursive Backtracking Solution | O((4^n)/√n) Time | O((4^n)/√n) Space
# * n -> Given n pairs

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generateParenthesisHelper(stack=[], open=0, close=0):
            if open == close == n:
                result.append(''.join(stack))
                return

            if open < n:
                stack.append('(')
                generateParenthesisHelper(stack, open+1, close)
                stack.pop()

            if close < open:
                stack.append(')')
                generateParenthesisHelper(stack, open, close+1)
                stack.pop()

        generateParenthesisHelper()
        return result

# @lc code=end
