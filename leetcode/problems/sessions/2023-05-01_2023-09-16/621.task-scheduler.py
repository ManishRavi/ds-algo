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
        max_heap = [-task_cnt for task_cnt in tasks_counter.values()]
        heapify(max_heap)
        queue = deque()
        total_time = 0
        while max_heap or queue:
            total_time += 1
            if not max_heap:
                total_time = queue[0][1]
            else:
                heap_cnt = -heappop(max_heap)
                heap_cnt -= 1
                if heap_cnt:
                    queue.append((-heap_cnt, total_time + n))

            if queue and queue[0][1] == total_time:
                heappush(max_heap, queue.popleft()[0])

        return total_time


# @lc code=end
