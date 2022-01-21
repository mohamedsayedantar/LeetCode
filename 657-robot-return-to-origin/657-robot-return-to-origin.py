class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0]
        for char in moves:
            if char=="U":
                start[1] += 1
            elif char=="D":
                start[1] -= 1
            elif char=="R":
                start[0] += 1
            else:
                start[0] -= 1
                
        if start == [0, 0]:
            return True
        return False
        