class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = left + (right - left)//2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True

        idx = left - 1
        print(idx)
        left, right = 0, len(matrix[idx]) - 1

        while left <= right:
            mid = left + (right - left)//2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False