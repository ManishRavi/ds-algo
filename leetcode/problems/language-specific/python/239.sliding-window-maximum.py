#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

# * Two Pointers and Sliding Window Solution | O(n) Time | O(k) Space
# * n -> The length of nums array | k -> The size of the window

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # * Stores the indexes of the elements in monotonically decreasing order
        nums_deque = collections.deque()
        result = []
        left = 0
        for right, right_val in enumerate(nums):
            # * Remove the elements from the left that are out of window bounds (k)
            if nums_deque and left > nums_deque[0]:
                nums_deque.popleft()

            # * Remove the elements from the right that are
            # * smaller than the current element as they're useless
            while nums_deque and nums[nums_deque[-1]] < right_val:
                nums_deque.pop()

            nums_deque.append(right)

            # * Add the elements iff we've the required window size
            # * as we're starting the pointers from the beginning (0)
            if right+1 >= k:
                result.append(nums[nums_deque[0]])
                left += 1

        return result

# @lc code=end
