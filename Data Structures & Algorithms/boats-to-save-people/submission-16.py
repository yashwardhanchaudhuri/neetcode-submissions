class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #minimum number of pairs of numbers s.t. s(x,y) == limit
        people.sort()

        l, r = 0, len(people) - 1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                count += 1
            else:
                r -= 1
                count += 1
                   
        return count