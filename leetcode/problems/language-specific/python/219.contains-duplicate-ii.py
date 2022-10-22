#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start

# * Hash Table Solution | O(n) Time | O(n) Space
# * n -> The length of nums array


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_val_idx_map = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            if num in nums_val_idx_map and abs(nums_val_idx_map[num] - idx) <= k:
                return True

            nums_val_idx_map[num] = idx

        return False


# @lc code=end
