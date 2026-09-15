class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [3,4.5,10,3] --> [10, 4.5, 3, 3]

        stack =  sorted([[position[i], ((target - position[i])/speed[i])] for i in range(len(position))], reverse = True)

        count, lt = 0, 0
        for i in stack:
            if i[-1] > lt:
                count += 1
                lt = i[-1]

        return count
