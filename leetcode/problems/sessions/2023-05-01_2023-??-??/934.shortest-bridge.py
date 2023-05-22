#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start

# * Recursive DFS and Iterative BFS Solution | O(mn) Time | O(mn) Space
# * m -> The number of rows in the grid matrix | n -> The number of columns in the grid matrix


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited_set = set()

        def is_invalid(row, col):
            return not 0 <= row <= ROWS - 1 or not 0 <= col <= COLS - 1

        def dfs(row, col):
            if is_invalid(row, col) or grid[row][col] != 1 or (row, col) in visited_set:
                return

            visited_set.add((row, col))
            for d_row, d_col in DIRECTIONS:
                dfs(row + d_row, col + d_col)

        def bfs():
            res = 0
            queue = deque(visited_set)
            while queue:
                for _ in range(len(queue)):
                    cur_row, cur_col = queue.popleft()
                    for d_row, d_col in DIRECTIONS:
                        row, col = cur_row + d_row, cur_col + d_col
                        if is_invalid(row, col) or (row, col) in visited_set:
                            continue
                        if grid[row][col] == 1:
                            return res

                        queue.append((row, col))
                        visited_set.add((row, col))
                res += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col)
                    return bfs()


# @lc code=end
