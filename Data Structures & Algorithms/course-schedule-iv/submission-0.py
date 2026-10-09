from collections import deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, num_courses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = [[] for _ in range(num_courses)]
        in_degree = [0] * num_courses

        for u, v in prerequisites:
            adj_list[u].append(v)
            in_degree[v] += 1

        # Track all indirect & direct prerequisites for each course
        is_prereq = [set() for _ in range(num_courses)]

        # Start BFS with all nodes that have in_degree == 0
        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])

        while queue:
            curr = queue.popleft()

            for neighbor in adj_list[curr]:
                # The neighbor inherits 'curr' AND all of 'curr's prerequisites
                is_prereq[neighbor].add(curr)
                is_prereq[neighbor].update(is_prereq[curr])

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Answer queries in O(1) time
        return [pre in is_prereq[course] for pre, course in queries]