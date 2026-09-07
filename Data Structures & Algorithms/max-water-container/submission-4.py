class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ar = 0

        while l < r:
            w = r - l
            h = min(heights[r], heights[l])
            a = w*h

            ar = max(ar, a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ar
        