#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

# * Trie and Backtracking Solution | O(n) Time | O(n) Space
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
        # * Store the maximum length of all the words inserted to avoid TLE.
        self.max_words_length = 0

    def addWord(self, word: str) -> None:
        cur = self.root
        count = 0
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]
            count += 1

        self.max_words_length = max(self.max_words_length, count)
        cur.is_word_end = True

    def search(self, word: str) -> bool:
        if len(word) > self.max_words_length:
            return False

        def searchHelper(start_index, root):
            for i in range(start_index, len(word)):
                c = word[i]
                if c == '.':
                    for children in root.children.values():
                        if searchHelper(i + 1, children):
                            return True

                    return False

                else:
                    if c not in root.children:
                        return False

                    root = root.children[c]

            return root.is_word_end

        return searchHelper(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
