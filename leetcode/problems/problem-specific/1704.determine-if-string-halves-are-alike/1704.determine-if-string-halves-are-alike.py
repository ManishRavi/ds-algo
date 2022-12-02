#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start

# * Counting Solution | O(n) Time | O(1) Space
# * n -> The length of s string


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_count = 0
        for char in s[: len(s) // 2]:
            if char.lower() in ("a", "e", "i", "o", "u"):
                vowel_count += 1

        for char in s[len(s) // 2 :]:
            if char.lower() in ("a", "e", "i", "o", "u"):
                vowel_count -= 1

        return vowel_count == 0


# @lc code=end
