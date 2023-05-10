#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start

# * Iterative Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for col in range(left, right):
                res.append(matrix[top][col])
            top += 1

            for row in range(top, bottom):
                res.append(matrix[row][right - 1])
            right -= 1

            if not left < right or not top < bottom:
                break

            for col in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][col])
            bottom -= 1

            for row in range(bottom - 1, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res


# @lc code=end
