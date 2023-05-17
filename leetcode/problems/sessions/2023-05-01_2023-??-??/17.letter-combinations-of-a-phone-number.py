#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

# * Backtracking Solution | O(n*(4^n)) Time | O(n) Space
# * n -> The length of digits string


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LETTERS = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        if not digits:
            return res

        def helper(start_idx, combination):
            if start_idx == len(digits):
                res.append("".join(combination))
                return

            for letter in LETTERS[int(digits[start_idx])]:
                helper(start_idx + 1, combination + [letter])

        helper(0, [])
        return res


# @lc code=end
