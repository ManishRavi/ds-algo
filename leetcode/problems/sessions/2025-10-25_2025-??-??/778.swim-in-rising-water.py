#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start

# * Dijkstra's Algorithm Solution | O((mn)logmn) Time | O(mn) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]
        visited_set = set((0, 0))
        while min_heap:
            cur_time, cur_row, cur_col = heappop(min_heap)
            if cur_row == ROWS - 1 and cur_col == COLS - 1:
                return cur_time

            for d_row, d_col in DIRECTIONS:
                row, col = cur_row + d_row, cur_col + d_col
                if (
                    not 0 <= row <= ROWS - 1
                    or not 0 <= col <= COLS - 1
                    or (row, col) in visited_set
                ):
                    continue

                heappush(min_heap, (max(cur_time, grid[row][col]), row, col))
                visited_set.add((row, col))


# @lc code=end
