#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start

# * Iterative Solution | O(n) Time | O(1) Space
# * n -> The length of gain array


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        cur_sum = 0
        for num in gain:
            cur_sum += num
            highest_altitude = max(highest_altitude, cur_sum)

        return highest_altitude


# @lc code=end
