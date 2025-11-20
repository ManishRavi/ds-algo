#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start

# * Hierholzer's Algorithm Solution | O(ElogE) Time | O(E) Space
# * E -> The number of edges in the graph


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        res = []
        stack = ["JFK"]

        def build_graph():
            for src, dest in sorted(tickets, reverse=True):
                graph[src].append(dest)

        build_graph()
        while stack:
            cur_airport = stack[-1]
            if not graph[cur_airport]:
                res.append(stack.pop())
            else:
                stack.append(graph[cur_airport].pop())

        return res[::-1]


# @lc code=end
