#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start

# * Recursive DFS Solution | O(mn) Time | O(mn) Space
# * m -> The number of rows in the heights matrix | n -> The number of columns in the heights matrix


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited_set, atlantic_visited_set = set(), set()

        def pacificAtlanticHelper(row, col, visited_set, prev_height):
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or (row, col) in visited_set
                or heights[row][col] < prev_height
            ):
                return

            visited_set.add((row, col))
            for d_row, d_col in DIRECTIONS:
                pacificAtlanticHelper(
                    row + d_row, col + d_col, visited_set, heights[row][col]
                )

        # * Perform a DFS traversal on the first row (pacific ocean cells) and last row (atlantic ocean cells).
        for col in range(COLS):
            pacificAtlanticHelper(0, col, pacific_visited_set, heights[0][col])
            pacificAtlanticHelper(
                ROWS - 1, col, atlantic_visited_set, heights[ROWS - 1][col]
            )

        # * Perform a DFS traversal on the first column (pacific ocean cells) and last column (atlantic ocean cells).
        for row in range(ROWS):
            pacificAtlanticHelper(row, 0, pacific_visited_set, heights[row][0])
            pacificAtlanticHelper(
                row, COLS - 1, atlantic_visited_set, heights[row][COLS - 1]
            )

        res = []
        # * For each cell check whether it has been visited by both the pacific and atlantic oceans.
        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) in pacific_visited_set) and (
                    (row, col) in atlantic_visited_set
                ):
                    res.append([row, col])

        return res


# @lc code=end
