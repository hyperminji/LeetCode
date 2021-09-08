class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #0을 리스트에서 지우고 0을 append로 넣는다.
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)