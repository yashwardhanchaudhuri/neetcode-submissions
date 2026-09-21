class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def dayc(arr, cap):
            used_days = 1
            curr = 0

            for weight in arr:
                if curr + weight > cap:
                    used_days += 1
                    curr = 0

                curr += weight

            return used_days

        left, right = max(weights), sum(weights)

        while left <= right:
            mid = left + (right - left)//2
            time = dayc(weights, mid)
            if time > days:
                left = mid + 1
            else:
                right = mid - 1

        return left