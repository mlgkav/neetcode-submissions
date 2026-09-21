class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build map of courses to a list of their prereqs
        pre_map = defaultdict(list)
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        
        res = []
        # visit tracks fully processed courses, cycle tracks DFS path (cycle detection)
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
