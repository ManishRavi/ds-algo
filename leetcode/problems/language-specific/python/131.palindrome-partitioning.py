#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start

# * Backtracking Solution | O(n*(2^n)) Time | O(n) Space
# * n -> The length of s

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def partitionHelper(idx=0, partition=[]):
            if idx >= len(s):
                res.append(partition[:])
                return

            for j in range(idx, len(s)):
                if self.is_palindrome(s, idx, j):
                    partition.append(s[idx: j + 1])
                    partitionHelper(j + 1, partition)
                    partition.pop()

        partitionHelper()
        return res

    def is_palindrome(self, word, left, right):
        while left < right:
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1

        return True

# @lc code=end
