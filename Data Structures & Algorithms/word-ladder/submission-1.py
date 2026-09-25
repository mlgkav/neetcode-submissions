class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Build a graph where nodes are words and edges describe possible transformations.
        Perform a DFS/BFS from beginWord to endWord to determine the shortest path of transformations
        """
        # Map wildcard patterns to hash table buckets
        pattern_map = defaultdict(list) # adjacency list
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        q = deque([beginWord])
        visited = set([beginWord])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return level

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in pattern_map[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

        return 0
                