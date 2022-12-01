#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of arr array


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_counter = collections.Counter(arr)
        return len(set(arr_counter.values())) == len(arr_counter.keys())


# @lc code=end
