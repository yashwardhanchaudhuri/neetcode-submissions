class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([
            [position[i], (target - position[i]) / speed[i]]
            for i in range(len(position))
        ], reverse=True)

        count, lt = 0, 0

        for _, time in cars:
            if time > lt:
                count += 1
                lt = time

        return count