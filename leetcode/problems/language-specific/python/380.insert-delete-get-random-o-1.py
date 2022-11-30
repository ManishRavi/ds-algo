#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start

# * Hash Table Solution | O(1) Time | O(n) Space
# * n -> The number of insert operations


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.val_idx_map = collections.defaultdict(int)

    def insert(self, val: int) -> bool:
        if val not in self.val_idx_map:
            self.nums.append(val)
            self.val_idx_map[val] = len(self.nums) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.val_idx_map:
            # * Get the corresponding index of the given value and the last index value.
            val_idx = self.val_idx_map[val]
            last_idx_val = self.nums[-1]
            # * Swap the given value with the last index value.
            self.nums[val_idx], self.nums[-1] = last_idx_val, val
            self.val_idx_map[last_idx_val] = val_idx
            # * Delete the last index value.
            self.nums.pop()
            del self.val_idx_map[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
