class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
        
        
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #순열
        result = []
        prev_ele = []
        
        def dfs(ele):
            #자식노드에 도달했을 때 결과에 하나씩 추가 
            if len(ele) == 0:
                result.append(prev_ele[:]) #[:]으로 해서 참조가 아닌 값 복사
                
            
            #순열 재귀 
            for e in ele:
                next_ele = ele[:]
                next_ele.remove(e) #확인한것 지우기
                
                prev_ele.append(e)
                dfs(next_ele)
                prev_ele.pop()
        
        dfs(nums)
        return result
        
'''