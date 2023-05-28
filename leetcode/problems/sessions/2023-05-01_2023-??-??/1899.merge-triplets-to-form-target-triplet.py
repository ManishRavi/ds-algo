#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start

# * Greedy Solution | O(n) Time | O(1) Space
# * n -> The length of triplets array


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_idx_set = set()
        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue

            for idx, val in enumerate(triplet):
                if val == target[idx]:
                    target_idx_set.add(idx)

        return len(target_idx_set) == len(target)


# @lc code=end
