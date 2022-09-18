#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start

# * Two Pointers Solution | O(n^2) Time | O(1) Space
# * n -> The length of s string


class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0

        def countSubstringsHelper(left, right):
            nonlocal palindrome_count

            # * Expand around its center, i.e., Start from the middle of the string and move the
            # * left pointer to left and right pointer to right to check if it's a palindrome.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            # * Handle odd length palindromic string.
            countSubstringsHelper(i, i)

            # * Handle even length palindromic string.
            countSubstringsHelper(i, i + 1)

        return palindrome_count


# @lc code=end
