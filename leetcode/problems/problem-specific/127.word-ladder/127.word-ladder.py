#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

# * Iterative BFS Solution | O((n^2)*m) Time | O((n^2)*m) Space
# * n -> The length of wordList array | m -> The length of each string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)
        # * Key -> Pattern | Value -> Array
        graph = collections.defaultdict(list)

        def build_graph():
            for word in wordList:
                for i in range(len(word)):
                    graph[f"{word[:i]}*{word[i+1:]}"].append(word)

        build_graph()
        # * Start BFS traversal.
        queue = collections.deque([beginWord])
        visited_set = set([beginWord])
        res = 1
        while queue:
            for _ in range(len(queue)):
                cur_word = queue.popleft()
                if cur_word == endWord:
                    return res

                for i in range(len(cur_word)):
                    for neighbor in graph[f"{cur_word[:i]}*{cur_word[i+1:]}"]:
                        if neighbor not in visited_set:
                            queue.append(neighbor)
                            visited_set.add(neighbor)

            res += 1

        return 0


# @lc code=end
