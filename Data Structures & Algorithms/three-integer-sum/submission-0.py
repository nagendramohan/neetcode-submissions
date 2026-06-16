class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l , r = 0 , len(nums) -1 
        res = []

        while l < r :
            for i in range(len(nums)) :
                curSum = nums[l] + nums[r] + nums[i]
                if i == l:
                    i += 1
                if i == r :
                    i += 1

                if curSum  == 0 :
                    res.append([nums[l],nums[r],nums[i]])
                elif (curSum > 0):
                    r -= 1 
                else:
                    l += 1
            # l += 1
            # r -= 1
        res = [list(x) for x in set(tuple(sorted(x)) for x in res)]
        return res
        # return res
        