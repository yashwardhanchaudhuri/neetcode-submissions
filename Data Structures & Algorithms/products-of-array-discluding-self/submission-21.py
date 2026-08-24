class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1]

        for i in range(0, len(nums) - 1):
            temp.append(temp[-1]*nums[i])

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            temp[i] *= product
            product *= nums[i]

        return temp