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
        # * If we can't partition the array into the given groupSize.
        if len(hand) % groupSize:
            return False

        hand_counter = collections.Counter(hand)
        min_heap = list(hand_counter.keys())
        heapq.heapify(min_heap)
        while min_heap:
            start_of_sequence = min_heap[0]
            for val in range(start_of_sequence, start_of_sequence + groupSize):
                if val not in hand_counter:
                    return False

                hand_counter[val] -= 1
                # * Remove the current val from the min_heap if the count becomes 0.
                if not hand_counter[val]:
                    # * Return false if the current val isn't the min element in the heap.
                    if val != min_heap[0]:
                        return False

                    heapq.heappop(min_heap)

        return True


# @lc code=end
