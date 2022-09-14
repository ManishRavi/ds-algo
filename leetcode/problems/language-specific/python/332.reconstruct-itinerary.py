#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start

# * Recursive DFS and Eulerian Path Solution | O((v+e)^2) Time | O(v+e) Space
# * v -> The number of vertices in the graph | e -> The number of edges in the graph


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # * Sort in lexical order.
        tickets.sort()
        graph = {src: [] for src, _ in tickets}
        res = ["JFK"]

        def build_graph():
            for src, dest in tickets:
                graph[src].append(dest)

        def findItineraryHelper(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in graph:
                return False

            for idx, dest in enumerate(graph[src]):
                if dest == "*":
                    continue

                graph[src][idx] = "*"
                res.append(dest)
                if findItineraryHelper(dest):
                    return True

                graph[src][idx] = dest
                res.pop()
            return False

        build_graph()
        findItineraryHelper("JFK")
        return res


# @lc code=end
