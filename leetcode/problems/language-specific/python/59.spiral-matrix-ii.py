#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start

# * Iterative Solution | O(mn) Time | O(1) Space
# * m -> The number of rows in the matrix | n -> The number of columns in the matrix


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n
        top, bottom = 0, n
        count = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        while left < right and top < bottom:
            for col in range(left, right):
                matrix[top][col] = count
                count += 1
            top += 1

            for row in range(top, bottom):
                matrix[row][right - 1] = count
                count += 1
            right -= 1

            if not left < right or not top < bottom:
                break

            for col in range(right - 1, left - 1, -1):
                matrix[bottom - 1][col] = count
                count += 1
            bottom -= 1

            for row in range(bottom - 1, top - 1, -1):
                matrix[row][left] = count
                count += 1
            left += 1

        return matrix


# @lc code=end
