#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start

# * Two Pointers Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        while left < right:
            if not self.is_vowel(s_list[left]):
                left += 1
            elif not self.is_vowel(s_list[right]):
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        return "".join(s_list)

    def is_vowel(self, char):
        return char.lower() in ("a", "e", "i", "o", "u")


# @lc code=end
