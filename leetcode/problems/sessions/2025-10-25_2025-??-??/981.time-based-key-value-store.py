#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start


# * Binary Search Based On Search Insert Position Solution | O(1) Set, O(logn) Get Time | O(n) Space
# * n -> The number of values per key


class TimeMap:
    def __init__(self):
        self.key_value_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_value_map[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        left -= 1
        return values[left][0] if left >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
