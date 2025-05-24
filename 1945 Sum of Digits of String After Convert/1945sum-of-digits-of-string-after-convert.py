class Solution(object):
    def getLucky(self, s, k):
        a=[]
        for c in s:
            p=ord(c)-ord("a")+1
            a.append(str(p))
        n="".join(a)
        for i in range(k):
            sum=0
            for num in n:
                sum+=int(num)
                n=str(sum)
        return int(n)
        