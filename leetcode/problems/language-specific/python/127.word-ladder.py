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
                    graph[word[:i] + "*" + word[i+1:]].append(word)

        build_graph()
        # * BFS Traversal
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        result = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result

                for i in range(len(word)):
                    for neighbour in graph[word[:i] + "*" + word[i+1:]]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)

            result += 1

        return 0

# @lc code=end
