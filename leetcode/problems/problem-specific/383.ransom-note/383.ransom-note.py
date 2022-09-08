#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(1) Space
# * n -> The length of ransomNote string


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        # * Contains only 26 lowercase letters which makes it a constant space.
        magazine_counter = collections.Counter(magazine)
        for char in ransomNote:
            magazine_counter[char] -= 1
            if magazine_counter[char] < 0:
                return False

        return True


# @lc code=end
