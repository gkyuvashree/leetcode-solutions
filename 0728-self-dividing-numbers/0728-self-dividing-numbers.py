class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):
            temp = i
            valid = True

            while temp > 0:
                digit = temp % 10

                if digit == 0 or i % digit != 0:
                    valid = False
                    break

                temp //= 10

            if valid:
                ans.append(i)

        return ans