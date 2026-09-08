class Solution:
    def trap(self, height: List[int]) -> int:
        #Find residuals in comparisons to minimum of maximum left and right heights to it
        l, r = 0, len(height) - 1
        l_max = height[l]
        r_max = height[r]
        water = 0

        while l <= r:

            if l_max <= r_max:
                l_max = max(l_max, height[l])
                water += l_max - height[l]
                l += 1

            else:
                r_max = max(r_max, height[r])
                water += r_max - height[r]
                r -= 1

        return water