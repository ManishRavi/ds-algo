#
# @lc app=leetcode id=1603 lang=python3
#
# [1603] Design Parking System
#

# @lc code=start

# * Hash Table Solution | O(1) Time | O(1) Space


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_slots_counter = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.parking_slots_counter[carType] <= 0:
            return False

        self.parking_slots_counter[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end
