#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start

# * Iterative BFS Solution | O(v+e) Time | O(v) Space
# * v -> The length of rooms array | e -> The total number of keys


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_set = set([0])
        queue = collections.deque([0])
        while queue:
            cur_room = queue.popleft()
            for key in rooms[cur_room]:
                if key not in visited_set:
                    queue.append(key)
                    visited_set.add(key)

        return len(rooms) == len(visited_set)


# @lc code=end
