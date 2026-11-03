class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        for num in count:
            if count[num] > len(arr) // 4:
                return num