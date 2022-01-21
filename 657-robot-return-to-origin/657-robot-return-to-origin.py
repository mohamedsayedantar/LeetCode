class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("U")==moves.count("D") and moves.count("R")==moves.count("L"):
            return True
        return False
        
        