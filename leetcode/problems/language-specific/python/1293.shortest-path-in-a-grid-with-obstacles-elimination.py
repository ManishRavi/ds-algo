#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start

# * Dijkstra's Algorithm Solution | O(mn*logn) Time | O(mn) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        # * Start Dijkstra's Algorithm.
        visited_set = set((0, 0, 0))
        # * Stores a pair of step, row, col and k.
        # * Pair -> (step, row, col, k)
        min_heap = [(0, 0, 0, 0)]
        while min_heap:
            cur_step, cur_row, cur_col, cur_k = heapq.heappop(min_heap)
            if cur_row == ROWS - 1 and cur_col == COLS - 1:
                return cur_step

            for d_row, d_col in DIRECTIONS:
                row, col = cur_row + d_row, cur_col + d_col
                if (
                    not 0 <= row <= ROWS - 1
                    or not 0 <= col <= COLS - 1
                    or (cur_k, row, col) in visited_set
                    or cur_k > k
                ):
                    continue

                visited_set.add((cur_k, row, col))
                heapq.heappush(
                    min_heap, (cur_step + 1, row, col, cur_k + grid[row][col])
                )

        return -1


# @lc code=end
