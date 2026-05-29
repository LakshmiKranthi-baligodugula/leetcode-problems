
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack= []        
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            res= -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res = nums2[j]
                    break                   
            stack.append(res)            
        return stack

            

        