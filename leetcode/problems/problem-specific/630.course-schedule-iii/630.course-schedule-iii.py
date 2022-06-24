# * Priority Queue Solution | O(nlogn) Time | O(n) Space

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        max_heap = []
        total_duration = 0
        for duration, last_day in sorted(courses, key=lambda x: x[1]):
            heapq.heappush(max_heap, -duration)
            total_duration += duration
            if total_duration > last_day:
                total_duration += heapq.heappop(max_heap)

        return len(max_heap)
