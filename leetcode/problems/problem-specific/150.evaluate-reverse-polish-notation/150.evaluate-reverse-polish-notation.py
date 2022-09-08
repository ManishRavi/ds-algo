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
        # * Stores the operands.
        tokens_stack = []
        for token in tokens:
            # * Push the operands into the stack.
            if token != "+" and token != "-" and token != "*" and token != "/":
                tokens_stack.append(int(token))
            # * Evaluate the operation by popping the 2 most recent operands from the stack.
            else:
                val2, val1 = tokens_stack.pop(), tokens_stack.pop()
                operation_res = 0
                if token == "+":
                    operation_res = val1 + val2
                elif token == "-":
                    operation_res = val1 - val2
                elif token == "*":
                    operation_res = val1 * val2
                elif token == "/":
                    operation_res = int(val1 / val2)

                tokens_stack.append(operation_res)

        return tokens_stack[0]


# @lc code=end
