class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(len(points)):
            slopes = {}
            same = 1

            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    same += 1
                    continue

                if dx == 0:
                    slope = (1, 0)
                elif dy == 0:
                    slope = (0, 1)
                else:
                    from math import gcd
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

            ans = max(ans, same + max(slopes.values(), default=0))

        return ans