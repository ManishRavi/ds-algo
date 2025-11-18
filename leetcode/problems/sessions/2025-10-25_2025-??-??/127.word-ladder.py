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

        graph = defaultdict(list)

        def build_graph():
            for word in wordList:
                for idx in range(len(word)):
                    pattern = f"{word[:idx]}*{word[idx + 1:]}"
                    graph[pattern].append(word)

        build_graph()
        queue = deque([beginWord])
        visited_set = set([beginWord])
        res = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res

                for idx in range(len(word)):
                    pattern = f"{word[:idx]}*{word[idx + 1:]}"
                    for neighbor in graph[pattern]:
                        if neighbor not in visited_set:
                            queue.append(neighbor)
                            visited_set.add(neighbor)
            res += 1

        return 0


# @lc code=end
