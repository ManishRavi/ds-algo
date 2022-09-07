#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

# * Backtracking Solution | O(4^n) Time | O(n) Space
# * n -> The length of digits

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LETTERS = [
            '0', '1', "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]
        res = []
        if not digits:
            return res

        def letterCombinationsHelper(idx=0, combination=[]):
            if len(combination) == len(digits):
                res.append(''.join(combination))
                return

            for c in LETTERS[ord(digits[idx]) - ord('0')]:
                combination.append(c)
                letterCombinationsHelper(idx + 1, combination)
                combination.pop()

        letterCombinationsHelper()
        return res

# @lc code=end
