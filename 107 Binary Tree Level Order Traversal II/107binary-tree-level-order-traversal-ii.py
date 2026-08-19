from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []

        q = deque([root])
        result = []

        while q:
            level = []

            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            result.append(level)

        return result[::-1]