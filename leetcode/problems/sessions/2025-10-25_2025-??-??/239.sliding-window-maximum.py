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
        queue = deque([])
        res = []
        left = 0
        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)
            if (right - left + 1) == k:
                res.append(nums[queue[0]])
                left += 1
                if queue[0] < left:
                    queue.popleft()

        return res


# @lc code=end
