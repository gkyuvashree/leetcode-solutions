class Solution:
    def toGoatLatin(self, sentence):
        vowels = "aeiouAEIOU"
        words = sentence.split()
        ans = []

        for i, word in enumerate(words):
            if word[0] in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"

            word += "a" * (i + 1)
            ans.append(word)

        return " ".join(ans)