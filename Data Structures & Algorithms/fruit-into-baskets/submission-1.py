class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding Window - II
        count = defaultdict(int)
        l = 0 

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0 :
                    count.pop(fruits[l])
                l += 1 

            return len(fruits) - l  


        
        
        
        
        
        
        
        # Sliding Window - I
        count = defaultdict(int)
        l , total, res = 0,0,0

        for r in range(len(fruits)):
            count[fruits[r]] += 1 
            total += 1 

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1 
                total -= 1 
                l += 1 
                if not count[f]:
                    count.pop(f)
            res = max(res, total)
        return res 


        # B force 
        # n = len(fruits)
        # res = 0
        # for i in range(n):
        #     types = set()
        #     j = i 
        #     while j < n and (len(types) < 2 or fruits[j] in types ):
        #         types.add(fruits[j])
        #         j += 1
        #     res = max(res, j - i)
        # return res 
        