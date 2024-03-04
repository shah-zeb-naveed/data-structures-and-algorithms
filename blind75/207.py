class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # make graph
        courses = {i : [] for i in range(numCourses)}
        for p in prerequisites:
            courses[p[0]].append(p[1])
        
        visited = set()
        #completed = set()

        def dfs(course):
            # if course in completed:
            #     return True

            if courses[course] == []:
                return True

            if course in visited:
                return False

            visited.add(course)
            
            for prereq in courses[course]:
                if not dfs(prereq): return False
 
            courses[course] = []
            return True

        for course in courses:
            if not dfs(course): return False

        return True