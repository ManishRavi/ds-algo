#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start

# * Math Solution | O(n) Time | O(1) Space
# * n -> The length of salary array


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = float("inf"), float("-inf")
        total_salary = 0
        for cur_salary in salary:
            total_salary += cur_salary
            min_salary = min(min_salary, cur_salary)
            max_salary = max(max_salary, cur_salary)

        return (total_salary - min_salary - max_salary) / (len(salary) - 2)


# @lc code=end
