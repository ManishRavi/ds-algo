#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start

# * Two Pointers Solution | O(n) Time | O(1) Space
# * n -> The length of s string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_length = len(s)
        if s_length <= 1:
            return True

        left, right = 0, s_length-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

# @lc code=end
