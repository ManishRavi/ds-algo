#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

# * Prefix Tree and Backtracking Solution | O(n) addWord, O(26^n) search Time | O(n) Space
# * n -> The number of characters in a given word


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.max_words_length = 0

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word_end = True
        self.max_words_length = max(self.max_words_length, len(word))

    def search(self, word: str) -> bool:
        if len(word) > self.max_words_length:
            return False

        def helper(start_idx, root):
            for i in range(start_idx, len(word)):
                char = word[i]
                if char == ".":
                    for children in root.children.values():
                        if helper(i + 1, children):
                            return True

                    return False
                else:
                    if char not in root.children:
                        return False

                    root = root.children[char]
            return root.is_word_end

        return helper(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
