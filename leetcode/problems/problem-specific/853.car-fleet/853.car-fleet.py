#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start

# * Sorting and Stack Solution | O(nlogn) Time | O(n) Space
# * n -> The length of position or speed array

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # * Stores a pair of the position and the speed of a car.
        # * Pair -> (position, speed).
        cars = [car for car in zip(position, speed)]
        # * Sort in descending order based on the position.
        cars.sort(key=lambda x: -x[0])
        stack = []
        for position, speed in cars:
            travel_time = (target - position) / speed
            if not stack or travel_time > stack[-1]:
                stack.append(travel_time)

        return len(stack)

# @lc code=end
