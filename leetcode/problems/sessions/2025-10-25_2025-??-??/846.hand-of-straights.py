#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start

# * Hash Table and Priority Queue (Min Heap) Solution | O(nlogn) Time | O(n) Space
# * n -> The length of hand array


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand_counter = Counter(hand)
        min_heap = list(hand_counter.keys())
        heapify(min_heap)
        while min_heap:
            group_start = min_heap[0]
            for val in range(group_start, group_start + groupSize):
                if val not in hand_counter:
                    return False

                hand_counter[val] -= 1
                if hand_counter[val] == 0:
                    if val != min_heap[0]:
                        return False

                    heappop(min_heap)

        return True


# @lc code=end
