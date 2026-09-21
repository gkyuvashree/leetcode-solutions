class Solution:
    def rob(self, root: TreeNode | None) -> int:

        def f(root):
            if not root:
                return (0, 0)

            l = f(root.left)
            r = f(root.right)

            return (root.val + l[1] + r[1], max(l) + max(r))

        return max(f(root))