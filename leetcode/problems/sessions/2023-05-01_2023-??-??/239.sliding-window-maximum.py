#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

# * Two Pointers and Sliding Window Solution | O(n) Time | O(k) Space
# * n -> The length of nums array | k -> The given input that represents size of the window


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_deque = deque()
        res = []
        left = 0
        for right, right_val in enumerate(nums):
            if nums_deque and left > nums_deque[0]:
                nums_deque.popleft()

            while nums_deque and nums[nums_deque[-1]] < right_val:
                nums_deque.pop()
            nums_deque.append((right))

            if right + 1 >= k:
                res.append(nums[nums_deque[0]])
                left += 1

        return res


# @lc code=end
