class Solution:
    def rotateString(self, s, goal):
        if len(s)==len(goal) and goal in s+s:
            return True
        else:
            return False