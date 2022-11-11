#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start

# * Stack Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


# @lc code=end
