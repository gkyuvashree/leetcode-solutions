
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        answer = []

        for s in score:
            rank = sorted_score.index(s) + 1

            if rank == 1:
                answer.append("Gold Medal")
            elif rank == 2:
                answer.append("Silver Medal")
            elif rank == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(rank))

        return answer
