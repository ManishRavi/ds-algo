#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start

# * Binary Search Solution | O(logn) Time | O(1) Space
# * n -> The given input


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            guess_res = guess(mid)
            if guess_res == 0:
                return mid
            elif guess_res == 1:
                left = mid + 1
            else:
                right = mid - 1


# @lc code=end
