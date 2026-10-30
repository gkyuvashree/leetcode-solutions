class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        ans = []

        for i in range(len(even)):
            ans.append(even[i])
            ans.append(odd[i])

        return ans