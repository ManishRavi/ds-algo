#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start

# * Priority Queue (Max Heap) and Queue Solution | O(n) Time | O(n) Space
# * n -> The length of tasks array


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n <= 0:
            return len(tasks)

        tasks_counter = Counter(tasks)
        max_heap = [-task_count for task_count in tasks_counter.values()]
        heapify(max_heap)
        queue = deque()
        total_time = 0
        while max_heap or queue:
            total_time += 1
            if not max_heap:
                total_time = queue[0][1]
            else:
                task_count = -heappop(max_heap)
                task_count -= 1
                if task_count:
                    queue.append((task_count, total_time + n))

            if queue and queue[0][1] == total_time:
                task_count, _ = queue.popleft()
                heappush(max_heap, -task_count)

        return total_time


# @lc code=end
