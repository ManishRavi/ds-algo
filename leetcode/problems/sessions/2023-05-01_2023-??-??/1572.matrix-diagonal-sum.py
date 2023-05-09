#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The number of rows or columns in the mat matrix


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + mat[i][n - i - 1]

        if (n % 2) == 1:
            res -= mat[n // 2][n // 2]

        return res


# @lc code=end
