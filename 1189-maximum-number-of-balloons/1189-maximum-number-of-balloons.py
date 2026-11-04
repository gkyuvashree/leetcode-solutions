class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        count = []

        for ch in set(word):
            count.append(text.count(ch) // word.count(ch))

        return min(count)