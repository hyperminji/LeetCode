class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1+n2
        
        end = n//2
        i, i1, i2 = 0,0,0
        curr, prev = 0, 0
        
        while i <= end:
            prev = curr
            if i1 == n1:
                curr = nums2[i2]
                i2+=1
            elif i2 == n2:
                curr = nums1[i1]
                i1 +=1
            elif nums1[i1]< nums2[i2]:
                curr = nums1[i1]
                i1+=1
            else:
                curr = nums2[i2]
                i2 +=1
            i += 1
        if n % 2 == 0:
            return (prev+ curr) / 2.0
        else:
            return curr
    