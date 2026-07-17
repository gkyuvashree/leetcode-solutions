class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        for l in columnTitle:
            value=ord(l)-ord('A')+1
            ans=ans*26
            ans=ans+value
        return ans