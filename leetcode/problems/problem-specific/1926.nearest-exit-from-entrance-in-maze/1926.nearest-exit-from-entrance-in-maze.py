#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start

# * Iterative BFS Solution | O(mn) Time | O(max(m,n)) Space
# * m -> The number of rows in the maze matrix | n -> The number of columns in the maze matrix


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(maze), len(maze[0])
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        # * Start BFS traversal.
        # * Stores a pair of step, row and col.
        # * Pair -> (step, row, col)
        queue = collections.deque([(0, start_row, start_col)])
        while queue:
            cur_step, cur_row, cur_col = queue.popleft()
            if cur_step != 0 and (cur_row in (0, ROWS - 1) or cur_col in (0, COLS - 1)):
                return cur_step

            for d_row, d_col in DIRECTIONS:
                row, col = cur_row + d_row, cur_col + d_col
                if (
                    not 0 <= row <= ROWS - 1
                    or not 0 <= col <= COLS - 1
                    or maze[row][col] != "."
                ):
                    continue

                maze[row][col] = "+"
                queue.append((1 + cur_step, row, col))

        return -1


# @lc code=end
