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
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False

        s1_counter = Counter(s1)
        left, right = 0, len(s1)
        while right <= len(s2):
            if Counter(s2[left:right]) == s1_counter:
                return True

            left += 1
            right += 1

        return False


# @lc code=end
