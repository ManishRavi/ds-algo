#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#

# @lc code=start

# * Sorting Solution | O(nlogn) Time | O(1) Space
# * n -> The length of properties array


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # * Sort in descending order based on the attack and
        # * in ascending order based on the defense.
        properties.sort(key=lambda property: (-property[0], property[1]))
        max_defense = total_weak_characters = 0
        for _, defense in properties:
            if defense < max_defense:
                total_weak_characters += 1
            max_defense = max(max_defense, defense)

        return total_weak_characters


# @lc code=end
