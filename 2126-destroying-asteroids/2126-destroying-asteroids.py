class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Sort to face the smallest asteroids first
        asteroids.sort()
        
        for ast in asteroids:
            # If current mass is too small, the planet is destroyed
            if mass < ast:
                return False
            # Accumulate mass upon successful destruction
            mass += ast
            
        return True
