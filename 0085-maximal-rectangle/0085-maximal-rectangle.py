class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []

            for j in range(cols + 1):
                h = heights[j] if j < cols else 0

                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]

                    width = j if not stack else j - stack[-1] - 1

                    ans = max(ans, height * width)

                stack.append(j)

        return ans