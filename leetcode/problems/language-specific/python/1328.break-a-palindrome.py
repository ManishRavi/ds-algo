#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start

# * Greedy Solution | O(n) Time | O(n) Space
# * n -> The length of palindrome string


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome_len = len(palindrome)
        if palindrome_len <= 1:
            return ""

        palindrome_list = list(palindrome)
        for idx, char in enumerate(palindrome_list[: palindrome_len // 2]):
            # * Check for the first non "a" char.
            if char != "a":
                # * If exists, replace it with "a" and return the string.
                palindrome_list[idx] = "a"
                return "".join(palindrome_list)

        # * Else replace the last char with "b" and return the string.
        palindrome_list[-1] = "b"
        return "".join(palindrome_list)


# @lc code=end
