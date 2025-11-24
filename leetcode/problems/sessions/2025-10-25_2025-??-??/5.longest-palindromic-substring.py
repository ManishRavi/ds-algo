#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

# * Two Pointers Solution | O(n^2) Time | O(1) Space
# * n -> The length of s string


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""

        def helper(left, right):
            nonlocal longest_palindrome

            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_window_len = right - left + 1
                if cur_window_len > len(longest_palindrome):
                    longest_palindrome = s[left : right + 1]

                left -= 1
                right += 1

        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)

        return longest_palindrome


# @lc code=end
