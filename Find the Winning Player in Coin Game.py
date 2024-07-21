class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
        x = min(x , y//4)

        return "Alice" if x % 2 else "Bob"