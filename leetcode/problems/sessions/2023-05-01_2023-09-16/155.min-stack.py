#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start

# * Two Stacks Solution | O(1) Time | O(n) Space
# * n -> The number of push operations


class MinStack:
    def __init__(self):
        self.real_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.real_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.real_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.real_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
