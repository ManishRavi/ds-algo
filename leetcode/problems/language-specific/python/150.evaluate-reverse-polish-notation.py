#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

# * Stack Solution | O(n) Time | O(n) Space
# * n -> The number of operands in tokens array

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # * Stores the operands
        tokens_stack = []
        for s in tokens:
            if s != '+' and s != '-' and s != '*' and s != '/':
                tokens_stack.append(int(s))
            else:
                val1, val2 = tokens_stack.pop(), tokens_stack.pop()
                operation_result = 0
                if s == '+':
                    operation_result = val1 + val2
                elif s == '-':
                    operation_result = val2 - val1
                elif s == '*':
                    operation_result = val1 * val2
                elif s == '/':
                    operation_result = int(val2/val1)

                tokens_stack.append(operation_result)

        return tokens_stack[0]

# @lc code=end
