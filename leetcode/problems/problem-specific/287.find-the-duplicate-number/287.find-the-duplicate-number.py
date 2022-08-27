#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start

# * Floyd's Tortoise and Hare Cycle Detection Solution | O(n) Time | O(1) Space
# * n -> The length of nums array

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # * Find the intersection point of the two runners.
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # * Find the entrance to the cycle.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# @lc code=end
