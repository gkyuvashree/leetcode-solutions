class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def dfs(start,target,path):
            if k==len(path):
                if target==0:
                    ans.append(path[:])
                return
            for i in range(start,10):
                if i>target:
                    break
                path.append(i)
                dfs(i+1,target-i,path)
                path.pop()
                
        dfs(1,n,[])
        return ans