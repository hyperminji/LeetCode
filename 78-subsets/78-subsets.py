class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        def dfs(index,path):
            result.append(path)
            
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
                #경로(path)를 만들면서 인덱스를 1씩 증가-> 깊이 탐색
        dfs(0, [])
        return result
        
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[]]
        
        for i in nums:
            result = result + [current + [i] for current in result]
            
        return result
'''
        