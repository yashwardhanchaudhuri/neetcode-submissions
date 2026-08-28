class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        c1, c2 = 0, 0
        mapping = {}

        for i in nums:
            mapping[i] = mapping.get(i, 0) + 1
            if i == candidate1:
                c1 += 1
            elif i == candidate2:
                c2 += 1
            else:
                if c1 == 0:
                    candidate1 = i
                    c1 += 1
                elif c2 == 0:
                    candidate2 = i
                    c2 += 1
                else:
                    c1 -= 1
                    c2 -= 1
        c1 = c2 = 0

        for x in nums:
            if x == candidate1:
                c1 += 1
            elif x == candidate2:
                c2 += 1

        result = []

        if c1 > len(nums) // 3:
            result.append(candidate1)

        if c2 > len(nums) // 3:
            result.append(candidate2)

        return result
        