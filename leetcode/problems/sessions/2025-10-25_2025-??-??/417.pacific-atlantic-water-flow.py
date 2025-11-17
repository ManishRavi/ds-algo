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
        res = []

        def helper(row, col, visited_set, prev_height):
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or (row, col) in visited_set
                or heights[row][col] < prev_height
            ):
                return

            visited_set.add((row, col))
            for d_row, d_col in DIRECTIONS:
                helper(row + d_row, col + d_col, visited_set, heights[row][col])

        for col in range(COLS):
            helper(0, col, pacific_visited_set, heights[0][col])
            helper(ROWS - 1, col, atlantic_visited_set, heights[ROWS - 1][col])

        for row in range(ROWS):
            helper(row, 0, pacific_visited_set, heights[row][0])
            helper(row, COLS - 1, atlantic_visited_set, heights[row][COLS - 1])

        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) in pacific_visited_set) and (
                    (row, col) in atlantic_visited_set
                ):
                    res.append([row, col])

        return res


# @lc code=end
