# * Priority Queue Solution | O(nlogn) Time | O(n) Space

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        max_heap = []
        for num in target:
            heappush(max_heap, -num)

        total_sum = sum(target)
        while max_heap:
            top_val = -max_heap[0]
            rem_sum = total_sum-top_val
            heappop(max_heap)
            total_sum -= top_val
            if rem_sum == 1 or top_val == 1:
                return True
            if rem_sum > top_val or rem_sum == 0 or top_val % rem_sum == 0:
                return False

            heappush(max_heap, -(top_val % rem_sum))
            total_sum += top_val % rem_sum

        return False
