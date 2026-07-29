class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        max_f=0
        longest=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            max_f=max(count[s[r]],max_f)
            replacement=(r-l+1)-max_f
            while replacement>k:
                count[s[l]]-=1
                l+=1
                max_f=max(count.values())
                replacement=(r-l+1)-max_f
            longest=max(longest,r-l+1)
        return longest