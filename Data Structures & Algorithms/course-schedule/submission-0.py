class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list) # maps each course 
        for a, b in prerequisites:
            pre_map[b].append(a)
        
        visit_set = set()
        def dfs(course):
            if course in visit_set:
                print(course)
                return False
            
            visit_set.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False

            pre_map[course] = []
            visit_set.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        