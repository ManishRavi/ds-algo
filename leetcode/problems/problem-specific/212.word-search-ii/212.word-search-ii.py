#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start

# * Trie and Backtracking Solution | O(mn*(4^mn)) Time | O(mn) Space
# * m -> The number of rows in the board matrix | n -> The number of columns in the board matrix


class TrieNode:
    def __init__(self):
        # * Stores a key-value pair where the key is a character and value is an array of TrieNodes.
        self.children = collections.defaultdict(list)
        # * Used to mark the end of a word.
        self.is_word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word_end = True

    def get_root(self):
        return self.root


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])
        trie = self._insert_words_into_trie(words)
        res = []

        def findWordsHelper(row, col, root, word_list):
            if (
                not 0 <= row <= ROWS - 1
                or not 0 <= col <= COLS - 1
                or board[row][col] == "*"
                or board[row][col] not in root.children
            ):
                return

            cur_val = board[row][col]
            board[row][col] = "*"
            root = root.children[cur_val]
            word_list.append(cur_val)
            if root.is_word_end:
                res.append("".join(word_list))
                root.is_word_end = False

            for d_row, d_col in DIRECTIONS:
                findWordsHelper(row + d_row, col + d_col, root, word_list)

            word_list.pop()
            board[row][col] = cur_val

        for row in range(ROWS):
            for col in range(COLS):
                findWordsHelper(row, col, trie.get_root(), [])

        return res

    def _insert_words_into_trie(self, words: List[str]) -> Trie:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie


# @lc code=end
