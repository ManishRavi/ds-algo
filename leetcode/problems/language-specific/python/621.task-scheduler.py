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

        task_counter = collections.Counter(tasks)
        # * Stores the task count.
        max_heap = [-task_count for task_count in task_counter.values()]
        heapq.heapify(max_heap)
        total_time = 0
        # * Stores a pair of count and available time.
        # * Pair -> (count, available_at)
        queue = collections.deque()

        while max_heap or queue:
            total_time += 1
            # * If the heap is empty then update total_time to 1st element in the queue
            # * since that's the idle time to process the next task.
            if not max_heap:
                total_time = queue[0][1]
            else:
                heap_count = -heapq.heappop(max_heap)
                heap_count -= 1
                if heap_count:
                    queue.append((-heap_count, total_time + n))

            # * If the task is available to process
            if queue and queue[0][1] == total_time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return total_time

# @lc code=end
