#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start

# * Hash Table Solution | O(mn) Time | O(mn) Space
# * m -> The length of words array | n -> The length of each string


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE_CODES_LOWER = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        words_morse_code_set = set()
        for word in words:
            transformed_word = "".join(
                [MORSE_CODES_LOWER[ord(char) - ord("a")] for char in word]
            )
            words_morse_code_set.add(transformed_word)

        return len(words_morse_code_set)


# @lc code=end
