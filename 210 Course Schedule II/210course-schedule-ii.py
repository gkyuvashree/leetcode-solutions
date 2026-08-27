class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses
        answer = []

        def dfs(course):

            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for nextcourse in graph[course]:
                if not dfs(nextcourse):
                    return False

            state[course] = 2
            answer.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return answer[::-1]