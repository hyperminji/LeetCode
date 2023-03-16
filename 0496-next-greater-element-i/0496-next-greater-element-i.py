class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgre = {}
        stack=[]
        
        for num in nums2:
            while stack and num > stack[-1]:
                nextgre[stack.pop()] = num
            stack.append(num)
        result=[]
        for num in nums1:
            if num in nextgre:
                result.append(nextgre[num])
            else:
                result.append(-1)
        return result
