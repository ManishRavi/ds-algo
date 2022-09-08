#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

# * Backtracking Solution | O(4^n) Time | O(n) Space
# * n -> The length of digits string


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LETTERS = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        if not digits:
            return res

        def letterCombinationsHelper(digits_idx, combination):
            if len(combination) == len(digits):
                res.append("".join(combination))
                return

            for char in LETTERS[ord(digits[digits_idx]) - ord("0")]:
                combination.append(char)
                letterCombinationsHelper(digits_idx + 1, combination)
                combination.pop()

        letterCombinationsHelper(0, [])
        return res


# @lc code=end
