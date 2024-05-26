class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        mid = n // 2
        return (merged[mid] + merged[mid - 1]) / 2.0 if n % 2 == 0 else merged[mid]
        