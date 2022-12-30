#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

# @lc code=start

# * Sorting and Priority Queue (Min Heap) Solution | O(nlogn) Time | O(n) Space
# * n -> The length of tasks array


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # * Store the index to be able to persist it after sorting as we need to return it.
        for idx, task in enumerate(tasks):
            task.append(idx)

        tasks.sort()
        res, min_heap = [], []
        i, cur_time = 0, tasks[0][0]

        while min_heap or i < len(tasks):
            # * Push all the available tasks into the Min Heap.
            while i < len(tasks) and cur_time >= tasks[i][0]:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if not min_heap:
                cur_time = tasks[i][0]
            else:
                processing_time, index = heapq.heappop(min_heap)
                cur_time += processing_time
                res.append(index)

        return res


# @lc code=end
