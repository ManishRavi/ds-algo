#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        heap = []
        for k in nums:
            # Remove sequences that cannot be extended
            while heap and (k > (heap[0][0]+1)):
                curr = heapq.heappop(heap)
                if curr[1] < 3:
                    # if any sequence len<3 , return False
                    return False

           # Get the sequence of smallest length ending at smallest point.
           # Extend if you can, if you can't then this will be starting point of new sequence
            if heap and heap[0][0]+1 == k:
                curr = heapq.heappop(heap)
                heapq.heappush(heap, (k, curr[1]+1))
            else:
                # push new sequence starting
                heapq.heappush(heap, (k, 1))

        # Final check if any seq len < 3
        while heap:
            if heapq.heappop(heap)[1] < 3:
                return False

        return True

# @lc code=end
