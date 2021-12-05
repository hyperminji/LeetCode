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
        
        
        