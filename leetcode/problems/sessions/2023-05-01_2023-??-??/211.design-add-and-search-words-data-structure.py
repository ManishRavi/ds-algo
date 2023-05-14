#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

# * Trie and Backtracking Solution | O(n) addWord, O(26^n) search Time | O(n) Space
# * n -> The number of characters in a given word


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(list)
        self.is_word_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.max_word_len = 0

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word_end = True
        self.max_word_len = max(self.max_word_len, len(word))

    def search(self, word: str) -> bool:
        if len(word) > self.max_word_len:
            return False

        def dfs(root, start_idx):
            for i in range(start_idx, len(word)):
                char = word[i]
                if char == ".":
                    for children in root.children.values():
                        if dfs(children, i + 1):
                            return True

                    return False
                else:
                    if char not in root.children:
                        return False

                    root = root.children[char]
            return root.is_word_end

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
