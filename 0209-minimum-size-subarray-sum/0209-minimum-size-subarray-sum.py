class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        left=0
        cur_sum=0
        min_len=float("inf")
        for right  in range(len(arr)):
            cur_sum=cur_sum+arr[right]
            while cur_sum>=target:
                min_len=min(min_len,right-left+1)
                cur_sum=cur_sum-arr[left]
                left=left+1
        if min_len==float("inf"):
            return 0
        return min_len
            