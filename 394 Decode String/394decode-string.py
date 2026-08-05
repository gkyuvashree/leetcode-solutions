class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        ans=""
        num=0
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=="[":
                stack.append((ans,num))
                ans=""
                num=0
            elif ch=="]":
                prev,repeat=stack.pop()  
                ans=prev+ans*repeat 
            else:
                ans+=ch    
        return ans