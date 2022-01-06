class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result =[]
        
        def dfs(ele, start:int, k:int):
            #k값을 전달받아 1씩 줄이면서 재귀 -> 0이 되면 빠져나간다
            #남아있는 값끼리 나머지 조합을 이뤄야 한다. k=0이 되면 결과에 삽입한다
            if k == 0:
                result.append(ele[:])
                return
            
            #자신 이전의 모든 값을 고정해 재귀, 
            #k개의 조합만을 만들어야함
            for i in range(start, n+1):
                ele.append(i)
                dfs(ele, i+1, k-1)
                ele.pop()
                
        dfs([],1,k)  
        return result
        