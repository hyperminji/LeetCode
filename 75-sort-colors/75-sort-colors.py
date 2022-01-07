class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0,0, len(nums)
        
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white +=1
                red += 1
            elif nums[white] > 1:
                blue-= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
                                               
        
        
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point0 = 0
        point2 = len(nums) -1
        
        i = 0
        count = 0 # 정렬완료된 원소
        
        while count < len(nums):
            if nums[i] == 0:  # 0 이라면 point0자리로 이동
                nums[i], nums[point0] = nums[point0], nums[i]
                point0 = point0+1
                i = i +1
            elif nums[i] ==1:  #1자리에 제대로 있으므로 pass
                i = i+1
            else: #2일경우 point2로 이동
                nums[i], nums[point2] = nums[point2], nums[i]
                point2= point2-1
            count = count+1 #정렬완료
#네덜란드국기문제
        
                
        
'''
        