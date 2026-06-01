class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total_cost = 0
        
        for i in range(len(cost)):
            # Skip every 3rd candy (indices 2, 5, 8, etc.) as they are free
            if i % 3 != 2:
                total_cost += cost[i]
                
        return total_cost

        