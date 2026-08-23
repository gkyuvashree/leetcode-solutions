class Solution:
    def findSecondMinimumValue(self, root):
        values = set()

        def dfs(node):
            if not node:
                return

            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        values = sorted(values)

        return values[1] if len(values) > 1 else -1