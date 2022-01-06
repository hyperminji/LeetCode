class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            
            #모든 경우의 수를 dfs하고 백트래킹으로 결과를 조합하게 됨
            if len(path) == len(digits):
                result.append(path)
                return
             
        
            #입력값 반복
            for i in range(index, len(digits)):
                for j in dic[digits[i]]: #숫자에 해당하는 모든 문자열 반복(키판배열)
                    dfs(i+1, path+j)
                    
        #예외처리- 숫자 키패드가 아닌경우
        if not digits:
            return []
        
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = []
        dfs(0,"")
        
        return result
        
        
        
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #예외처리
        if not digits:
            return []
        #문자입력 딕셔너리로
        digi = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        answer = ['']
        
        for d in digits:
            tmp = []
            for a in answer:
                for i in digi[d]:
                    tmp.append(a+i)
                answer = tmp
        return answer
                '''