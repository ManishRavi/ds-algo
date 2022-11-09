#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start

# * Stack Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def makeGood(self, s: str) -> str:
        # * Use stack to store the visited characters.
        stack = []

        for cur_char in list(s):
            # * If the current character make a pair with the last character in the stack,
            # * remove both of them. Otherwise, we add the current character to stack.
            if stack and abs(ord(cur_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(cur_char)

        return "".join(stack)


# @lc code=end
