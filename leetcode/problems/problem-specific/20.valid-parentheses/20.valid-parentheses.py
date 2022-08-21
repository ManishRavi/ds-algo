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
        for c in s:
            if c == '(' or \
                    c == '{' or \
                    c == '[':
                s_stack.append(c)

            else:
                if not s_stack or \
                        c == ')' and not s_stack[-1] == '(' or \
                        c == '}' and not s_stack[-1] == '{' or \
                        c == ']' and not s_stack[-1] == '[':
                    return False

                s_stack.pop()

        return not s_stack

# @lc code=end
