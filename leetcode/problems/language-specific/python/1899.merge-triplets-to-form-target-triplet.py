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
            # * Filter out the triplet that is greater than the target
            # * values as it never becomes a target when merged.
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue

            # * We iterate through the triplet and check if the value equals the target
            # * value specific to a position. If so add its index to the hashset.
            for idx, v in enumerate(triplet):
                if v == target[idx]:
                    target_idx_set.add(idx)

        return len(target_idx_set) == len(target)


# @lc code=end
