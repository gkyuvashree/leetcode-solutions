class Solution(object):
    def addBinary(self, a, b):
        i=len(a)-1
        j=len(b)-1
        carry=0
        result=[]
        while i>=0 or j>=0 or carry>0:
            if i>=0:
                da=int(a[i])
            else:
                da=0
            if j>=0:
                db=int(b[j])
            else:
                db=0
            total=da+db+carry
            if total%2==0:
                result.append("0")
            else:
                result.append("1")
            carry=total//2
            i-=1
            j-=1
        result.reverse()
        return"".join(result)
        