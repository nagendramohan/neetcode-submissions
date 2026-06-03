class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = set()
        for num in nums:
            if num in visit:
                return True 
            else :
                visit.add(num)
        return False
