
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]

        if old == color:
            return image

        m = len(image)
        n = len(image[0])

        def fill(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if image[r][c] != old:
                return

            image[r][c] = color

            fill(r + 1, c)
            fill(r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)

        fill(sr, sc)
        return image
