class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def dfs(i,target,path):
            if target==0:
                result.append(path[:])
                return
            if target<0 or i==len(candidates):
                return
            path.append(candidates[i])
            dfs(i,target-candidates[i],path)
            path.pop()
            dfs(i+1,target,path)
        dfs(0,target,[])
        return result