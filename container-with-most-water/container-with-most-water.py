class Solution:
    def maxArea(self, height: List[int]) -> int:
        #max_water=0
        #n= len(height)
        
        #for i in range(n):
        #    for j in range(i+1, n):
        #        max_water = max((j-i)*min(height[i], height[j]), max_water)
        #return max_water
    
    # 선 사이의 높이를 세로로 하는 직사각형으로 만들고 그 영역의 최대값을 구한다.
        #time터짐
        low=0
        high = len(height)-1
        ans = 0
        while low<high:
            if height[low]<height[high]:
                min_he = height[low]
                min_he_index = low
            else:
                min_he = height[high]
                min_he_index = high
            ans = max((high - low)*min_he, ans)
            if low+1 == min_he_index+1:
                low= low+1
            else:
                high = high-1
        return ans
    
        