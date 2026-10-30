class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []

        for i in set(words[0]):
            mini = min(word.count(i) for word in words)

            for j in range(mini):
                ans.append(i)

        return ans