#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

# * Stack Solution | O(n) Time | O(n) Space
# * n -> The length of tokens array

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # * Stores the operands.
        tokens_stack = []
        for s in tokens:
            # * Push the operands into the stack.
            if s != '+' and s != '-' and s != '*' and s != '/':
                tokens_stack.append(int(s))

            # * Evaluate the operation by popping the 2 most recent operands from the stack.
            else:
                val2, val1 = tokens_stack.pop(), tokens_stack.pop()
                operation_result = 0
                if s == '+':
                    operation_result = val1 + val2
                elif s == '-':
                    operation_result = val1 - val2
                elif s == '*':
                    operation_result = val1 * val2
                elif s == '/':
                    operation_result = int(val1 / val2)

                tokens_stack.append(operation_result)

        return tokens_stack[0]

# @lc code=end
