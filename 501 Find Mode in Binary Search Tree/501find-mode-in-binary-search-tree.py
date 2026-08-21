class Solution:
    def findMode(self, root):
        a = []
        def f(n):
            if n:
                f(n.left)
                a.append(n.val)
                f(n.right)
        f(root)

        m = max(a.count(x) for x in a)
        return [x for x in set(a) if a.count(x) == m]