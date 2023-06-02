#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start

# * Iterative BFS Solution | O(mn) Time | O(mn) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1

        queue = deque([(1, 0, 0)])
        grid[0][0] = 1
        while queue:
            for _ in range(len(queue)):
                cur_len, cur_row, cur_col = queue.popleft()
                if cur_row == ROWS - 1 and cur_col == COLS - 1:
                    return cur_len

                for d_row, d_col in DIRECTIONS:
                    row, col = cur_row + d_row, cur_col + d_col
                    if (
                        not 0 <= row <= ROWS - 1
                        or not 0 <= col <= COLS - 1
                        or grid[row][col] == 1
                    ):
                        continue

                    queue.append((cur_len + 1, row, col))
                    grid[row][col] = 1

        return -1


# @lc code=end
