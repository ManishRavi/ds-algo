#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start

# * Backtracking Solution | O(n*(2^n)) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(start_idx, partition):
            if start_idx == len(s):
                res.append(partition[:])
                return

            for i in range(start_idx, len(s)):
                if self.is_palindrome(s[start_idx : i + 1]):
                    partition.append(s[start_idx : i + 1])
                    helper(i + 1, partition)
                    partition.pop()

        helper(0, [])
        return res

    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


# @lc code=end
