#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start

# * Hash Table and Counting Solution | O(logn) Time | O(logn) Space
# * n -> The given input


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # * We can check whether two numbers have the same digits by comparing the frequencies of their digits.
        # * For example, 338 and 833 have the same digits because they both have exactly two 3's and one 8.
        # * Since N could only be a power of 2 with 9 digits or less namely (2^0, 2^1, ..., 2^29 ),
        # * we can just check whether N has the same digits as any of these possibilities.
        n_counter = collections.Counter(str(n))
        return any(n_counter == collections.Counter(str(1 << i)) for i in range(30))


# @lc code=end
