from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if left_to_right:
                result.append(level)
            else:
                result.append(level[::-1])

            left_to_right = not left_to_right

        return result