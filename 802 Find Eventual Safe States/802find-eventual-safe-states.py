class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        state = [0] * len(graph)

        def dfs(node):

            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for nextnode in graph[node]:
                if not dfs(nextnode):
                    return False

            state[node] = 2
            return True

        answer = []

        for node in range(len(graph)):
            if dfs(node):
                answer.append(node)

        return answer