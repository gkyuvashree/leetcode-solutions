class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float('inf')]*(n+1)
        dist[k]=0
        for _ in range(n-1):
            for u,v,w in times:
                if dist[u]!=float('inf'):
                    dist[v]=min(dist[v],dist[u]+w)
        ans=max(dist[1:])
        if ans==float('inf'):
            return -1
        else:
            return ans