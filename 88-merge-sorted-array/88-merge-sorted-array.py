class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums1의 길이 m+n
        #nums2의 길이 n
        if n > 0:
            nums1[-n:] = nums2
            nums1.sort()