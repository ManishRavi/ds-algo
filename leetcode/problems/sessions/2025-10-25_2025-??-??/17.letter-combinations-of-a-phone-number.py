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
        digit_to_letters_map = [
            "0",
            "1",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]
        res = []

        def helper(start_idx, combination):
            if len(combination) == len(digits):
                res.append("".join(combination))
                return

            for letter in digit_to_letters_map[int(digits[start_idx])]:
                combination.append(letter)
                helper(start_idx + 1, combination)
                combination.pop()

        helper(0, [])
        return res


# @lc code=end
