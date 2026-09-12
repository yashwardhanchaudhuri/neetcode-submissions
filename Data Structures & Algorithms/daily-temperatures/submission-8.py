class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        answer = [0]*len(arr)
        stack = []

        for i in range(len(arr)):
            if len(stack) == 0:
                stack.append(i)
            else:
                if arr[stack[-1]] < arr[i]:
                    while len(stack) and (arr[stack[-1]] < arr[i]):
                        answer[stack[-1]] = i - stack[-1]
                        stack.pop()

                stack.append(i)
        return answer
                    