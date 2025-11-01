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
        cars = [car for car in zip(position, speed)]
        cars.sort(key=lambda car: -car[0])
        stack = []
        for car_position, car_speed in cars:
            travel_time = (target - car_position) / car_speed
            if not stack or travel_time > stack[-1]:
                stack.append(travel_time)

        return len(stack)


# @lc code=end
