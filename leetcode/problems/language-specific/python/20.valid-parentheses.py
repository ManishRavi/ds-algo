#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

# * Iterative Stack Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                s_stack.append(char)
            else:
                if (
                    not s_stack
                    or (char == ")" and not s_stack[-1] == "(")
                    or (char == "}" and not s_stack[-1] == "{")
                    or (char == "]" and not s_stack[-1] == "[")
                ):
                    return False

                s_stack.pop()

        return not s_stack


# @lc code=end
