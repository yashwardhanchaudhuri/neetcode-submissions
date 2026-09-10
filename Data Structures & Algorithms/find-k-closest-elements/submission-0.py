class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []
        for i in arr:
            temp.append(abs(x - i))
        
        l,r = 0, len(arr) - 1
        while (l<r) and (r - l + 1) > k:
            if temp[r] >= temp[l]:
                r -= 1
            else:
                l += 1
        
        return [arr[i] for i in range(l, r+ 1)]
        