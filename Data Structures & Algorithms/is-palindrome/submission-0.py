class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ", "").lower()
        # s = ''.join(s.split()).lower()
        s = ''.join(char for char in s if char.isalnum()).lower()
        # print("s is ", s)
        l , r = 0, len(s) -1  
        while l <= r:
            if s[l] == s[r] :
                l += 1
                r -= 1
            else :
                return False
        return True  

        