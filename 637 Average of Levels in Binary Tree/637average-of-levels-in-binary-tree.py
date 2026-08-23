from collections import deque

class Solution:
    def averageOfLevels(self, root):
        queue = deque([root])
        ans = []

        while queue:
            total = 0
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(total / n)

        return ans