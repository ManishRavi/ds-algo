#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

# * Trie and Backtracking Solution | O(n) addWord, O(26^n) search Time | O(n) Space
# * n -> The number of characters in a given word


class TrieNode:
    def __init__(self):
        # * Stores a key-value pair where the key is a character and value is an array of TrieNodes.
        self.children = collections.defaultdict(list)
        # * Used to mark the end of a word.
        self.is_word_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        # * Stores the maximum length of all the words inserted to avoid TLE.
        self.max_words_length = 0

    def addWord(self, word: str) -> None:
        cur = self.root
        count = 0
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            count += 1
        self.max_words_length = max(self.max_words_length, count)
        cur.is_word_end = True

    def search(self, word: str) -> bool:
        if len(word) > self.max_words_length:
            return False

        def searchHelper(root, start_idx):
            for i in range(start_idx, len(word)):
                char = word[i]
                if char == ".":
                    for children in root.children.values():
                        if searchHelper(children, i + 1):
                            return True

                    return False
                else:
                    if char not in root.children:
                        return False

                    root = root.children[char]
            return root.is_word_end

        return searchHelper(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
