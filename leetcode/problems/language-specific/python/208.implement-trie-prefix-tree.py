#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

# * Hash Table and Prefix Tree Solution | O(n) Time | O(n) Space
# * n -> The number of characters in a given word


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

    def search(self, word: str) -> bool:
        return self._find_helper(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self._find_helper(prefix, False)

    def _find_helper(self, word: str, is_full_word_search: bool) -> bool:
        """Returns if the word is in the trie or if there is any word in the trie
        that starts with the given prefix based on the is_full_word_search flag.
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False

            cur = cur.children[char]
        return cur.is_word_end if is_full_word_search else True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
