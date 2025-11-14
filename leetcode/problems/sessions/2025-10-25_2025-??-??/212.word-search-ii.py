#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start

# * Prefix Tree and Backtracking Solution | O(mn*(4^mn)) Time | O(mn) Space
# * m -> The number of rows in the board matrix | n -> The number of columns in the board matrix


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word_end = True


class Solution:
    def __init__(self):
        self.trie = Trie()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])
        self._insert_words_into_trie(words)
        res = []

        def helper(row, col, root, word_list):
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or board[row][col] == "*"
                or board[row][col] not in root.children
            ):
                return

            cur_val = board[row][col]
            board[row][col] = "*"
            word_list.append(cur_val)
            root = root.children[cur_val]
            if root.is_word_end:
                res.append("".join(word_list))
                root.is_word_end = False

            for d_row, d_col in DIRECTIONS:
                helper(row + d_row, col + d_col, root, word_list)

            word_list.pop()
            board[row][col] = cur_val

        for row in range(ROWS):
            for col in range(COLS):
                helper(row, col, self.trie.root, [])

        return res

    def _insert_words_into_trie(self, words):
        for word in words:
            self.trie.insert(word)


# @lc code=end
