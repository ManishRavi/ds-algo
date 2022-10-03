#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start

# * Recursive Top-Down Solution | O(nkt) Time | O(nt) Space
# * n -> The given input | k -> The given input | t -> The given input target


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # * Stores a key-value pair where the key is a pair of current
        # * die & current sum and value is the total ways.
        # * Key -> (cur_die, cur_sum) | Value -> total_ways
        memcache = {}

        def numRollsToTargetHelper(cur_die, cur_sum):
            if cur_die == n:
                return 1 if cur_sum == target else 0
            if (cur_die, cur_sum) in memcache:
                return memcache[(cur_die, cur_sum)]

            res = 0
            for i in range(1, k + 1):
                res += numRollsToTargetHelper(cur_die + 1, cur_sum + i)

            memcache[(cur_die, cur_sum)] = res
            return memcache[(cur_die, cur_sum)]

        return numRollsToTargetHelper(0, 0) % (10**9 + 7)


# @lc code=end
