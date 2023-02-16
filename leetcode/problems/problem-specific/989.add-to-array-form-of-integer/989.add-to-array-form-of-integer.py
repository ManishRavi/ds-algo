#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start

# * Math Solution | O(max(n, logk)) Time | O(max(n, logk)) Space
# * n -> The length of num array


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            if not k:
                break
            k, num[i] = divmod(num[i] + k, 10)

        while k > 0:
            k, extra_digit = divmod(k, 10)
            num = [extra_digit] + num

        return num


# @lc code=end
