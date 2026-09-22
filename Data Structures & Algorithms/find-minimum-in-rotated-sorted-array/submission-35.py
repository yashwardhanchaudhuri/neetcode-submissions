class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        answer = nums[0]
        while left <= right:
            mid = left + (right - left)//2
            print(left, right, mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                answer = min(answer, nums[mid])
                right = mid - 1

        
        return answer