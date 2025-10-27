#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start


# * Hash Table and Intelligent Sequence Building Solution | O(n) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                cur_sequence = 1
                while (num + cur_sequence) in nums_set:
                    cur_sequence += 1
                longest_sequence = max(longest_sequence, cur_sequence)

        return longest_sequence


# @lc code=end
