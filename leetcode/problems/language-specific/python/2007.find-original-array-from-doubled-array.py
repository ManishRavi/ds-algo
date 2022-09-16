#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

# @lc code=start

# * Sorting and Hash Table Solution | O(nlogn) Time | O(n) Space
# * n -> The length of changed array


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed_len = len(changed)
        original = []
        # * If the length of changed array is odd then we can't find the original array.
        if changed_len % 2:
            return original

        changed.sort()
        changed_counter = collections.Counter(changed)
        for num in changed:
            # * 0 is a special case where the twice of it is 0 itself.
            if num == 0:
                if changed_counter[num] > 1:
                    original.append(num)
                    changed_counter[num] -= 2
            elif changed_counter[num] > 0 and changed_counter[num * 2] > 0:
                original.append(num)
                changed_counter[num] -= 1
                changed_counter[num * 2] -= 1

            if len(original) == changed_len // 2:
                return original

        return []


# @lc code=end
