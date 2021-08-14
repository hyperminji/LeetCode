#현재온도를 stack에 저장
#현재온도 > stack , stack.pop() 현재-stack 를 정답으로
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        
        for i , today in enumerate(temperatures):
            while stack and today > temperatures[stack[-1]]:
                last= stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer
    
        