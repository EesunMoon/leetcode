class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # have to calculate maximum health
        
        maxDamage = max(damage) # O(n)
        if maxDamage > armor:
            maxDamage = armor

        return sum(damage) + 1 - maxDamage
            