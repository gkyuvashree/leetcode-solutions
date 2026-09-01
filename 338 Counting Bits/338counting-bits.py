class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            c=0
            while i:
                if i%2==1:
                    c+=1
                i//=2
            ans.append(c)
        return ans