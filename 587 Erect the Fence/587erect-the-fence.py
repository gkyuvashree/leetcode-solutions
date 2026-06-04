class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees)<=1:
            return trees
        trees.sort()
        def cross(o,a,b):
            return((a[0]-o[0])*(b[1]-o[1]))-((a[1]-o[1])*(b[0]-o[0]))
        l=[]
        for p in trees:
            while len(l)>=2 and cross(l[-2],l[-1],p)<0:
                l.pop()
            l.append(p)
        u=[]
        for p in reversed(trees):
            while len(u)>=2 and cross(u[-2],u[-1],p)<0:
                u.pop()
            u.append(p)
        return list(set(map(tuple,l+u)))