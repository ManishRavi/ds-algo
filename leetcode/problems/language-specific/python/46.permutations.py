#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start

# * Backtracking Solution | O(n*(n!)) Time | O(n) Space
# * n -> The length of nums array

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permuteHelper(used=set(), permutation=[]):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return

            for num in nums:
                if num in used:
                    continue

                used.add(num)
                permutation.append(num)
                permuteHelper(used, permutation)
                permutation.pop()
                used.remove(num)

        permuteHelper()
        return result

# @lc code=end
