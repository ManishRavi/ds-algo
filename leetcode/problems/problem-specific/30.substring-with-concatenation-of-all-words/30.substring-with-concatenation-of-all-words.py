#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start

# * Sliding Window Solution | O(nml) Time | O(m) Space
# * n -> The length of s string | m -> The length of words array |
# * l -> The length of each string


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len, words_len = len(s), len(words)
        each_word_len = len(words[0])
        words_counter = collections.Counter(words)
        start_idxs = []
        for i in range(s_len - (words_len * each_word_len) + 1):
            words_seen = collections.defaultdict(int)
            for j in range(words_len):
                cur_word_index = i + (j * each_word_len)
                cur_word = s[cur_word_index : cur_word_index + each_word_len]
                if cur_word not in words_counter:
                    break

                words_seen[cur_word] += 1
                if words_seen[cur_word] > words_counter[cur_word]:
                    break

                if j + 1 == words_len:
                    start_idxs.append(i)

        return start_idxs


# @lc code=end
