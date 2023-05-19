#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start

# * Iterative Multi-Source BFS Solution | O(mn) Time | O(mn) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        min_time = total_fresh_oranges = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    total_fresh_oranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        while queue and total_fresh_oranges > 0:
            for _ in range(len(queue)):
                cur_row, cur_col = queue.popleft()
                for d_row, d_col in DIRECTIONS:
                    row, col = cur_row + d_row, cur_col + d_col
                    if (
                        not 0 <= row <= ROWS - 1
                        or not 0 <= col <= COLS - 1
                        or grid[row][col] != 1
                    ):
                        continue

                    grid[row][col] = 2
                    queue.append((row, col))
                    total_fresh_oranges -= 1

            min_time += 1

        return min_time if total_fresh_oranges == 0 else -1


# @lc code=end
