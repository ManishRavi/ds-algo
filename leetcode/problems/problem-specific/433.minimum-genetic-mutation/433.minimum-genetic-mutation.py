#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start

# * Iterative BFS Solution | O((n^2)*m) Time | O((n^2)*m) Space
# * n -> The length of bank array | m -> The length of each string


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1

        if start not in bank:
            bank.append(start)
        # * Key -> Pattern | Value -> Array
        graph = collections.defaultdict(list)

        def build_graph():
            for word in bank:
                for i in range(len(word)):
                    graph[f"{word[:i]}*{word[i+1:]}"].append(word)

        build_graph()
        # * Start BFS traversal.
        queue = collections.deque([start])
        visited_set = set([start])
        res = 0
        while queue:
            for _ in range(len(queue)):
                cur_word = queue.popleft()
                if cur_word == end:
                    return res

                for i in range(len(cur_word)):
                    for neighbor in graph[f"{cur_word[:i]}*{cur_word[i+1:]}"]:
                        if neighbor not in visited_set:
                            queue.append(neighbor)
                            visited_set.add(neighbor)

            res += 1

        return -1


# @lc code=end
