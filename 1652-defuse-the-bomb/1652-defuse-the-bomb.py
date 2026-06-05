class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        # Base Case: If k is 0, return all zeros immediately
        if k == 0:
            return [0] * n
        result = [0] * n        
        for i in range(n):
            current_sum = 0          
            if k > 0:
                # Sum the next k elements
                for j in range(1, k + 1):
                    current_sum += code[(i + j) % n]
            else:
                # Sum the previous |k| elements
                # code[(i - j) % n] correctly wraps backward in Python
                for j in range(1, abs(k) + 1):
                    current_sum += code[(i - j) % n]                    
            result[i] = current_sum           
        return result
