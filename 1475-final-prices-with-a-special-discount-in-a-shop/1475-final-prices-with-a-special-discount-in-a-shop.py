class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        stack=[]
        for i in range(n):
            while stack and prices[i]<=prices[stack[-1]]:
                index=stack.pop()
                prices[index]=prices[index]-prices[i]
            stack.append(i)
        return prices