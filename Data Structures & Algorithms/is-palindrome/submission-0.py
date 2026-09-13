class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearS = ""
        for c in s:
            if c.isalnum():
                clearS+=c.lower()
        
        i=0
        j=len(clearS)-1
        while i<j:
            if clearS[i]==clearS[j]:
                i+=1
                j-=1
                continue
            return False

        return True