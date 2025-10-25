#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start

# * Sorting and Priority Queue (Min Heap) Solution | O(nlogn) Time | O(n) Space
# * n -> The length of nums1 or nums2 array


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums_pair = [num_pair for num_pair in zip(nums1, nums2)]
        nums_pair.sort(key=lambda num_pair: -num_pair[1])
        min_heap = []
        nums1_sum = res = 0
        for num1, num2 in nums_pair:
            nums1_sum += num1
            heappush(min_heap, num1)

            if len(min_heap) > k:
                nums1_sum -= heappop(min_heap)
            if len(min_heap) == k:
                res = max(res, nums1_sum * num2)

        return res


# @lc code=end
