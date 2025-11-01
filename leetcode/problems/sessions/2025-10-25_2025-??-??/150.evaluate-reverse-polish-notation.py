#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

# * Iterative Stack Solution | O(n) Time | O(n) Space
# * n -> The length of tokens array


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens_stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                res = 0
                val2, val1 = tokens_stack.pop(), tokens_stack.pop()
                if token == "+":
                    res = val1 + val2
                elif token == "-":
                    res = val1 - val2
                elif token == "*":
                    res = val1 * val2
                elif token == "/":
                    res = int(val1 / val2)

                tokens_stack.append(res)
            else:
                tokens_stack.append(int(token))

        return tokens_stack[0]


# @lc code=end
