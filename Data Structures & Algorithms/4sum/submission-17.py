class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        temp = []
        for i in range(1, len(nums) - 2):
            a = nums[i - 1]
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue
            for j in range(i, len(nums) - 2):
                # if j > i and nums[j] == nums[j - 1]:
                #     continue
                b = nums[j]
                k = j + 1
                l = len(nums) - 1
                balance = target - a - b

                while k < l:
                    c = nums[k]
                    d = nums[l]
                    if balance == c + d:
                        if [a,b,c,d] not in temp:
                            temp.append([a,b,c,d])
                                    
                        # while k < l and nums[k] == nums[k + 1]:
                        #     k += 1

                        # while k < l and nums[l] == nums[l - 1]:
                        #     l -= 1
                        k += 1
                        l -= 1
                    elif balance > c + d:
                        k += 1
                    else:
                        l -= 1
        return temp
