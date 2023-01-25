#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start

# * Iterative BFS Solution | O(mn) Time | O(mn) Space
# * m -> The number of rows in the board matrix | n -> The number of columns in the board matrix


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_len = len(board)
        board.reverse()

        def get_val_to_pos(val):
            row = (val - 1) // board_len
            col = (val - 1) % board_len
            if row % 2:
                col = board_len - 1 - col
            return row, col

        # * Start BFS traversal.
        visited_set = set([1])
        # * Stores a pair of val and moves.
        # * Pair -> (val, moves)
        queue = deque([(1, 0)])
        while queue:
            cur_val, cur_moves = queue.popleft()
            for i in range(1, 7):
                next_val = cur_val + i
                row, col = get_val_to_pos(next_val)
                if board[row][col] != -1:
                    next_val = board[row][col]
                if next_val == board_len * board_len:
                    return cur_moves + 1

                if next_val not in visited_set:
                    queue.append((next_val, cur_moves + 1))
                    visited_set.add(next_val)

        return -1


# @lc code=end
