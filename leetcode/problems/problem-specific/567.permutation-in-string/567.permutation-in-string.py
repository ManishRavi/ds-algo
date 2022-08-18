#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start

# * Two Pointers and Sliding Window Solution | O(n) Time | O(n) Space
# * n -> The length of s2 string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        if s1_length > s2_length:
            return False

        s1_counter = collections.Counter(s1)
        left, right = 0, s1_length
        while right <= s2_length:
            # * Check if the current window in s2 has
            # * all the chars of s1 by comparing the frequencies
            if s1_counter == collections.Counter(s2[left:right]):
                return True

            left += 1
            right += 1

        return False

# @lc code=end
